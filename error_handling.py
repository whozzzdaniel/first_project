# try...except...else...finally

try:
	number = int('abc')
	result = 10 / number
except ValueError:
	print('That was not a valid number.')
except ZeroDivisionError:
	print("Can't divide by zero.")

try:
	number = 5
	result = 10 / number
except ZeroDivisionError:
	print("Can't divide by zero.")
else:
	print('The result is:', result) # Runs when no errors occurred
finally:
	print('Always runs') # Always runs

try:
	x = 1 / 0
except ZeroDivisionError as e:
	print(f'Error occurred: {e}') # Error occurred: division by zero

try:
	x = 1 / 0
	number = int('abc')
except (ValueError, ZeroDivisionError) as e:
	print(f'Error occurred: {e}') # Error occurred: division by zero

# raise

def check_age(age):
	if age < 0:
		raise ValueError('Age cannot be negative')
	return age

try:
	check_age(-5)
except ValueError as e:
	print(f'Error: {e}') # Error: Age cannot be negative

def process_data(data):
	try:
		result = int(data)
		return result * 2
	except ValueError:
		print('Logging: Invalid data received')
		raise # Re-raises the same ValueError

try:
	process_data('abc')
except ValueError:
	print('Handled at higher level')

# Custom Exceptions

class InsufficientFundsError(Exception):
	def __init__(self, balance, amount):
		self.balance = balance
		self.amount = amount
		super().__init__(f'Insufficient funds: ${balance} available, ${amount} requested')

def withdraw(balance, amount):
	if amount > balance:
		raise InsufficientFundsError(balance, amount)
	return balance - amount

try:
	new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
	print(f'Transaction failed: {e}')

# raise...from

def parse_config(filename):
	try:
		with open(filename, 'r') as file:
			data = file.read()
			return int(data)
	except FileNotFoundError:
		raise ValueError('Configuration file is missing')  from None
	except ValueError as e:
		raise ValueError('Invalid configuration format') from e

# assert

def calculate_square_root(number):
	assert number >= 0, 'Cannot calculate square root of negative number'
	return number ** 0.5