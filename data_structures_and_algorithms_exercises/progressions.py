class Progression:

    def __init__(self, start):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))


class FibonacciProgression(Progression):

    def __init__(self, first_number, second_number):
        super().__init__(first_number)
        self._previous = second_number - first_number

    def _advance(self):
        self._previous, self._current = self._current, self._previous + self._current


test = FibonacciProgression(2, 2)
test.print_progression(10)