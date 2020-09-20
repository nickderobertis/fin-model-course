import datetime
from typing import Sequence, Optional, Tuple, List, Dict

from pydantic import BaseModel
import pyexlatex as pl
from pyexlatex.models.landscape import Landscape

from lectures.lab_exercise import LabExerciseGroup, LabExerciseLecture
from lectures.model import Lecture, LectureGroup


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
    date_fmt: str = '%m/%d'

    def to_pyexlatex(self, lectures: Dict[str, List[Lecture]], lab_exercises: List[LabExerciseLecture],
                     week_num: int, start_date: datetime.date,
                     end_date: datetime.date, project_date: Optional[datetime.date] = None) -> pl.Section:
        if project_date is None:
            project_date = start_date

        start_fmt = start_date.strftime(self.date_fmt)
        end_fmt = end_date.strftime(self.date_fmt)
        project_fmt = project_date.strftime(self.date_fmt)

        section_contents = []

        if lectures:
            content = []
            for lecture_group_title, lecture_list in lectures.items():
                lecture_contents = pl.UnorderedList([lect.title for lect in lecture_list])
                content.append(pl.UnorderedList([lecture_group_title, lecture_contents]))

            section_contents.append(
                pl.SubSection(
                    content,
                    title='Lectures Covered'
                )
            )

        if self.assigned_projects:
            section_contents.append(
                pl.SubSection(
                    [
                        pl.UnorderedList([proj.display_name for proj in self.assigned_projects])
                    ],
                    title='Projects Assigned'
                )
            )

        if self.projects_due:
            section_contents.append(
                pl.SubSection(
                    [
                        pl.UnorderedList([proj.display_name for proj in self.projects_due])
                    ],
                    title=f'Projects Due by {project_fmt}'
                )
            )

        if lab_exercises:
            section_contents.append(
                pl.SubSection(
                    [
                        pl.UnorderedList([lab.title for lab in lab_exercises])
                    ],
                    title=f'Lab Exercises Due by {end_fmt}'
                )
            )

        date_str = f'{start_fmt} - {end_fmt}'
        section = pl.Section(section_contents, title=f'Week {week_num} ({date_str})')
        return section


class CourseSchedule(BaseModel):
    weeks: Sequence[ClassContent]
    start_date: datetime.date
    end_date: datetime.date
    lab_exercises: LabExerciseGroup
    lectures: Sequence[LectureGroup]
    date_fmt: str = '%m/%d'

    class Config:
        arbitrary_types_allowed = True

    def dates_for_week(self, week_num: int) -> Tuple[datetime.date, datetime.date]:
        begin_date = self.start_date
        for i, content in enumerate(self.weeks):
            if i != len(self.weeks) - 1:
                end_date = begin_date + datetime.timedelta(days=7)
            else:
                end_date = self.end_date
            if i + 1 == week_num:
                return begin_date, end_date
            begin_date = end_date
        raise ValueError(f'invalid week number {week_num}')

    def to_pyexlatex(self) -> list:
        contents = [
            Landscape().wrap(self._pyexlatex_schedule_table),
            self._pyexlatex_by_week_detail,
        ]

        return contents

    @property
    def _pyexlatex_schedule_table(self) -> pl.Tabular:
        table_rows = []
        begin_date = self.start_date
        for i, content in enumerate(self.weeks):
            week_num = i + 1
            if i != len(self.weeks) - 1:
                end_date = begin_date + datetime.timedelta(days=7)
            else:
                end_date = self.end_date
            date_str = f'{begin_date.strftime(self.date_fmt)}-{end_date.strftime(self.date_fmt)}'
            lectures = [item.display_name for item in content.lectures]
            if content.assigned_projects:
                assigned = [item.display_name for item in content.assigned_projects]
            else:
                assigned = []
            if content.projects_due:
                due = [item.display_name for item in content.projects_due]
            else:
                due = []
            max_num_rows = max(len(lectures), len(assigned), len(due))
            num_rows = max(max_num_rows, 1)  # always output at least one row
            for j in range(num_rows):
                if j == 0:
                    row = [f'Week {week_num}', date_str, content.summary]
                else:
                    row = ['', '', '']
                for content_list in [lectures, assigned, due]:
                    try:
                        row_item = content_list[j]
                    except IndexError:
                        row_item = ''
                    row.append(row_item)
                table_rows.append(row)
            table_rows.append(pl.Raw(r'\hline'))
            begin_date = end_date

        values_tables = []
        this_table_rows = []
        for row in table_rows:
            if isinstance(row, pl.Raw):
                values_tables.append(pl.ValuesTable.from_list_of_lists(this_table_rows))
                values_tables.append(row)
                this_table_rows = []
            else:
                this_table_rows.append(row)
        values_tables.pop(-1)  # get rid of final hline

        table = pl.Tabular(
            [

                pl.MultiColumnLabel(pl.Bold('Financial Modeling Schedule'), 6),
                pl.TopRule(),
                pl.ValuesTable.from_list_of_lists([[
                    'Week', 'Dates', 'Topic', 'Lectures', 'Projects Assigned', 'Projects Due'
                ]]),
                pl.MidRule(),
                *values_tables,
                pl.BottomRule(),
            ],
            align='L{1.3cm}lL{5cm}L{9cm}' + 'L{2.5cm}' * 2
        )
        return table

    @property
    def _pyexlatex_by_week_detail(self) -> List[pl.Section]:
        sections = []
        for i, week in enumerate(self.weeks):
            week_num = i + 1
            begin_date, end_date = self.dates_for_week(week_num)
            kwargs = {}
            if i == len(self.weeks) - 1:
                # last week, project should be due at end instead of beginning
                kwargs['project_date'] = end_date
            lab_exercises = self.lab_exercises.lectures_for_week(week_num)
            week_lecture_titles = [lect.name for lect in week.lectures]
            lectures: Dict[str, List[Lecture]] = {}
            for lg in self.lectures:
                if lg.title in week_lecture_titles:
                    lectures[lg.title] = lg.lectures_for_week(week_num)
            sections.append(
                week.to_pyexlatex(lectures, lab_exercises, week_num, begin_date, end_date, **kwargs)
            )
        return sections