class FizzBuzz:
    def say_it(self, word):
        if word % 3 == 0 and word % 5 == 0:
            return 'fizzbuzz'
        if word % 3 == 0:
            return 'fizz'
        elif word % 5 == 0:
            return 'buzz'
        return word


if __name__ == '__main__':
    fizz_buzz = FizzBuzz()
    for number in range(1, 16):
        print(fizz_buzz.say_it(number))
