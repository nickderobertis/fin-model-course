from typing import Sequence, Optional

from pydantic import BaseModel


class ScheduleProject(BaseModel):
    name: str
    index: int

    @property
    def display_name(self) -> str:
        return f'{self.index}: {self.name}'


class ScheduleLecture(ScheduleProject):
    pass


class ClassContent(BaseModel):
    summary: str
    lectures: Sequence[ScheduleLecture]

    assigned_projects: Optional[Sequence[ScheduleProject]] = None
    projects_due: Optional[Sequence[ScheduleProject]] = None


class CourseSchedule(BaseModel):
    weeks: Sequence[ClassContent]

