from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str, yob: int):
        self.__name = name
        self.__yob = yob

    @abstractmethod
    def describe(self):
        """Print all the information of the subject
        """
        class_name = self.__class__.__name__
        print(
            f'{class_name} - Name: {self.__name} - YoB: {self.__yob}', end="")

    # yob getter method
    def get_yob(self):
        return self.__yob

    def set_yob(self, yob):
        self.__yob = yob


class Student(Person):
    def __init__(self, name: str, yob: int, grade: int):
        super().__init__(name=name, yob=yob)
        self.__grade = grade

    def describe(self):
        """Print the information of the student
        """
        # print(f'{__name__}')
        super().describe()
        print(f' - Grade: {self.__grade}')


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name=name, yob=yob)
        self.__subject = subject

    def describe(self):
        """Print the information of the teacher
        """
        super().describe()
        print(f' - Subject: {self.__subject}')


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name=name, yob=yob)
        self.__specialist = specialist

    def describe(self):
        """Print the information of the doctor
        """
        super().describe()
        print(f' - Specialist: {self.__specialist}')


class Ward:
    __people = []
    __size = 0

    def __init__(self, name: str):
        self.__name = name

    def add_person(self, person: Person):
        """Add person to the current ward

        Args:
            person (Person): the person to be add to the ward
            can be either Student, Teacher, Doctor
        """
        self.__people.append(person)
        self.__size += 1

    def describe(self):
        """print the information about the ward
        """
        print(f'Ward Name: {self.__name}')
        for i in range(self.__size):
            self.__people[i].describe()

    def count_doctor(self) -> int:
        """count the total number of doctors
        Returns: 
            int: the total number of doctors in the ward
        """
        total_doctor: int = 0
        for i in range(self.__size):
            if (self.__people[i].__class__.__name__ == 'Doctor'):
                total_doctor += 1
        return total_doctor

    def sort_age(self):
        """Sort the list of citizens by age
        """
        self.__people.sort(key=lambda x: (2024 - x.get_yob()))

    def compute_average(self):
        """Get the average yob of teachers in the ward 
        """
        total_yob: int = 0
        total_teachers: int = 0
        for i in range(self.__size):
            if (self.__people[i].__class__.__name__ == 'Teacher'):
                total_yob += self.__people[i].get_yob()
                total_teachers += 1

        average_yob = total_yob / total_teachers
        return round(average_yob, ndigits=2)


def main():
    # 1
    student1 = Student(name='studentA', yob=2010, grade="7")
    teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
    doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
    teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
    doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
    ward1 = Ward(name="Ward1")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    ward1.describe()

    # 2
    print(f'\nNumber of doctors: {ward1.count_doctor()}')

    # 3
    print("\nAfter sorting Age of Ward1 people")
    ward1.sort_age()
    ward1.describe()

    # 4
    print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")


if __name__ == '__main__':
    main()
