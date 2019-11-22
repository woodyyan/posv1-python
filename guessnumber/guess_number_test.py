import unittest
from guessnumber.guess_number import GuessNumberGame


class TestGuessNumber(unittest.TestCase):
    def setUp(self):
        self.game = GuessNumberGame()

    def test_should_return_0A0B_given_1234_when_answer_is_5678(self):
        self.game.answer = '5678'
        result = self.game.play('1234')
        self.assertEqual(result, '0A0B')

    def test_should_return_4A0B_given_1234_when_answer_is_1234(self):
        self.game.answer = '1234'
        result = self.game.play('1234')
        self.assertEqual(result, '4A0B')

    def test_should_return_2A2B_given_1234_when_answer_is_1243(self):
        self.game.answer = '1243'
        result = self.game.play('1234')
        self.assertEqual(result, '2A2B')

    def test_should_return_1A1B_given_1234_when_answer_is_1357(self):
        self.game.answer = '1357'
        result = self.game.play('1234')
        self.assertEqual(result, '1A1B')

    def test_should_return_0A4B_given_1234_when_answer_is_4321(self):
        self.game.answer = '4321'
        result = self.game.play('1234')
        self.assertEqual(result, '0A4B')

    def test_should_return_0A1B_given_1234_when_answer_is_5671(self):
        self.game.answer = '1234'
        result = self.game.play('5671')
        self.assertEqual(result, '0A1B')
