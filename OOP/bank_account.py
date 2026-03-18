class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Wpłacono {amount}. Obecne saldo: {self.balance}")
        else:
            print("Kwota wpłaty musi być dodatnia.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Brak wystarczających środków. Dostępne saldo: {self.balance}")
        elif amount <= 0:
            print("Kwota wypłaty musi być dodatnia.")
        else:
            self.balance -= amount
            print(f"Wypłacono {amount}. Obecne saldo: {self.balance}")

# Test działania
if __name__ == "__main__":
    acc = BankAccount("Jan Kowalski", 100)
    acc.deposit(50)
    acc.withdraw(200)
    acc.withdraw(80)
