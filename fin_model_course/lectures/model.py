import datetime
import itertools
import time
import warnings
from abc import ABC, abstractmethod
from weakref import ref, ReferenceType
from typing import Union, Sequence, Type, Optional, TYPE_CHECKING, TypeVar, List, Any
import urllib.parse

import more_itertools
from pydantic import BaseModel, AnyHttpUrl, ConfigDict
from pydantic.dataclasses import dataclass, rebuild_dataclass
from youtube_transcript_api import TranscriptsDisabled

from build_tools import yt_api
from build_tools.config import SITE_URL, LECTURE_YOUTUBE_DESCRIPTIONS_METADATA_PATH
from build_tools.ext_rst import header_rst
from build_tools.get_transcripts import Transcript, get_transcript
from build_tools.yt_api import YouTubeDescriptionIsCurrentException
from courses.config import COURSES
from courses.model import CourseModel, CourseSelectors
from pltemplates.frames.lab import LabFrame
from pltemplates.hyperlink import Hyperlink

if TYPE_CHECKING:
    from models.content import FileContentMetadata, LectureYouTubeDescriptionMetadata

import pyexlatex as pl


T = TypeVar("T")


class Serializable(BaseModel, ABC):

    @abstractmethod
    def to_pyexlatex(self):
        ...

    @abstractmethod
    def to_rst(self) -> str:
        ...

LectureNoteItem = "Union[str, Serializable, LectureNotes]"

@dataclass
class LectureNotes:
    items: "Sequence[Union[LectureNoteItem, Sequence[LectureNoteItem]]]"
    title: str

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def __getitem__(self, item):
        return self.items[item]

    def __bool__(self) -> bool:
        return bool(self.items)

    def to_models(
        self, top_model: Type[T] = pl.Section, sub_model: Type = pl.UnorderedList
    ) -> T:
        items = []
        for item in self:
            if isinstance(item, self.__class__):
                items.append(item.to_models(top_model=sub_model, sub_model=sub_model))
            else:
                items.append(item)

        # Collect strs into sub models
        final_items = []
        current_str_items = []
        for item in items:
            if isinstance(item, str):
                current_str_items.append(item)
            elif hasattr(item, 'to_pyexlatex'):
                current_str_items.append(item.to_pyexlatex())
            else:
                # Not a str item, so the str section has ended
                if current_str_items:
                    # Add collection of the str items and wipe str items
                    final_items.append(sub_model(current_str_items))
                    current_str_items = []
                # Now add the current not str item
                final_items.append(item)

        # If str items were last, will have some left over
        if current_str_items:
            final_items.append(sub_model(current_str_items))

        if top_model is not None:
            return top_model(final_items, title=self.title)

        return final_items

    def to_pyexlatex_content(self) -> list:
        return [to_pyexlatex_content(item) for item in self]

    def to_rst(self) -> str:
        lines = []
        for note in self:
            lines.extend(to_rst_bullet_content(note))
        return "\n" + "\n".join([f'- {line}' for line in lines]) + "\n"

    def to_youtube(self) -> str:
        lines = []
        for note in self:
            lines.extend(to_youtube_bullet_content(note))
        return "\n" + "\n".join([f'- {line}' for line in lines]) + "\n"


def to_pyexlatex_content(item: Any):
    if isinstance(item, str):
        return item
    if isinstance(item, (list, tuple)):
        out_items = []
        for sub_item in item:
            out_items.append(to_pyexlatex_content(sub_item))
        return out_items
    if hasattr(item, 'to_pyexlatex'):
        return item.to_pyexlatex()

    return item


def to_rst_bullet_content(item: Any) -> list:
    if isinstance(item, str):
        return [item]
    elif isinstance(item, (list, tuple)):
        return [' '.join(itertools.chain(*[to_rst_bullet_content(sub_item) for sub_item in item]))]
    elif hasattr(item, 'to_rst'):
        return [item.to_rst()]
    else:
        raise ValueError(f'could not serialize {item} of type {type(item)} to rst')


def to_youtube_bullet_content(item: Any) -> list:
    if isinstance(item, str):
        return [item]
    elif isinstance(item, (list, tuple)):
        return [' '.join(itertools.chain(*[to_youtube_bullet_content(sub_item) for sub_item in item]))]
    elif hasattr(item, 'to_youtube'):
        return [item.to_youtube()]
    else:
        raise ValueError(f'could not serialize {item} of type {type(item)} to youtube')

rebuild_dataclass(LectureNotes)

