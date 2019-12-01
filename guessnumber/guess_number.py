import random

ANSWER_FORMAT = '%sA%sB'
CORRECT_ANSWER_FORMAT = '4A0B'


def get_player_answer():
    answer = input('请输入你的数字：')
#     TODO: verify input
    return answer


class GuessNumberGame:
    ROUND_COUNT = 6
    __answer = ''

    def __init__(self, answer_generator):
        self.__answer = answer_generator.generate()

    def guess(self, numbers):
        player_numbers = list(numbers)
        answer_numbers = list(self.__answer)
        allCorrectCount = 0
        numbersCorrectCount = 0
        for number in player_numbers:
            if number in answer_numbers:
                if answer_numbers.index(number) == player_numbers.index(number):
                    allCorrectCount += 1
                else:
                    numbersCorrectCount += 1
        return ANSWER_FORMAT % (allCorrectCount, numbersCorrectCount)

    def play(self):
        isSuccess = False
        for index in range(GuessNumberGame.ROUND_COUNT):
            answer = self.guess(get_player_answer())
            if answer == CORRECT_ANSWER_FORMAT:
                isSuccess = True
                break
            else:
                print(answer)
        print('Game Over! You Win!' if isSuccess else 'Game Over! You Lose! Answer is %s' % self.__answer)


class AnswerGenerator:
    def generate(self):
        answer = set()
        while len(answer) < 4:
            answer.add(str(random.randint(0, 9)))
        return ''.join(answer)


if __name__ == '__main__':
    game = GuessNumberGame(AnswerGenerator())
    game.play()
