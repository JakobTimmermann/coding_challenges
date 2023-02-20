class Vector:

    def __init__(self, input_info: int | list):
        if type(input_info) == int:
            self.array = [0] * input_info
        elif type(input_info) == list:
            self.array = input_info
        else:
            raise ValueError("Initialization either with length (int) or vector (list)")

    def __len__(self) -> int:
        return len(self.array)

    def __getitem__(self, i: int) -> int | float:
        return self.array[i]

    def __setitem__(self, i: int, value: int | float):
        self.array[i] = value

    def __add__(self, other) -> object:
        if len(other) != len(self.array):
            raise ValueError("Different length array")
        output = Vector(len(other))
        for idx, n1, n2 in zip(range(len(other)), self.array, other):
            output[idx] = n1 + n2
        return output

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if len(other) != len(self.array):
            raise ValueError("Different length array")
        output = Vector(len(other))
        for idx, n1, n2 in zip(range(len(other)), self.array, other):
            output[idx] = n1 - n2
        return output

    def __rsub__(self, other):
        return self.__sub__(other)

    def __str__(self):
        return f"[{', '.join([str(number) for number in self.array])}]"

    def __neg__(self):
        output = Vector(len(self.array))
        for idx, number in enumerate(self.array):
            output[idx] = -number
        return output

    def __mul__(self, multiplier):
        if type(multiplier) in [float, int]:
            output = Vector(len(self.array))
            for idx, number in enumerate(self.array):
                output[idx] = multiplier * number
            return output
        elif isinstance(multiplier, Vector):
            if len(multiplier) != len(self.array):
                raise ValueError("Different length array")
            scalar_product = 0
            for idx in range(len(multiplier)):
                scalar_product += multiplier[idx] * self.array[idx]
            return scalar_product

    def __rmul__(self, other):
        return self.__mul__(other)


if __name__ == "__main__":
    v = Vector(8)
    for k in range(8):
        v[k] = 3 * k**2 - 5*k
    print(v)
    x = [1, 2, 3, 4, 5, 6, 7, 8] - v
    print(x)
    print(Vector([1, 1, 1, 0, 2, 0, 0, 0])*x)
    print(-x)
