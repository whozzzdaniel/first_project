# name = input('What is your name? ') # User types 'Danila' and presses enter
# print(f'Hello, {name}!') # Hello, Danila!


# Defining custom functions

def hello():
	print('Hello World!')

hello() # Hello World!

def calculate_sum(a, b):
	print(a + b)

calculate_sum(2, 3) # 5

my_sum = calculate_sum(2, 3) # Implicitly returns None
print(my_sum) # None

def calculate_sum(a, b):
	return a + b

my_sum = calculate_sum(2, 3) # Explicitly returns the addition
print(my_sum) # 5


# Scopes LEGB

# Local Scope (L)

def my_func():
	my_var = 10 # !
	print(my_var)

my_func() # 10

# Enclosing Scope (E)

def outer_func():
	msg = 'Hello there!'

	def inner_func():
		print(msg) # Can access the variable of the function it is nested within

	inner_func()

outer_func() # Hello there!

# nonlocal keyword usage

def outer_func2():
	msg = 'Hello there!'
	res = "" # Declare res in the enclosing scope

	def inner_func():
		nonlocal res # Allow modification of an enclosing variable
		res = 'How are you?'
		print(msg) # Accessing msg from outer_func()

	inner_func()
	print(res) # Now res is accessible and modified

outer_func2()
# Output:
# Hello there!
# How are you?

# Global Scope (G)

my_var = 100

def show_var():
	print(my_var)

show_var() # 100
print(my_var) # 100

# global keyword usage

my_var_1 = 7

def show_vars():
	global my_var_2
	my_var_2 = 10
	print(my_var_1)
	print(my_var_2)

show_vars() # 7 10

print(my_var_2)  # my_var_2 is now a global variable and can be accessed anywhere in the program

my_var = 10 # A global variable

def change_var():
	global my_var # Allows modification of a global variable
	my_var = 20

change_var()
print(my_var) # my_var is now modified globally to 20

# Built-in Scope (B)
# Refers to all python keywords, built-in functions, modules, available anywhere

print(str(45)) # "45"
print(type(3.14)) # <class 'float'>
print(isinstance(3, str)) # False