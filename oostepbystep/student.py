from oostepbystep.person import Person


class Student(Person):
    def __init__(self, name, age, class_number):
        super().__init__(name, age)
        self.class_number = class_number

    def introduce(self):
        return 'My name is %s. I am %s years old. I am a student of class %s. Coding for the glory of HW.' % (self.name, self.age, self.class_number)
