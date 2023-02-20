class Flower:

    def __init__(self, name: str, number_of_petals: int, price: float):
        self._name = name
        self._number_of_petals = number_of_petals
        self._price = price

    def set_price(self, new_price: float):
        self._price = new_price

    def get_price(self) -> float:
        return self._price


rose = Flower("rose", 10, 1.5)

print(rose.get_price())
rose.set_price(1.75)
print(rose.get_price())
