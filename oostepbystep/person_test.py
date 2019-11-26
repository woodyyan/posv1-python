import unittest

from oostepbystep.person import Person


class TestPerson(unittest.TestCase):
    def test_should_person_have_name_and_age(self):
        person = Person('Tom', '21', 1)
        self.assertEqual(person.id, 1)
        self.assertEqual(person.name, 'Tom')
        self.assertEqual(person.age, '21')

    def test_should_person_have_an_introduce_method_which_introduce_person_with_name_and_age(self):
        tom = Person('Tom', '21', 2)
        introduce = tom.introduce()
        self.assertEqual(introduce, 'My name is Tom. I am 21 years old.')
