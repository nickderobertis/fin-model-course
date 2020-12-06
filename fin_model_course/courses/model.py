from enum import Enum
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from lectures.model import LectureGroup

from pydantic import BaseModel


class CourseSelectors(str, Enum):
    BASIC = 'Financial Modeling with Python and Excel'
    ADVANCED = 'Advanced Financial Modeling with Python'


class CourseModel(BaseModel):
    title: str
    order: int
    stub: str = ''

    @property
    def lecture_groups(self) -> List['LectureGroup']:
        from lectures.config import get_lecture_groups
        lgs = get_lecture_groups()
        return [lg for lg in lgs if lg.course == self]
