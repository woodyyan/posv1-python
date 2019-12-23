import unittest

from oostepbystep.person import Person
from oostepbystep.student import Student
from oostepbystep.teacher import Teacher


class TestPerson(unittest.TestCase):
    def test_should_person_have_name_and_age(self):
        person = Person('Tom', '21')
        self.assertEqual(person.name, 'Tom')
        self.assertEqual(person.age, '21')

    def test_should_person_have_an_introduce_method_which_introduce_person_with_name_and_age(self):
        tom = Person('Tom', '21')
        introduce = tom.introduce()
        self.assertEqual(introduce, 'My name is Tom. I am 21 years old.')

    def test_should_coach_introduce(self):
        tom = Teacher('Tom', '20', 1)
        introduce = tom.introduce()
        self.assertEqual(introduce, 'My name is Tom. I am 20 years old. Teaching for the future of world.')

    def test_should_student_introduce_with_class(self):
        tom = Student('Tom', '20', 2)
        introduce = tom.introduce()
        self.assertEqual(introduce,
                         'My name is Tom. I am 20 years old. I am a student of class 2. Coding for the glory of HW.')
