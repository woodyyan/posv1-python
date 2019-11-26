import unittest

from oostepbystep.person import Person, Student, Coach


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

    def test_should_student_introduce(self):
        tom = Student('Tom', '18', 1)
        introduce = tom.introduce()
        self.assertEqual(introduce, 'My name is Tom. I am 18 years old. Coding for the glory of HW.')

    def test_should_coach_introduce(self):
        tom = Coach('Tom', '20', 1)
        introduce = tom.introduce()
        self.assertEqual(introduce, 'My name is Tom. I am 20 years old. Teaching for the future of world.')
