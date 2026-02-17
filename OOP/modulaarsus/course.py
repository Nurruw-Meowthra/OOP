"""Course module for school information system."""


from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from student import Student


class Course:
    """Represent course with name and student grades."""

    def __init__(self, name: str):
        """
        Initialize the Course object.

        :param name: name of the course
        """
        self.name = name
        self.grades: list[tuple[Student, int]] = []

    def get_grades(self) -> list[tuple[Student, int]]:
        """Return the grades given in this course."""
        return self.grades

    def add_grade(self, student: Student, grade: int):
        """
        Add a grade for a student.

        :param student: Student object
        :param grade: grade as integer
        """
        self.grades.append((student, grade))

    def get_average_grade(self) -> float:
        """
        Calculate and return the average grade of the course.

        :return: average grade or -1.0 if no grades
        """
        if not self.grades:
            return -1.0
        total = sum(grade for _, grade in self.grades)
        return total / len(self.grades)

    def __repr__(self):
        """Return the name of the course."""
        return self.name