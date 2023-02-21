from abc import ABCMeta, abstractmethod


class Sequence(metaclass=ABCMeta):

    @abstractmethod
    def __len__(self):
        """Return the length of the sequence"""

    @abstractmethod
    def __getitem__(self, k):
        """Return the element at list index idx of the sequence"""

    def __contains__(self, item):
        for j in range(len(self)):
            if self[j] == item:
                return True
        return False

    def index(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return val
        raise ValueError("Value not in sequence")

    def count(self, val):
        _count = 0
        for k in range(len(self)):
            if self[k] == val:
                _count += 1
        return _count

    def __eq__(self, other):
        if not isinstance(other, Sequence | range):
            raise AssertionError("Can only compare to sequence | range types")
        if len(other) != len(self):
            return False
        for i, k in enumerate(other):
            if self[i] != k:
                return False
        return True

    def __lt__(self, other):
        if not isinstance(other, Sequence | range):
            raise AssertionError("Can only compare to sequence | range types")
        i = 0
        while i < len(other) and i < len(self):
            if self[i] != other[i]:
                if self[i] < other[i]:
                    return True
                else:
                    return False
            i += 1
        return False


class Range(Sequence):

    def __init__(self, start, stop=None, step=1):

        if step == 0:
            raise ValueError("Step size cannot be zero")

        if stop is None:
            start, stop = 0, start
        self._start, self._stop = start, stop
        self._step = step
        self._length = max(0, (stop - start + step - 1) // step)

    def __len__(self):
        return self._length

    def __getitem__(self, k):
        if k < 0:
            k += len(self)

        if not 0 <= k <= len(self):
            raise IndexError("Index out of bound")

        return self._start + k * self._step

    def __contains__(self, item):
        if self._start <= item < self._stop:
            if (item - self._start) % self._step == 0:
                return True
        return False


start, stop, step = 10, 100, 2
custom_range = Range(start, stop, step)
idx = 8
element = start + idx * step
print(f"Accessing element {idx} should return {element}: {custom_range[idx]}")
print(f"seq == seq should return True: {custom_range == custom_range}")
print(f"seq == range_eq should return True: {custom_range == range(start, stop, step)}")
print(f"seq == range_neq should return False: {custom_range == range(start, stop+step, step)}")
print(f"seq < greater_range should return True: {custom_range < range(10, 30, 3)}")
print(f"seq < smaller_range should return False: {custom_range < range(9, 30, 3)}")
print(f"start in seq should be True: {start in custom_range}")
print(f"stop in seq should be False: {stop in custom_range}")
print(f"start + 3 * step in seq should be True: {start + 3 * step in custom_range}")
print(f"start + 3 * step + 1 in seq should be {step == 1}: {start + 3 * step + 1 in custom_range}")
