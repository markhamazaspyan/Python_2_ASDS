from abc import ABC, abstractmethod

"""
You know that each BankAccount object has attributes id, balance and rate. Use builder pattern
and any extra classes and methods that you may need to realize the creation of a BankAccount type
object. Create some objects and do some operations to test your classes.
"""


class Builder(ABC):

    @abstractmethod
    def create_id(self):
        pass

    @abstractmethod
    def create_balance(self):
        pass

    @abstractmethod
    def create_rate(self):
        pass


class ConcreteBuilder(Builder):

    def __init__(self):
        self.account = Account()


    def create_id(self, _id):
        self.account.add_id(_id)

    def create_balance(self, _balance):
        self.account.add_balance(_balance)

    def create_rate(self, _rate):
        self.account.add_rate(_rate)


class Account:

    def __init__(self):
        self.id = []
        self.rate = []
        self.balance = []

    def add_id(self, desc_id):
        self.id.append(desc_id)

    def add_balance(self, desc_b):
        self.rate.append(desc_b)

    def add_rate(self, desc_r):
        self.balance.append(desc_r)

    def describe_accounts(self):
        print(f"Id: {self.id} \nRate: {self.rate} \nBalance: {self.balance}")



if __name__ == "__main__":
    builder = ConcreteBuilder()

    builder.create_id(101)
    builder.create_balance(1000)
    builder.create_rate(2001)

    builder.account.describe_accounts()