class Equation(Serializable):
    latex: str

    def to_pyexlatex(self):
        return pl.Equation(str_eq=self.latex)

    def to_rst(self) -> str:
        return f':math:`{self.latex}`'

    def to_youtube(self) -> str:
        return str(self.latex)


class Link(Serializable):
    href: AnyHttpUrl
    display_text: Optional[str] = None

    def to_pyexlatex(self) -> Hyperlink:
        return Hyperlink(str(self.href), self.display_text)

    def to_rst(self) -> str:
        if self.display_text:
            text = self.display_text.replace(r'_', r'\_')
            return f'`{text} <{self.href}>`_'

        # No display text
        return f'`<{self.href}>`_'

    def to_youtube(self) -> str:
        if self.display_text:
            return f'{self.display_text} ({self.href})'

        # No display text
        return f'{self.href}'


@dataclass
class LectureResource:
    name: str
    static_url: Optional[str] = None
    external_url: Optional[str] = None
    updated: Optional[datetime.datetime] = None
    index: Optional[int] = None
    datetime_fmt: str = "%B %e, %l:%M %p"

    def __eq__(self, other):
        try:
            return all([
                self.name == other.name,
                self.static_url == other.static_url,
                self.external_url == other.external_url
            ])
        except AttributeError:
            return False

    @classmethod
    def from_metadata(cls, md: "FileContentMetadata", url: Optional[str] = None) -> "LectureResource":
        from models.content import GeneratedContentMetadata
        if url is None:
            generated_content_subfolder = md.output_extension + "s"
            if isinstance(md, GeneratedContentMetadata):
                url = f"generated/{generated_content_subfolder}/{md.content_type_code}{md.content_index} {md.name}.{md.output_extension}"
            else:
                raise NotImplementedError('need to implement auto url for non-generated content')
        resource = cls(
            name=md.name,
            static_url=url,
            index=md.content_index,
            updated=md.last_modified,
        )
        return resource

    @property
    def url(self) -> Optional[str]:
        if self.static_url is not None:
            return f"/_static/{self.static_url}"
        if self.external_url is not None:
            return self.external_url
        return None

    @property
    def full_url(self) -> Optional[str]:
        if self.static_url is not None:
            return f'{SITE_URL}_static/{self.static_url}'
        if self.external_url is not None:
            return self.external_url
        return None

    @property
    def full_quoted_url(self) -> Optional[str]:
        url = self.full_url
        if url is None:
            return None
        parts: List[str] = list(urllib.parse.urlparse(url))
        parts[2] = urllib.parse.quote(parts[2])
        quoted_url = urllib.parse.urlunparse(parts)
        return quoted_url

    @property
    def display_name(self) -> str:
        name = ""
        if self.index is not None:
            name += f"{self.index} "
        name += self.name
        if self.updated is not None:
            name += f" (updated {self.updated.strftime(self.datetime_fmt)})"
        return name

    def to_pyexlatex(self) -> Hyperlink:
        return Hyperlink(self.full_url, self.display_name)

    def to_rst(self) -> str:
        if self.static_url is not None:
            return self._to_download_rst()
        if self.external_url is not None:
            return self._to_external_link_rst()
        raise ValueError(f'No link provided, cannot form RST in {self}')

    def _to_download_rst(self) -> str:
        return f"""
- :download:`{self.display_name} <{self.url}>`
        """

    def _to_external_link_rst(self) -> str:
        return f"""
- `{self.display_name} <{self.url}>`_
        """

    def to_youtube(self) -> str:
        return f"""
- {self.display_name}: {self.full_quoted_url}
        """.strip()


