class FizzBuzz:
    def fizz_buzz(self, word):
        if word % 3 == 0:
            return 'fizz'
        elif word % 5 == 0:
            return 'buzz'
        return word


if __name__ == '__main__':
    fizz_buzz = FizzBuzz()
    for number in range(10):
        word = fizz_buzz.fizz_buzz(number)
        print(word)


def test1():
    return 1
