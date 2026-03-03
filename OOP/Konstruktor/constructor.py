"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

    pass


class Person:
    """Represent person with firstname, lastname and age."""

    firstname = ""
    lastname = ""
    age = 0


class Student:
    """Represent student with firstname, lastname and age."""

    def __init__(self, firstname, lastname, age):
        """CAT EATER...."""
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


if __name__ == '__main__':
    # empty usage
    me = Empty()
    # 3 x person usage
    esi = Person()
    esi.firstname = "Matt"
    esi.lastname = "Laud"
    esi.age = "645"

    viima = Person()
    viima.firstname = "Sibul"
    viima.lastname = "Kivi"
    viima.age = "120"

    vana = Person()
    vana.firstname = "Kaaan"
    vana.lastname = "Ahv"
    vana.age = "4864"
    # 3 x student usage
    kana = Student("Broiler", "Filee", "0.5")
    salmon = Student("Sushi", "Calamari", "10")
    beef = Student("Bone-in", "Ribeye", "50")