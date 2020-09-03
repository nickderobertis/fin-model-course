from typing import Sequence, Optional

from pydantic import BaseModel


class ClassContent(BaseModel):
    summary: str
    lectures: Sequence[int]

    assigned_projects: Optional[Sequence[int]] = None
    projects_due: Optional[Sequence[int]] = None


class CourseSchedule(BaseModel):
    weeks: Sequence[ClassContent]

