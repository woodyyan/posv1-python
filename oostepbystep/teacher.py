from oostepbystep.person import Person


class Teacher(Person):
    def __init__(self, name, age, class_numbers):
        super().__init__(name, age)
        self.class_numbers = class_numbers

    def introduce(self):
        return 'My name is %s. I am %s years old. Teaching for the future of world.' % (self.name, self.age)
