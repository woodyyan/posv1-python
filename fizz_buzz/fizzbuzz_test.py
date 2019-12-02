import unittest
from fizz_buzz.fizzbuzz import FizzBuzz


class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.fizzbuzz = FizzBuzz()

    def test_should_return_1_when_fizzbuzz_given_1(self):
        result = self.fizzbuzz.say_it(1)
        self.assertEqual(result, '1')

    def test_should_return_fizz_when_fizzbuzz_given_3(self):
        result = self.fizzbuzz.say_it(3)
        self.assertEqual(result, "fizz")

    def test_should_return_buzz_when_fizzbuzz_given_5(self):
        result = self.fizzbuzz.say_it(5)
        self.assertEqual(result, 'buzz')

    def test_should_return_whizz_when_fizzbuzz_given_7(self):
        result = self.fizzbuzz.say_it(7)
        self.assertEqual(result, 'whizz')

    def test_should_return_fizzbuzz_when_fizzbuzz_given_15(self):
        result = self.fizzbuzz.say_it(15)
        self.assertEqual(result, 'fizzbuzz')

    def test_should_return_fizzwhizz_when_fizzbuzz_given_21(self):
        result = self.fizzbuzz.say_it(21)
        self.assertEqual(result, 'fizzwhizz')

    def test_should_return_buzzwhizz_when_fizzbuzz_given_70(self):
        result = self.fizzbuzz.say_it(70)
        self.assertEqual(result, 'buzzwhizz')

    def test_should_return_fizz_when_fizzbuzz_given_13(self):
        result = self.fizzbuzz.say_it(13)
        self.assertEqual(result, 'fizz')


if __name__ == '__main__':
    unittest.main()