@dataclass(config=ConfigDict(arbitrary_types_allowed=True))
class Lecture:
    title: str
    week_covered: int
    notes: Optional[LectureNotes] = None
    youtube_id: Optional[str] = None
    resources: Optional[Sequence[LectureResource]] = None
    custom_tags: Sequence[str] = tuple()
    _transcript: Optional[Transcript] = None
    notes_section_name: str = 'Notes'
    _group_ref: Optional[ReferenceType] = None

    def to_rst(self) -> str:
        out_str = header_rst(self.title, 3)
        if self.youtube_id:
            out_str += self._youtube_rst
        else:
            out_str += self._youtube_alt_rst
        if self.notes:
            out_str += self._notes_rst
        else:
            out_str += self._notes_alt_rst
        out_str += self._resources_rst
        out_str += self._transcript_rst
        return out_str

    def youtube_title(self, include_group: bool = True, include_course: bool = False) -> str:
        title = self.title
        group = self.group
        if group is not None:
            if include_group:
                title += f' - {group.title}'
            if include_course:
                title += f' - {group.course.title}'
        return title

    @property
    def youtube_description(self) -> str:
        desc = self.youtube_title(include_group=False, include_course=False) + '\n\n'
        group = self.group
        if group is not None:
            desc += f'Part of the lecture series "{group.title}":\n{group.url}\n\n'
            desc += f'Full Course Website:\n{SITE_URL}\n\n'
        if self.notes:
            desc += self._notes_youtube
        desc += self._resources_youtube
        return desc

    @property
    def youtube_description_has_changed(self) -> bool:
        from models.content import LectureYouTubeDescriptionCollectionMetadata, LectureYouTubeDescriptionMetadata
        metadata_path = LECTURE_YOUTUBE_DESCRIPTIONS_METADATA_PATH
        if not metadata_path.exists():
            return True

        all_existing_metadata = LectureYouTubeDescriptionCollectionMetadata.parse_raw(metadata_path.read_text())
        existing_metadata = all_existing_metadata.items[self.youtube_id]
        current_metadata = LectureYouTubeDescriptionMetadata.generate_from_lecture(self)
        return existing_metadata != current_metadata

    def upload_youtube_description(self, youtube: Optional = None):
        if self.youtube_id is None:
            raise ValueError(f'cannot update youtube video with id: {self}')
        if self.group is None:
            raise ValueError(f'cannot update youtube video without lecture group: {self}')
        if not self.youtube_description_has_changed:
            raise YouTubeDescriptionIsCurrentException(
                f'{self.youtube_id} - {self.title} already has newest description, will not update'
            )
        if youtube is None:
            youtube = yt_api.get_authenticated_service()
        self._upload_youtube_description(youtube)

    def _upload_youtube_description(self, youtube):
        print(f'Uploading description for {self.youtube_id} - {self.title}')
        title = self.youtube_title(include_group=True, include_course=False)
        if len(title) > 100:
            warnings.warn(f'Not updating title {title} as it is too long')
            title = None
        yt_api.update_video_description(
            self.youtube_id,
            title=title,
            description=self.youtube_description,
            tags=self.tags,
            youtube=youtube,
            print_output=False
        )

    @property
    def tags(self) -> List[str]:
        tags = list(self.custom_tags)
        group = self.group
        if group is not None:
            tags.extend(group.custom_tags)
            tags.extend(group.course.tags)
        return tags

    def register_group(self, group: 'LectureGroup'):
        self._group_ref = ref(group)

    @property
    def group(self) -> Optional['LectureGroup']:
        if self._group_ref is None:
            return None
        return self._group_ref()

    @property
    def _youtube_rst(self) -> str:
        return f"""
.. youtube:: {self.youtube_id}
    :height: 315
    :width: 80%
    :align: center

|
            """

    @property
    def _youtube_alt_rst(self) -> str:
        return '\n**Video coming soon**\n'

    @property
    def _notes_rst(self) -> str:
        out_str = header_rst(self.notes_section_name, 4)
        out_str += self.notes.to_rst()
        return out_str

    @property
    def _notes_alt_rst(self) -> str:
        return '\n**Notes coming soon**\n'

    @property
    def _notes_youtube(self) -> str:
        out_str = header_rst(self.notes_section_name, 4)
        out_str += self.notes.to_youtube()
        return out_str

    @property
    def _resources_rst(self) -> str:
        out_str = ''
        if self.resources:
            out_str += (
                header_rst('Resources', 4)
                + "\n"
                + "\n".join([res.to_rst() for res in self.resources])
                + "\n"
            )
        return out_str

    @property
    def _resources_youtube(self) -> str:
        out_str = ''
        if self.resources:
            out_str += (
                    header_rst('Resources', 4)
                    + '\n'
                    + "\n".join([res.to_youtube() for res in self.resources])
            )
        return out_str

    @property
    def _transcript_rst(self) -> str:
        if not self.youtube_id:
            return ''

        try:
            transcript = self.transcript
        except TranscriptsDisabled:
            return ''

        out_str = header_rst('Transcript', 4)
        html = transcript.to_html()
        rst = f"""
.. raw:: html
    
    {html}

|
"""
        out_str += rst
        return out_str

    @property
    def transcript(self) -> Transcript:
        if self._transcript is not None:
            return self._transcript

        if not self.youtube_id:
            raise ValueError('cannot load transcript without YouTube ID')

        self._transcript = get_transcript(self.youtube_id)
        return self._transcript


