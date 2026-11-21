def add(num1: int, num2: int) -> int:
    """Функция берет 2 численных аргумента и складывает их"""
    return num1 + num2

def subtract(num1: int, num2: int) -> int:
    """Функция берет 2 численных аргумента и вычитает второй агрумент из первого"""
    return num1 - num2

class InsufficientFunds(Exception):
    pass

class BankAccount:
    def __init__(self, starting_balance=0):
        self.balance = starting_balance

    def deposit(self, amount):
        if amount < 0:
            raise Exception('can`t deposit a negative number')
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFunds('can`t withdraw more money than user has')
        self.balance -= amount

    def collect_interest(self):
        self.balance = self.balance * 1.1