from datetime import datetime


class Client:
    def __init__(self, name: str):
        self._name = name
        self._accounts = []

    @property
    def accounts(self):
        return self._accounts

    def create_account(self, account_name: str, account_type: str = 'main', balance: float = 0.0):
        if account_type == 'save':
            self._accounts.append(SaveAccount(account_name))
        elif account_type == 'credit':
            self._accounts.append(CreditAccount(account_name))
        else:
            self._accounts.append(Account(account_name, account_type, balance))
        return self._accounts[-1]


class Account:
    def __init__(self, account_name: str, account_type: str, balance: float):
        self._account_name = account_name
        self._account_type = account_type
        self._balance = balance
        self._transactions = []

    def withdraw(self, money: float):
        if self._balance >= money:
            self._balance -= money
            self._transactions.append(Transaction(money, 'withdraw'))
            print(f'Со счета снято {money}')
        else:
            print('Недостаточно денег для снятия')

    def deposit(self, money: float):
        self._balance += money
        self._transactions.append(Transaction(money, 'deposit'))
        print(f'Счет пополнен на {money}')

    @property
    def balance(self):
        return self._balance

    def show_transactions(self):
        if self._transactions:
            print(f'Транзакции для счета: {self._account_name}')
            for transaction in self._transactions:
                print(transaction)
        else:
            print('Транзакций для выбранного счета нет')

    def __str__(self):
        return f'Название счета: {self._account_name}, Тип счета: {self._account_type}, Баланс: {self.balance} '


class SaveAccount(Account):
    def __init__(self, account_name):
        super().__init__(account_name=account_name, account_type='save', balance=0)
        self._rate = 0.05

    def add_rate(self):
        new_rate = self._balance * self._rate
        self._balance += new_rate
        self._transactions.append(Transaction(new_rate, operation_type='interest'))
        print(f'Начисление за сбережение средств: {new_rate}')


class CreditAccount(Account):
    def __init__(self, account_name):
        self._limit = 10000
        self._rate = 0.01
        super().__init__(account_name=account_name, account_type='credit', balance=-self._limit)

    def charge_rate(self):
        interest = self._balance * self._rate
        self._balance += interest
        self._transactions.append(Transaction(interest, "interest"))
        print(f"Удержание за использования кредитных средств: {interest}")

    def withdraw(self, money):
        total_withdraw = money + abs(self._balance)
        if total_withdraw <= self._limit:
            super().withdraw(money)
        else:
            print(f'Лимит кредитного счета превышен')


class Transaction:
    def __init__(self, amount: float, operation_type: str):
        self._amount = amount
        self._date = datetime.now()
        self._operation_type = operation_type

    def __str__(self):
        return f'Тип транзакции: {self._operation_type}, Дата: {self._date}, Сумма транзакции: {self._amount}'


client = Client('Test CLient')

save_account = client.create_account('save_account', 'save')
save_account.deposit(5.0)
save_account.withdraw(4.0)
save_account.add_rate()

main_account = client.create_account('main_account')
main_account.deposit(200.0)

credit_account = client.create_account('credit_account', 'credit')
credit_account.charge_rate()

for account in client.accounts:
    account.show_transactions()
