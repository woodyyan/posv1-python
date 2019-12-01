import unittest
from fizz_buzz.fizzbuzz import FizzBuzz
from fizz_buzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.fizzbuzz = FizzBuzz()

    def test_should_return_1_when_fizzbuzz_given_1(self):
        word = 1
        result = self.fizzbuzz.say_it(word)
        self.assertEqual(result, word)

    def test_should_return_fizz_when_fizzbuzz_given_3(self):
        word = 3
        result = self.fizzbuzz.say_it(word)
        self.assertEqual(result, "fizz")

    def test_should_return_buzz_when_fizzbuzz_given_5(self):
        word = 5
        result = self.fizzbuzz.say_it(word)
        self.assertEqual(result, 'buzz')


if __name__ == '__main__':
    unittest.main()
