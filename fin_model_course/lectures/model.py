from dataclasses import dataclass
from typing import Union, Sequence, Type, T, Optional

import pyexlatex as pl


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


@dataclass
class Lecture:
    title: str
    notes: LectureNotes
    youtube_id: Optional[str] = None


@dataclass
class LectureResource:
    name: str
    generated_url: Optional[str] = None
    external_url: Optional[str] = None


@dataclass
class LectureGroup:
    title: str
    description: str
    lectures: Sequence[Lecture]
    resources: Sequence[LectureResource] = tuple()

    def __getitem__(self, item):
        return self.lectures[item]

    def to_models(
            self, top_model: Type[T] = pl.Section, sub_model: Type = pl.UnorderedList
    ) -> T:
        return [mod.notes.to_models(top_model=top_model, sub_model=sub_model) for mod in self]
