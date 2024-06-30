class Teacher:
    def __init__(self, name, education, experience):
        self.__name = name
        self.__education = education
        self.__experience = experience

    def get_teacher_data(self):
        print(f"{self.__name}, {self.__education}, опыт работы {self.__experience}")

    def add_mark(self, student, grade):
        print(f"{self.__name} поставил оценку {grade} студенту {student}")

    def remove_mark(self, student, grade):
        print(f"{self.__name} поставил оценку {grade} студенту {student}")

    def give_a_consultation(self, classroom):
        print(f"{self.__name} провел консультацию в кабинете {classroom}")

    def get_name(self):
        return self.__name

    def get_education(self):
        return self.__education

    def get_experience(self):
        return self.__experience

    def set_experience(self, experience):
        self.__experience = experience


#########################################################################

class DisciplineTeacher(Teacher):
    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
        self.__discipline = discipline
        self.__job_title = job_title

    def get_discipline(self):
        return self.__discipline

    def get_job_title(self):
        return self.__job_title

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def get_teacher_data(self):
        super().get_teacher_data()
        print(f"Предмет: {self.__discipline}, должность {self.__job_title}")

    def add_mark(self, student, grade):
        super().add_mark(student, grade)
        print(f"Предмет: {self.__discipline}")

    def remove_mark(self, student, grade):
        super().remove_mark(student, grade)
        print(f"Предмет: {self.__discipline}")

    def give_a_consultation(self, classroom):
        super().give_a_consultation(classroom)
        print(f"По прeдмету {self.__discipline} как {self.__job_title}")


teacher1 = DisciplineTeacher("Иван Петров", "ДГТУ", "4 года", "Химия", "Директор")
teacher1.get_teacher_data()
teacher1.add_mark("Петр Сидоров", "4")
teacher1.remove_mark("Сергей Иванов", "3")
teacher1.give_a_consultation("9Б")