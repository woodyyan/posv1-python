import unittest
from unittest import mock
from guessnumber.guess_number import GuessNumberGame, AnswerGenerator


class TestGuessNumber(unittest.TestCase):
    def setUp(self):
        self.game = GuessNumberGame(StubAnswerGenerator())

    def test_should_return_0A0B_given_5678_when_answer_is_1234(self):
        result = self.game.guess('5678')
        self.assertEqual(result, '0A0B')

    def test_should_return_4A0B_given_1234_when_answer_is_1234(self):
        result = self.game.guess('1234')
        self.assertEqual(result, '4A0B')

    def test_should_return_2A2B_given_1243_when_answer_is_1234(self):
        result = self.game.guess('1243')
        self.assertEqual(result, '2A2B')

    def test_should_return_1A1B_given_1357_when_answer_is_1234(self):
        result = self.game.guess('1357')
        self.assertEqual(result, '1A1B')

    def test_should_return_0A4B_given_4321_when_answer_is_1234(self):
        result = self.game.guess('4321')
        self.assertEqual(result, '0A4B')

    def test_should_return_0A1B_given_1234_when_answer_is_5671(self):
        result = self.game.guess('5671')
        self.assertEqual(result, '0A1B')

    def test_should_return_4_digits_when_generate_answer(self):
        answerGenerator = AnswerGenerator()
        answer = answerGenerator.generate()
        self.assertEqual(len(answer), 4)

    def test_should_return_numbers_when_generate_answer(self):
        answerGenerator = AnswerGenerator()
        answer = answerGenerator.generate()
        self.assertTrue(answer.isdigit())

    def test_should_return_unique_numbers_when_generate_answer(self):
        answerGenerator = AnswerGenerator()
        answer = answerGenerator.generate()
        self.assertEqual(len(set(answer)), 4)

    def test_should_return_4A0B_given_1234_when_answer_is_1234_with_stub(self):
        generator = StubAnswerGenerator()
        game = GuessNumberGame(generator)
        result = game.guess('1234')
        self.assertEqual(result, '4A0B')

    def test_should_return_4A0B_given_1234_when_answer_is_1234_with_mock(self):
        generator = AnswerGenerator()
        generator.generate = mock.Mock(return_value='1234')
        game = GuessNumberGame(generator)
        result = game.guess('1234')
        self.assertEqual(result, '4A0B')


class StubAnswerGenerator(AnswerGenerator):
    def generate(self):
        return '1234'
