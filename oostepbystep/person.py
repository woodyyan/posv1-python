class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return 'My name is %s. I am %s years old.' % (self.name, self.age)


class Student(Person):
    def __init__(self, name, age, class_number):
        super().__init__(name, age)
        self.class_number = class_number

    def introduce(self):
        return 'My name is %s. I am %s years old. I am a student of class %s. Coding for the glory of HW.' % (self.name, self.age, self.class_number)


class Teacher(Person):
    def introduce(self):
        return 'My name is %s. I am %s years old. Teaching for the future of world.' % (self.name, self.age)
