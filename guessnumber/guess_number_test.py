import unittest
from guessnumber.guess_number import GuessNumberGame


class TestGuessNumber(unittest.TestCase):
    def test_should_return_0A0B_given_1234_when_answer_is_5678(self):
        game = GuessNumberGame()
        game.answer = '5678'
        result = game.play('1234')
        self.assertEqual(result, '0A0B')

    def test_should_return_4A0B_given_1234_when_answer_is_1234(self):
        game = GuessNumberGame()
        game.answer = '1234'
        result = game.play('1234')
        self.assertEqual(result, '4A0B')
