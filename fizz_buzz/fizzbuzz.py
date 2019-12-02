class FizzBuzz:
    def say_it(self, word):
        result = ''

        if '3' in str(word):
            return 'fizz'

        if word % 3 == 0:
            result += 'fizz'
        if word % 5 == 0:
            result += 'buzz'
        if word % 7 == 0:
            result += 'whizz'

        if result:
            return result
        return str(word)


if __name__ == '__main__':
    fizz_buzz = FizzBuzz()
    for number in range(1, 16):
        print(fizz_buzz.say_it(number))
