class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
            self.balance = self.balance + amount
            print(f"Deposit of {amount} made. New balance is {self.balance}")

    def withdraw(self, amount):
            if amount <= self.balance:
                self.balance = self.balance - amount
                print(f"Withdrawal of {amount} made. New balance is {self.balance}")
            else:
                print("Insufficient funds")

            

class SavingAccount(BankAccount):
      def __init__(self, owner, balance, rate):
        super().__init__(owner, balance)
        self.rate = rate

      def add_interest(self):
        interest = self.balance * self.rate
        self.balance = self.balance + interest
        print(f"Interest of {interest} added. New balance is {self.balance}")

s = SavingAccount("nikita", 1000, 0.10)
s.deposit(500)
s.add_interest()
s.withdraw(2000)
# acc = BankAccount("Nikita", 1000)
# acc.deposit(5000)
# acc.withdraw(1300)
# acc.withdraw(200)


class Cat:
      def __init__(self, name):
          self.name = name

      def meow(self):
          print(f"{self.name} says Meow")

c = Cat("Tom")
c.meow()
