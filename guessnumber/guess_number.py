class GuessNumberGame:
    def __init__(self, answer=None):
        self.answer = answer

    def play(self, numbers):
        player_numbers = list(numbers)
        answer_numbers = list(self.answer)
        allCorrectCount = 0
        numbersCorrectCount = 0
        for number in player_numbers:
            if number in answer_numbers:
                if answer_numbers.index(number) == player_numbers.index(number):
                    allCorrectCount += 1
                else:
                    numbersCorrectCount += 1
        return '%sA%sB' % (allCorrectCount, numbersCorrectCount)
