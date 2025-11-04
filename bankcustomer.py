class Account:
    def _init_(self, name, balance):
        self._name = name
        self._balance = balance
        self._active = True
        self._atm_requested = False
        self._cheque_requested = False
    def __is_active(self):
        return self._active

    def check_balance(self):
        if not self.__is_active():
            print(" Account inactive.")
        else:
            print(f" Balance for {self._name}: ₹{self._balance}")
    def deposit(self, amount):
        if amount <= 0:
            print(" Invalid deposit amount.")
        else:
            self._balance += amount
            print(f" Deposited ₹{amount}. New balance: ₹{self._balance}")

    def freeze_account(self):
        if not self._active:
            print(" Account already frozen.")
        else:
            self._active = False
            print("Account frozen successfully.")

    def unfreeze_account(self):
        if self._active:
            print("⚠ Account already active.")
        else:
            self._active = True
            print(" Account unfrozen successfully.")

    def request_atm(self):
        if self._atm_requested:
            print(" ATM card already requested.")
        else:
            self._atm_requested = True
            print(" ATM card request approved.")

    def request_cheque_book(self):
        if self._cheque_requested:
            print(" Cheque book already requested.")
        else:
            self._cheque_requested = True
            print(" Cheque book request approved.")


class SavingsAccount(Account):
    def _init_(self, name, balance, pin):
        super()._init_(name, balance)
        self.__pin = pin
        self._daily_limit = 20000

    def check_balance(self, pin):
        if pin != self.__pin:
            print("Incorrect PIN.")
        elif not self._active:
            print(" Account is frozen.")
        else:
            print(f" Savings Balance: ₹{self._balance}")

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            print(" Incorrect PIN.")
        elif not self._active:
            print(" Account is frozen.")
        elif amount > self._balance:
            print(" Insufficient balance.")
        elif amount > self._daily_limit:
            print(" Exceeds daily withdrawal limit.")
        else:
            self._balance -= amount
            print(f" Withdrawn ₹{amount}. Remaining balance: ₹{self._balance}")

    def deposit(self, amount, pin):
        if pin != self.__pin:
            print(" Invalid PIN.")
        elif amount <= 0:
            print(" Invalid deposit amount.")
        else:
            self._balance += amount
            print(f" Deposited ₹{amount}. New balance: ₹{self._balance}")


class BusinessAccount(Account):
    def _init_(self, business_name, balance, overdraft_limit=50000, loan_limit=100000):
        super()._init_(business_name, balance)
        self._overdraft_limit = overdraft_limit
        self._loan_limit = loan_limit

    def withdraw(self, amount):
        if not self._active:
            print(" Account inactive.")
        elif amount > (self._balance + self._overdraft_limit):
            print(" Exceeds overdraft limit.")
        else:
            self._balance -= amount
            print(f" Withdrawn ₹{amount}. New balance: ₹{self._balance}")

    def request_loan(self, amount):
        if amount <= self._loan_limit:
            print(f" Loan of ₹{amount} approved.")
        else:
            print(" Loan request exceeds limit.")


if _name_ == "_main_":
    print(" Savings Account Tests ")
    s1 = SavingsAccount("Deekshitha", 50000, 1234)

    s1.check_balance(1234)         # Correct PIN
    s1.check_balance(9999)         # Wrong PIN
    s1.withdraw(10000, 1234)       # Within limit
    s1.withdraw(25000, 1234)       # Above daily limit
    s1.withdraw(1000, 9999)        # Wrong PIN
    s1.deposit(5000, 1234)         # Valid deposit
    s1.deposit(2000, 1111)         # Wrong PIN
    s1.request_atm()               # Request ATM
    s1.request_atm()               # Request again
    s1.request_cheque_book()       # Request cheque book
    s1.request_cheque_book()       # Request again
    s1.freeze_account()            # Freeze account
    s1.withdraw(1000, 1234)        # Withdraw after freeze
    s1.unfreeze_account()          # Unfreeze

    print("Business Account Tests ")
    b1 = BusinessAccount("Tech Solutions Pvt Ltd", 100000)

    b1.check_balance()
    b1.withdraw(120000)            # Within overdraft
    b1.withdraw(200000)            # Above overdraft
    b1.request_loan(80000)         # Within limit
    b1.request_loan(150000)        # Above limit
    b1.request_cheque_book()       # Request cheque book
    b1.request_cheque_book()       # Request again
