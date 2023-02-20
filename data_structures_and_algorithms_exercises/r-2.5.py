class CreditCard:

    def __init__(self, customer: str, bank: str, account: str, limit: float, initial_balance=0.):
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = initial_balance

    def get_balance(self) -> float:
        return self._balance

    def charge(self, price) -> bool:
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount: float):
        assert type(amount) in [float, int]
        if amount < 0:
            raise ValueError("Negative payment is not possible")
        self._balance -= amount


test = CreditCard('test', 'bank', 'account', 1000, 1000)
test.make_payment(100)
test.make_payment(100.)
print(test.get_balance())
