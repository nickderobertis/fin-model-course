import datetime
from typing import Sequence, Optional, List, Union

import pyexlatex as pl
from pydantic.dataclasses import dataclass

from build_tools.ext_rst import header_rst
from lectures.model import Lecture, LectureNotes, LectureGroup, Serializable
from pltemplates.exercises.lab_exercise import LabExercise


@dataclass
class LabExerciseModel:
    bullet_content: Sequence[Union[str, Serializable, Sequence]]
    answers_content: Sequence[Union[str, Serializable, Sequence]] = tuple()

    @property
    def exercise(self) -> LectureNotes:
        return LectureNotes(self.bullet_content, title='Exercise')

    @property
    def answers(self) -> Optional[LectureNotes]:
        if not self.answers_content:
            return None
        return LectureNotes(self.answers_content, title='Answers')


@dataclass
class LabExerciseLecture(Lecture):
    short_title: Optional[str] = None
    label: Optional[str] = None
    exercises: Sequence[LabExerciseModel] = tuple()

    @classmethod
    def from_seq_of_seq(cls, *args, bullet_content: Sequence[Sequence[str]], answers_content: Sequence[Sequence[str]],
                        **kwargs):
        exercises: List[LabExerciseModel] = []
        for bullets, answers in zip(bullet_content, answers_content):
            le = LabExerciseModel(bullets, answers)
            exercises.append(le)

        return cls(*args, exercises=exercises, **kwargs)

    @property
    def visible_from_week(self) -> int:
        if self.week_covered is None:
            return 1
        return self.week_covered + 1

    @property
    def visible(self) -> bool:
        from schedule.main import get_course_schedule

        schedule = get_course_schedule()
        begin_date, _ = schedule.dates_for_week(self.visible_from_week)
        return datetime.datetime.today().date() > begin_date

    def to_pyexlatex(self) -> LabExercise:
        bullet_contents = []
        answer_contents = []
        for exercise in self.exercises:
            if exercise.exercise:
                bullet_contents.append(exercise.exercise.to_pyexlatex_content())
            else:
                bullet_contents.append([])
            if exercise.answers:
                answer_contents.append(exercise.answers.to_pyexlatex_content())
            else:
                answer_contents.append([])

        resources = [res.to_pyexlatex() for res in self.resources]

        frame_title = self.short_title or self.title
        label = self.label or "labs:" + "-".join(frame_title.casefold().split())
        return LabExercise(
            bullet_contents,
            self.title,
            frame_title,
            label,
            answers_content=answer_contents,
            resources=resources,
        )

    def to_rst(self) -> str:
        if not self.visible:
            return ''

        return self._rst

    @property
    def _rst(self) -> str:
        out_str = header_rst(self.title, 3)
        out_str += self._youtube_rst
        out_str += self._description_rst
        out_str += self._resources_rst
        out_str += self._answers_rst
        return out_str

    @property
    def _description_rst(self) -> str:
        out_str = ''
        if self.exercises is not None:
            num_exercises = len(self.exercises)
            out_str += header_rst('Description', 4)
            for i, exercise in enumerate(self.exercises):
                if num_exercises > 1:
                    out_str += header_rst(f'Level {i + 1}', 5)

                out_str += exercise.exercise.to_rst()
        return out_str

    @property
    def _answers_rst(self) -> str:
        out_str = ''
        exc_with_answers = [exc for exc in self.exercises if exc.answers_content]
        if exc_with_answers:
            num_exercises = len(exc_with_answers)
            out_str += header_rst('Answers', 4)
            for i, exercise in enumerate(self.exercises):
                if not exercise.answers_content:
                    continue
                if num_exercises > 1:
                    out_str += header_rst(f'Level {i + 1}', 5)

                out_str += exercise.answers.to_rst()
        return out_str


class LabExerciseGroup(LectureGroup):
    lectures: Sequence[LabExerciseLecture]
