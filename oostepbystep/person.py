class Person:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def introduce(self):
        return 'My name is %s. I am %s years old.' % (self.name, self.age)
