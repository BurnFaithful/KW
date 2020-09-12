# 멤버변수[속성] private형 _name, id
# getter[멤버변수값 => 외부] : _name, id
# setter[멤버변수값 <= 외부] : _name


class Student:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def __str__(self):
        return self.__name + ', ' + str(self.__id)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

student = Student("Youngmin", 10)
student.id = 20
print(student.id)
print(student)