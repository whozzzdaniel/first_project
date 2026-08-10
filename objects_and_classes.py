class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def bark(self):
		print(f"{self.name.upper()} says woof woof! I'm {self.age} years old!")

dog_1 = Dog("Jack", 3)
dog_2 = Dog("Thatcher", 5)

# Call the bark method
dog_1.bark()  # JACK says woof woof! I'm 3 years old!
dog_2.bark()  # THATCHER says woof woof! I'm 5 years old!

# Methods And Attributes

# Instance And Class Attributes

class Dog:
	species = "French Bulldog" # Class attribute

	def __init__(self, name):
		self.name = name # Instance attribute

print(Dog.species) # French Bulldog

dog1 = Dog("Jack")
print(dog1.name)    # Jack
print(dog1.species) # French Bulldog

dog2 = Dog("Tom")
print(dog2.name)    # Tom
print(dog2.species) # French Bulldog

class Car:
	def __init__(self, color, model):
		self.color = color # Instance Attribute
		self.model = model # Instance Attribute

car_1 = Car("red", "Toyota Corolla")
car_2 = Car("green", "Lamborghini Revuelto")

print(car_1.model) # Toyota Corolla
print(car_2.model) # Lamborghini Revuelto

print(car_1.color) # red
print(car_2.color) # green

# Methods

class Dog:
	species = "French Bulldog" # Class Attribute

	def __init__(self, name):
		self.name = name # Instance Attribute

	def bark(self): # Method
		return f"{self.name} says woof woof!"

jack = Dog("Jack")
jill = Dog("Jill")

print(jack.bark()) # Jack says woof woof!
print(jill.bark()) # Jill says woof woof!

class Car:
	def __init__(self, color, model):
		self.color = color  # Instance Attribute
		self.model = model  # Instance Attribute

	def describe(self): # Method
		return f"This car is a {self.color} {self.model}"

car_1 = Car("red", "Toyota Corolla")
car_2 = Car("green", "Lamborghini Revuelto")

print(car_1.describe()) # This car is a red Toyota Corolla
print(car_2.describe()) # This car is a green Lamborghini Revuelto


# Special Methods ("Magic Methods", "Dunder Methods")

3 + 4 # 3.__add__(3) under the hood, Python automatically handles it
3 > 4 # 3.__gt__(4)
# and so on

class Book:
	def __init__(self, title, pages):
		self.title = title
		self.pages = pages

book1 = Book("Built Wealth Like a Boss", 420)
book2 = Book("Be Your Own Start", 420)

# print(len(book1)) TypeError: object of type 'Book' has no len(), Python doesn't know how to handle it
print(str(book1)) # <__main__.Book object at 0x102ed2900>, Default output
print(book1 == book2) # False even though they have the same number


class Book:
	def __init__(self, title, pages):
		self.title = title
		self.pages = pages

	# Teaching Python how to handle this operations
	def __len__(self):
		return self.pages

	def __str__(self):
		return f"'{self.title}' has {self.pages} pages"

	def __eq__(self, other):
		return self.pages == other.pages


book1 = Book("Built Wealth Like a Boss", 420)
book2 = Book("Be Your Own Start", 420)

print(len(book1))  # 420
print(len(book2))  # 420
print(str(book1))  # 'Built Wealth Like a Boss' has 420 pages
print(str(book2))  # 'Be Your Own Start' has 420 pages
print(book1 == book2)  # True

class Cart:
	def __init__(self):
		self.items = []

	def add(self, item):
		self.items.append(item)

	def remove(self, item):
		if item in self.items:
			self.items.remove(item)
		else:
			print(f'{item} is not in cart')

	def list_items(self):
		return self.items

	def __len__(self):
		return len(self.items)

	def __getitem__(self, index):
		return self.items[index]

	def __contains__(self, item):
		return item in self.items

	def __iter__(self):
		return iter(self.items)

cart = Cart()
cart.add('Laptop')
cart.add('Mouse')
cart.add('Keyboard')
cart.add('Monitor')

for item in cart:
	print(item, end=' ') # Laptop Mouse Keyboard Monitor

print(len(cart)) # 4
print(cart[3]) # Monitor

print('Monitor' in cart) # True
print('banana' in cart) # False

cart.remove('Keyboard')

print(cart.list_items()) # ['Laptop', 'Mouse', 'Monitor']

cart.remove('banana') # banana is not in cart

# Handling Object Attributes Dynamically

# getattr()

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age


person = Person('John Doe', 30)

print(getattr(person, 'name'))  # John Doe
print(getattr(person, 'age'))  # 30
print(getattr(person, 'city', 'Milano'))  # Milano, default value

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

person = Person('John Doe', 30)

attr_name = 'John Doe' # We can get the attribute at runtime so we dynamically handle it
print(getattr(person, attr_name, 'Attribute not found'))

# dir(), displays all the attributes and methods of an object

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

person = Person('John Doe', 30)

# Loop through all attributes of the person object with dir() function
for attr in dir(person):
	# Ignore dunder methods like __init__ or __str__ and regular methods
	# callable() returns True if the object passed can be called (e.g, a function)
	if not attr.startswith('__') and not callable(getattr(person, attr)):
		value = getattr(person, attr)
		print(f'{attr}: {value}')
# Output
# age: 30
# name: John Doe

# setattr()

class Configuration:
	pass

# Data loaded at runtime (like from a config or env file)
settings_data = {
	'server_url': 'https://api.example.com',
	'timeout_sec': 30,
	'max_retries': 5
}

config_obj = Configuration()

# Dynamically set attributes using dictionary keys and values
for attr_name, attr_value in settings_data.items():
	setattr(config_obj, attr_name, attr_value)

print(config_obj.server_url) # https://api.example.com
print(config_obj.timeout_sec) # 30

# hasattr()

class Product:
	def __init__(self, name, price):
		self.name = name
		self.price = price

product_a = Product('T-Shirt', 25)

required_attributes = ['name', 'price', 'inventory_id']

for attr in required_attributes:
	if not hasattr(product_a, attr):
		print(f"ERROR: Product is missing the required attribute: '{attr}'")
	else:
		# Access the attributes dynamically once their existence is confirmed
		print(f'{attr}: {getattr(product_a, attr)}')

# Output:
# name: T-Shirt
# price: 25
# ERROR: Product is missing the required attribute: 'inventory_id'

# delattr()

class UserSession:
	def __init__(self, user_id, token):
		self.user_id = user_id
		self.auth_token = token # sensitive
		self.temp_counter = 0 # temporary

session = UserSession(101, 'om34fm43')

# List of attributes to remove dynamically before "saving" the session
attributes_to_clean = ['auth_token', 'temp_counter']

# Dynamically remove specified attributes
for attr in attributes_to_clean:
		if hasattr(session, attr):
			delattr(session, attr)
			print(f'Removed attribute: {attr}')

print('\nFinal attributes remaining:')

# Loop through the remaining attributes with dir()
for attr in dir(session):
		# Ignore dunder methods like __init__ or __str__ and regular methods
		if not attr.startswith('__') and not callable(getattr(session, attr)):
			print(f' - {attr}: {getattr(session, attr)}')
# Output:
# Removed attribute: auth_token
# Removed attribute: temp_counter

# Final attributes remaining:
#  - user_id: 101