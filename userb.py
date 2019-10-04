class User:
	def __init__(self, name, email, account = 1):
		self.name = name
		self.email = email
		self.account = BankAccount(int_rate=.02, balance = 0)
	def make_deposit(self, amount):
		self.account.deposit(amount)
		return self
	def make_withdrawal(self, amount):
		self.account.withdraw(amount)
		return self
	def display_user_balance(self):
		print(self.name, self.account.balance)
		return self
	def transfer(self, other_user, amount):
		self.account.balance -= amount
		other_user.account.balance += amount
		return self	
	def interest(self):
		if self.account.balance > 0:
			self.account.balance *= (1 + self.account.int_rate)
			return self

	
class BankAccount:
	def __init__(self, int_rate=.02, balance=0):
		self.name = self
		self.int_rate = int_rate
		self.balance = balance

	def deposit(self, amount):
		self.balance += amount
		return self

	def withdraw(self, amount):
		self.balance -= amount
		return self

	def display_account_info(self):
		print(self.name, self.balance)
		return self

	def yield_interest(self):
		if self.balance > 0:
			self.balance *= (1 + self.int_rate)
		return self


Mark = User("Mark Mark", "mark@mail.com")
Mark2 = User("Mark Mark", "mark@mail.com", 2)
Jeff = User("Jeff Sloan", "jeff@mail.com")
John = User("John Doe", 'john@doe.com')

print(Mark.name, Jeff.name, John.name)
Mark.make_deposit(100).display_user_balance().make_deposit(100).make_withdrawal(50).interest().display_user_balance()
Mark2.make_deposit(1000).display_user_balance().interest().display_user_balance()