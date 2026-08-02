# Dictionaries

pizza = {
	'name': 'Margherita Pizza',
	'price': 8.9,
	'calories_per_slice': 250,
	'toppings': ['mozzarella', 'basil']
}

pizza = dict([('name', 'Margherita Pizza'),
			('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])

print(pizza['name']) # 'Margherita Pizza'

pizza['name'] = 'Margherita'
print(pizza['name']) # Margherita

# .get()

print(pizza.get('toppings', [])) # ['mozzarella', 'basil'], default value = []

# .keys() and .values()

print(pizza.keys()) # dict_keys(['name', 'price', 'calories_per_slice', 'toppings'])
print(pizza.values()) # dict_values(['Margherita', 8.9, 250, ['mozzarella', 'basil']])

# .items()

print(pizza.items())
# dict_items([('name', 'Margherita'), ('price', 8.9),
# ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])

# .clear()

pizza.clear()
print(pizza) # {}

# .pop()

pizza = {
	'name': 'Margherita Pizza',
	'price': 8.9,
	'calories_per_slice': 250,
	'toppings': ['mozzarella', 'basil']
}

print(pizza.pop('price', 10)) # 8.9; default_value = 10

# .popitem()

print(pizza.popitem()) #  ('toppings', ['mozzarella', 'basil']); returns the last inserted item

# .update()

pizza = {
	'name': 'Margherita Pizza',
	'price': 8.9,
	'calories_per_slice': 250,
	'toppings': ['mozzarella', 'basil']
}

pizza.update({'price': 10, 'total_time': 25}) # updates price, adds 'total_time': 25

print(pizza)
# {'name': 'Margherita Pizza', 'price': 10, 'calories_per_slice': 250,
# 'toppings': ['mozzarella', 'basil'], 'total_time': 25}


# Looping over a dictionary

products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for price in products.values():
	print(price)
# 990
# 600
# 250
# 70

for product in products.keys():
	print(product)

# or

for product in products:
	print(product)
# Laptop
# Smartphone
# Tablet
# Headphones

for product in products.items():
	print(product)
# ('Laptop', 990)
# ('Smartphone', 600)
# ('Tablet', 250)
# ('Headphones', 70)

for product, price in products.items():
	print(product, price)
# Laptop 990
# Smartphone 600
# Tablet 250
# Headphones 70


products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for product, price in products.items():
	products[product] = round(price * 0.8) # Applying a discount

print(products) # {'Laptop': 792, 'Smartphone': 480, 'Tablet': 200, 'Headphones': 56}

# enumerate()

for product in enumerate(products):
	print(product)
# (0, 'Laptop')
# (1, 'Smartphone')
# (2, 'Tablet')
# (3, 'Headphones')

for index, product in enumerate(products):
	print(index, product)
# 0 Laptop
# 1 Smartphone
# 2 Tablet
# 3 Headphones

for price in enumerate(products.values()):
	print(price)
# (0, 792)
# (1, 480)
# (2, 200)
# (3, 56)

for index, price in enumerate(products.values()):
	print(index, price)
# 0 792
# 1 480
# 2 200
# 3 56

for index, product in enumerate(products.items()):
	print(index, product)
# 0 ('Laptop', 792)
# 1 ('Smartphone', 480)
# 2 ('Tablet', 200)
# 3 ('Headphones', 56)

for index, product in enumerate(products.items(), 1): # Starts from 1
	print(index, product)
# 1 ('Laptop', 792)
# 2 ('Smartphone', 480)
# 3 ('Tablet', 200)
# 4 ('Headphones', 56)


# Sets

my_set = {1, 2, 3, 4, 5}

set() # An empty set {}
{} # An empty dictionary

# .add()

my_set.add(6)
print(my_set) # {1, 2, 3, 4, 5, 6}

my_set.add(5) # Nothing happens, we already have the number 5 in the set
print(my_set) # {1, 2, 3, 4, 5, 6}

my_set.remove(4)
my_set.discard(4) # Does not throw an error if there is no such value

print(my_set) # {1, 2, 3, 5, 6}

# .clear()

my_set.clear()
print(my_set) # set()

# .issubset() and .issuperset()

my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

print(your_set.issubset(my_set)) # False
print(my_set.issuperset(your_set)) # False

# .isdisjoint()

print(my_set.isdisjoint(your_set)) # False

# | Union operator

print(my_set | your_set) # {1, 2, 3, 4, 5, 6}

# & Intersection operator

print(my_set & your_set) # {2, 3, 4}

# - Difference operator

print(my_set - your_set) # {1, 5}

# ^ Symmetric difference operator

print(my_set ^ your_set) # {1, 5, 6}

# All operators have compound assignment version |=, &=, -=, ^=

my_set -= your_set
print(my_set) # {1, 5}

# in

print(5 in my_set) # True