@dataclass
class LectureGroup:
    title: str
    description: str
    lectures: Sequence[Lecture]
    order: Union[int, str]
    global_resources: Sequence[LectureResource] = tuple()
    course: CourseModel = COURSES[CourseSelectors.BASIC]
    show_aggregate_resources: bool = True
    custom_tags: Sequence[str] = tuple()

    def __post_init__(self):
        for lect in self.lectures:
            lect.register_group(self)

    def __getitem__(self, item):
        return self.lectures[item]

    @property
    def stub(self) -> str:
        lower = self.title.casefold()
        parts: List[str] = []
        if self.course.stub:
            parts.append(self.course.stub)
        parts.append(str(self.order))
        parts.extend(lower.split())
        return "-".join(parts)

    @property
    def url(self) -> str:
        return f'{SITE_URL}lectures/{self.stub}'

    @property
    def resources(self) -> List[LectureResource]:
        resources = list(self.global_resources)
        for lecture in self:
            if lecture.resources:
                for resource in lecture.resources:
                    if resource not in resources:
                        resources.append(resource)
        return resources

    @property
    def has_content(self) -> bool:
        for lecture in self:
            if lecture.youtube_id:
                return True
            if lecture.notes and lecture.notes.items:
                return True
        return False

    def to_models(
        self, top_model: Type[T] = pl.Section, sub_model: Type = pl.UnorderedList
    ) -> T:
        return [
            mod.notes.to_models(top_model=top_model, sub_model=sub_model)
            for mod in self
        ]

    def to_rst(self) -> str:
        out_str = header_rst(self.title, 2)
        out_str += f'\n{self.description}\n'
        if self.show_aggregate_resources and self.resources:
            out_str += (
                header_rst('Resources', 3)
                + "\n"
                + "\n".join([res.to_rst() for res in self.resources])
                + "\n"
            )
        for lecture in self:
            out_str += lecture.to_rst()
        return out_str

    def lectures_for_week(self, week_num: int) -> List[Lecture]:
        return [exc for exc in self.lectures if exc.week_covered == week_num]

    @property
    def pyexlatex_resources_frame(self) -> Optional[Sequence[LabFrame]]:
        if not self.resources:
            return None

        block_title = frame_title = 'Lecture Resources'
        label = 'frames:resources'

        pyexlatex_resources = [res.to_pyexlatex() for res in self.resources]
        resource_chunks = list(more_itertools.chunked(pyexlatex_resources, 10))
        if len(resource_chunks) > 1:
            # Multiple slides
            all_content = []
            num_slides = len(resource_chunks)
            for i, resources in enumerate(resource_chunks):
                count = i + 1
                slide_position_str = f' ({count}/{num_slides})'
                lab = label + f'-{count}'
                bt = block_title + slide_position_str
                ft = block_title + slide_position_str
                lab_frame = LabFrame(resources, bt, ft,
                                     label=label,
                                     color='teal')
                all_content.append(lab_frame)
            return all_content
        else:
            return [
                LabFrame(
                    pyexlatex_resources,
                    block_title,
                    frame_title,
                    label=label,
                    color='teal',
                )
            ]

    @property
    def youtube_playlist_description(self) -> str:
        return f'Lecture videos - {self.title}: \n\n{self.description}'

    @property
    def youtube_playlist_title(self) -> str:
        return f'{self.title} - {self.course.title}'

    def update_youtube_playlist(self, existing_playlists: Optional[yt_api.PlaylistListResponse] = None,
                                youtube: Optional = None, print_output: bool = True):
        if youtube is None:
            youtube = yt_api.get_authenticated_service()

        if existing_playlists is None:
            existing_playlists = yt_api.get_all_playlists(youtube=youtube, print_output=print_output)

        try:
            new_playlist = yt_api.add_playlist_if_needed(
                self.youtube_playlist_title,
                self.youtube_playlist_description,
                existing_playlists=existing_playlists,
                youtube=youtube,
                print_output=print_output
            )
            existing_playlists['items'].append(new_playlist)
        except yt_api.YouTubePlaylistExistsException:
            if print_output:
                print(f'Playlist {self.youtube_playlist_title} exists, will not create')

        for i, lect in enumerate(self.lectures):
            try:
                yt_api.add_video_to_playlist_if_needed(
                    lect.youtube_id,
                    self.youtube_playlist_title,
                    i,
                    existing_playlists=existing_playlists,
                    youtube=youtube,
                    print_output=False
                )
                if print_output:
                    print(f'Added lecture {lect.title} to playlist {self.youtube_playlist_title}')
            except yt_api.YouTubeVideoExistsOnPlaylistException:
                if print_output:
                    print(f'Lecture {lect.title} exists on playlist {self.youtube_playlist_title} exists, will not add')
