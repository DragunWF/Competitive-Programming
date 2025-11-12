# https://www.codewars.com/kata/5a03af9606d5b65ff7000009/train/python

class User:
    def __init__(self, name: str, balance: int, checking_account: bool):
        # the account holder's name
        self.name = name
        # the initial balance
        self.balance = balance
        # whether this user can issue checks to others
        self.checking_account = checking_account

    def withdraw(self, amount: float) -> str:
        """Withdraw `amount` from this account, if balance is sufficient"""
        if amount > self.balance:
            raise ValueError("There is imbalance with the force, Jedi")
        self.balance -= amount
        return f"{self.name} has {self.balance}."

    def add_cash(self, amount: float) -> str:
        """Deposit `amount` into this account"""
        self.balance += amount
        return f"{self.name} has {self.balance}."

    def get_status(self) -> str:
        return f"{self.name} has {self.balance}"

    def check(self, issuer, amount: float):
        """Receive a check from `issuer` over `amount`, if possible

        `issuer` is the User issuing the check, i.e. the account the `amount` will be taken from
        `self` is the User receiving the check, i.e. the account the `amount` will be added to
        """
        if not issuer.checking_account:
            raise ValueError(
                "Issuer is not worthy enough... Come back in a 100 years"
            )
        issuer.withdraw(amount)
        self.add_cash(amount)
        return f"{self.get_status()} and {issuer.get_status()}."
