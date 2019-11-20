class FizzBuzz:
    def fizzBuzz(self, word):
        if word % 3 == 0:
            return 'fizz'
        elif word % 5 == 0:
            return 'buzz'
        return word


if __name__ == '__main__':
    fizzbuzz = FizzBuzz()
    for number in range(10):
        word = fizzbuzz.fizzBuzz(number)
        print(word)


def test1():
    return 1
