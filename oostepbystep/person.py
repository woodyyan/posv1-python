class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return 'My name is %s. I am %s years old.' % (self.name, self.age)
