"""1234..........."""
from student import Student
from course import Course


class School:
    """1234....."""

    def __init__(self, name: str):
        """1234."""
        self.name = name
        self.students: list[Student] = []
        self.courses: list[Course] = []

    def add_course(self, course: Course):
        """1234."""
        if course not in self.courses:
            self.courses.append(course)

    def add_student(self, student: Student):
        """1234..."""
        if student not in self.students:
            # Määrame õpilasele ID lisamise hetkel
            student.set_id(len(self.students) + 1)
            self.students.append(student)

    def add_student_grade(self, student: Student, course: Course, grade: int):
        """1234.."""
        # Kontroll, kas mõlemad on koolis olemas
        if student in self.students and course in self.courses:
            student.add_grade(course, grade)
            course.add_grade(student, grade)

    def get_students(self) -> list[Student]:
        """1234.."""
        return self.students

    def get_courses(self) -> list[Course]:
        """1234.."""
        return self.courses

    def get_students_ordered_by_average_grade(self) -> list[Student]:
        """1234...."""
        return sorted(self.students, key=lambda s: s.get_average_grade(), reverse=True)