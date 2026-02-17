"""Student module for school information system."""


from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from course import Course


class Student:
    """Represent student with name, id and grades."""

    def __init__(self, name: str):
        """
        Initialize the Student object.

        :param name: name of the student
        """
        self.name = name
        self.grades: list[tuple[Course, int]] = []
        self.id = None

    def set_id(self, student_id: int):
        """
        Set unique identifier for the student.

        :param student_id: unique ID to be assigned
        """
        if self.id is None:
            self.id = student_id

    def get_id(self) -> int:
        """Return the student ID."""
        return self.id

    def get_grades(self) -> list[tuple[Course, int]]:
        """Return the student's grades."""
        return self.grades

    def add_grade(self, course: Course, grade: int):
        """
        Add a grade for a specific course.

        :param course: Course object
        :param grade: grade as integer
        """
        self.grades.append((course, grade))

    def get_average_grade(self) -> float:
        """
        Calculate and return the average grade.

        :return: average grade or -1.0 if no grades
        """
        if not self.grades:
            return -1.0
        total = sum(grade for _, grade in self.grades)
        return total / len(self.grades)

    def __repr__(self) -> str:
        """Return the name of the student."""
        return self.name