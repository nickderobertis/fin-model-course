import datetime
from typing import Sequence, Optional

from pydantic import BaseModel
import pyexlatex as pl


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
    start_date: datetime.date
    end_date: datetime.date
    date_fmt: str = '%m/%d'

    def to_pyexlatex(self):
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
