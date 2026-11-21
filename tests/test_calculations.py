from server.calculations import add, subtract, BankAccount
import pytest

@pytest.fixture
def zero_bank_account():
    """Создание объекта для тестирования"""
    print('creating new bank account')
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(100)

@pytest.mark.parametrize('num1, num2, expected_value', [
    (3, 2, 5),
    (5, 8, 13),
    (13, 16, 29)
])
def test_add(num1, num2, expected_value):
    """Тестирование с несколькими параметрами"""
    assert add(num1, num2) == expected_value

def test_subtract():
    print('testing subtract function')
    assert subtract(9, 4) == 5

def test_bank_set_initial_amount():
    bank_account = BankAccount(100)
    assert bank_account.balance == 100

def test_bank_default_amount(zero_bank_account):
    print('testing my bank account')
    assert zero_bank_account.balance == 0

def test_bank_withdraw(bank_account):
    bank_account.withdraw(30)
    assert bank_account.balance == 70

def test_bank_withdraw(bank_account):
    bank_account.deposit(30)
    assert bank_account.balance == 130

def test_bank_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance, 3) == 110

@pytest.mark.parametrize('deposit, withdraw, result', [
    (200, 100, 100),
    (1000, 1, 999),
    (76341223, 70.9, 76341152.1)
])
def test_bank_transaction(zero_bank_account, deposit, withdraw, result):
    zero_bank_account.deposit(deposit)
    zero_bank_account.withdraw(withdraw)
    assert zero_bank_account.balance == result

def test_unsufficient_funds(zero_bank_account):
    """Тест проверяющий выход ошибок"""
    with pytest.raises(Exception):
        zero_bank_account.withdraw(1000)