import unittest
from guess_number import GuessNumberGame


class TestGuessNumber(unittest.TestCase):
    def test_should_return_0A0B_given_1234_when_answer_is_5678(self):
        game = GuessNumberGame()
        result = game.play('1234')
        self.assertEqual(result, '0A0B')
