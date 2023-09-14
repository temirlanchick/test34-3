class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        amount = float(input("Введите сумму для пополнения счета: "))
        self._balance += amount

    def _kill(self):
        self._balance = 0


    def _jeckpot(self):
        self._balance *= 10

    def _merge_balance(self, other_bank):
        self._balance += other_bank._balance
        other_bank._balance = 0

    def get_balance(self):
        return self._balance



class Calculator:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        return Calculator(self.value + other.value)

    def __sub__(self, other):
        return Calculator(self.value - other.value)

    def __mul__(self, other):
        return Calculator(self.value * other.value)

    def __truediv__(self, other):
        if other.value == 0:
            raise ValueError("Division by zero is not allowed")
        return Calculator(self.value / other.value)

    def __str__(self):
        return str(self.value)




bank1 = Bank("Клиент 1", 100)
bank2 = Bank("Клиент 2", 100)

print(f"Баланс клиента 1: {bank1.get_balance()}")
print(f"Баланс клиента 2: {bank2.get_balance()}")

bank1._merge_balance(bank2)
print(f"Баланс клиента 1 после объединения: {bank1.get_balance()}")
print(f"Баланс клиента 2 после объединения: {bank2.get_balance()}")


calc1 = Calculator(10)
calc2 = Calculator(5)

result_add = calc1 + calc2
result_sub = calc1 - calc2
result_mul = calc1 * calc2
result_div = calc1 / calc2

print(f"Результат сложения: {result_add}")
print(f"Результат вычитания: {result_sub}")
print(f"Результат умножения: {result_mul}")
print(f"Результат деления: {result_div}")