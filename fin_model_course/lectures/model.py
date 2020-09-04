import datetime
from dataclasses import dataclass
from typing import Union, Sequence, Type, Optional, TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from models.content import ContentMetadata

import pyexlatex as pl


T = TypeVar("T")


@dataclass
class LectureNotes:
    items: Sequence[Union[str, "LectureNotes"]]
    title: str

    def __getitem__(self, item):
        return self.items[item]

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

        return top_model(final_items, title=self.title)

    def to_rst(self) -> str:
        return "\n" + "\n".join([f"- {note}" for note in self]) + "\n"


@dataclass
class LectureResource:
    name: str
    static_url: Optional[str] = None
    external_url: Optional[str] = None
    updated: Optional[datetime.datetime] = None
    index: Optional[int] = None
    datetime_fmt: str = "%B%e, %l:%M %p"

    @classmethod
    def from_metadata(cls, md: "ContentMetadata", url: Optional[str] = None) -> "LectureResource":
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
    def display_name(self) -> str:
        name = ""
        if self.index is not None:
            name += f"{self.index} "
        name += self.name
        if self.updated is not None:
            name += f" (updated {self.updated.strftime(self.datetime_fmt)})"
        return name

    def to_rst(self) -> str:
        return f"""
- :download:`{self.display_name} <{self.url}>`
        """


@dataclass
class Lecture:
    title: str
    notes: LectureNotes
    youtube_id: Optional[str] = None

    def to_rst(self) -> str:
        out_str = f"""
{self.title}
============================================================================================================
        """
        if self.youtube_id is not None:
            out_str += f"""
.. youtube:: {self.youtube_id}
    :height: 315
    :width: 560
    :align: center

|
"""
        out_str += self.notes.to_rst()
        return out_str

@dataclass
class LectureGroup:
    title: str
    description: str
    lectures: Sequence[Lecture]
    resources: Sequence[LectureResource] = tuple()

    def __getitem__(self, item):
        return self.lectures[item]

    @property
    def stub(self) -> str:
        lower = self.title.casefold()
        parts = lower.split()
        return "-".join(parts)

    def to_models(
        self, top_model: Type[T] = pl.Section, sub_model: Type = pl.UnorderedList
    ) -> T:
        return [
            mod.notes.to_models(top_model=top_model, sub_model=sub_model)
            for mod in self
        ]

    def to_rst(self) -> str:
        out_str = f"""
{self.title}
*************************************************************************************************************

{self.description}
        """
        if self.resources:
            out_str += (
                f"""
Resources
=================
            """
                + "\n"
                + "\n".join([res.to_rst() for res in self.resources])
                + "\n"
            )
        for lecture in self:
            out_str += lecture.to_rst()
        return out_str
