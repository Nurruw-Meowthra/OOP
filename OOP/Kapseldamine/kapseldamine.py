"""Encapsulation exercise."""


class Student:
    """Represent student with name, id and status."""

    def __init__(self, name, student_id, status="Active"):
        """fish..."""
        self.__name = name
        self.__student_id = student_id
        # Use the setter here to ensure the initial status is also validated
        self.set_status(status)

    def get_name(self):
        """Return the name of the student."""
        return self.__name

    def set_name(self, name):
        """Set the name of the student."""
        self.__name = name

    def get_id(self):
        """Return the student ID."""
        return self.__student_id

    def get_status(self):
        """Return the status of the student."""
        return self.__status

    def set_status(self, status):
        """Set the status of the student only if it is valid."""
        # Define the allowed values
        valid_statuses = ["Active", "Expelled", "Finished", "Inactive"]
        # Only update if the status is in our list
        if status in valid_statuses:
            self.__status = status
        # If invalid, we do nothing, so the old status is preserved




if __name__ == "__main__":
    student = Student("Alice", 12345)
    kana = Student("Broiler", 13255)
    salmon = Student("Sushi", 99887)
    beef = Student("Bone-in", 77665)
    print(student.get_name())      # Alice
    print(student.get_id())        # 12345
    student.set_status("Active")
    print(student.get_status())    # Active
    kana.set_status("Expelled")
    print(kana.get_status())       # Expelled
    salmon.set_status("Sleeping")
    print(salmon.get_status())     # Inactive
    beef.set_status("Finished")
    print(beef.get_status())       # Finished