# Assignment

name = "John Doe" # String
age = 23 # Integer
my_float_var = 3.14 # Float
my_boolean_var = True # Boolean
my_set_var = {7, 'hello', 8.5} # Set
my_dict_var = {'name': 'John Doe', 'age': 23} # Dictionary
my_tuple_var = (7, 'hello', 8.5) # Tuple
my_range_var = range(5) # Range
my_list_var = [1, 2, 'John Doe', 4, 5] # List
my_none_var = None # None

# Printing

print('Float:', my_float_var)
print('Boolean:', my_boolean_var)
print('Set:', my_set_var)
print('Dictionary:', my_dict_var)
print('Tuple:', my_tuple_var)
print('Range:', my_range_var)
print('List:', my_list_var)
print('None:', my_none_var)
print('Name:', name)
print('Age:', age)

# Checking

print(type(my_float_var)) # <class 'float'>
print(type(my_boolean_var)) # <class 'bool'>

print(isinstance(my_float_var, float)) # True
print(isinstance(my_float_var, (str, float))) # True
print(isinstance(my_float_var, (str, int))) # False
print(isinstance(my_float_var, int)) # False

# Multi-line strings

my_str = """multiline
string"""
my_str_2 = '''another multiline
string'''

print(my_str)
print(my_str_2)

# Backslash usage

msg = 'It\'s a sunny day'
quote = "She said \"Hello World!\""

print(msg)
print(quote)

# Operator "in"

my_str = "Hello"

print('Hello' in my_str) # True
print('Hi' in my_str) # False

# "Len" function and indexing

my_str = "Hello World!"

print(len(my_str)) # 12
print(my_str[0]) # H
print(my_str[1]) # e
print(my_str[-1]) # !
print(my_str[-2]) # d

# Immutability

my_str = "Hello"
my_str = "Hi"
# my_str[0] = "A" – TypeError

# String concatenation

my_str = "Hello"
my_str_2 = "World"

str_plus_str = my_str + " " + my_str_2
print(str_plus_str) # Hello World

# Concatenation works only with strings

# age = 20 – Integer
# name = "David" – String

# name_and_age = name + age – TypeError

# Conversion using str()

age = 20
name = "David"

name_and_age = name + str(age)
print(name_and_age) # David20

# Augmented assignment operator

name = "David"
age = 20

name_and_age = name
name_and_age += str(age)

print(name_and_age) # David20

# String interpolation

name = "David"
age = 20
name_and_age = f"My name is {name} and my age is {age}" # Auto conversion from int to str (age)
print(name_and_age) # My name is David and my age is 20

num1 = 5
num2 = 10
print(f"The sum of {num1} and {num2} is {num1 + num2}") # The sum of 5 and 10 is 15

# String slicing

my_str = "Hello World"
print(my_str[1:4]) # ell
print(my_str[:7]) # Hello W
print(my_str[8:]) # rld
print(my_str[:]) # Hello World

print(my_str) # Does not modify the original string – Hello World

print(my_str[:11:2]) # Using step – printing every second character – HloWrd

print(my_str[::-1]) # Reverse string using step -1 – dlroW olleH

# Common string methods

my_str = "Hello World"
uppercase_my_str = my_str.upper()
print(uppercase_my_str) # HELLO WORLD

my_str = "Hello World"
lowercase_my_str = my_str.lower()
print(lowercase_my_str) # hello world

my_str = "   Hello World   "
trimmed_my_str = my_str.strip()
print(trimmed_my_str) # "Hello World"

my_str = "Hello World"
replaced_my_str = my_str.replace("Hello", "Hi")
print(replaced_my_str) # Hi world

my_str = "Hello World"
split_words = my_str.split()
print(split_words) # ['Hello', 'World']

my_list = ["Hello", "World", "!"]
joined_my_str = " ".join(my_list)
print(joined_my_str) # Hello World !

my_str = "Hello World"
ends_with_world = my_str.endswith("World")
print(ends_with_world) # True

my_str = "Hello World"
world_index = my_str.find("World")
print(world_index) # 6

my_str = "Hello World"
o_count = my_str.count("o")
print(o_count) # 2

my_str = "hello world"
capitalized_my_str = my_str.capitalize()
print(capitalized_my_str) # Hello world

my_str = "Hello World"
is_all_upper = my_str.isupper()
print(is_all_upper) # False

my_str = "hello world"
is_all_lower = my_str.islower()
print(is_all_lower) # True

my_str = "Hello World"
title_case_my_str = my_str.title()
print(title_case_my_str) # Hello World


# Integers and floats

my_int_1 = 56
my_int_2 = 12
my_float_1 = -12.0
my_float_2 = 4.9

# Addition

sum_ints = my_int_1 + my_int_2
print('Integer Addition:', sum_ints) # Integer Addition: 68

sum_floats = my_float_1 + my_float_2
print('Float Addition:', sum_floats) # Float Addition: -7.1

sum_int_and_float = my_int_1 + my_float_1
print(sum_int_and_float) # 44.0
print(type(sum_int_and_float)) # <class 'float'>

# Subtraction

diff_ints = my_int_1 - my_int_2
print('Integer Subtraction:', diff_ints) # Integer Subtraction: 44

diff_floats = my_float_1 - my_float_2
print('Float Subtraction:', diff_floats) # Float Subtraction: -16.9

# Division

div_ints = my_int_1 / my_int_2
print('Integer Division:', div_ints) # Integer Division: 4.666666666666667

div_floats = my_float_1 / my_float_2
print('Float Division:', div_floats) # Float Division: -2.4489795918367343

# Multiplication

product_ints = my_int_1 * my_int_2
print('Integer Multiplication:', product_ints) # Integer Multiplication: 672

product_floats = my_float_1 * my_float_2
print('Float Multiplication:', product_floats) # Float Multiplication: -58.800000000000004

# Modulo Operator

mod_ints = my_int_1 % my_int_2
mod_floats = my_float_1 % my_float_2

print('Integer Modulo:', mod_ints) # Integer Modulo: 8
print('Float Modulo:', mod_floats) # Float Modulo: 2.700000000000001

# Floor Division

floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float_1 // my_float_2

print('Integer Floor Division:', floor_div_ints) # Integer Floor Division: 4
print('Float Floor Division:', floor_div_floats) # Float Floor Division: -3.0

# Exponentiation

exp_ints = my_int_1 ** my_int_2
exp_floats = my_float_1 ** my_float_2

print('Integer Exponentiation:', exp_ints) # Integer Exponentiation: 951166013805414055936
print('Float Exponentiation:', exp_floats) # Float Exponentiation: (-184584.1607052842+59975.02942576666j)

# Conversion using int() and float()

my_int_1 = 56
my_float_1 = float(my_int_1)

print(my_float_1) # 56.0
print(type(my_float_1)) # <class 'float'>

my_float = 2.96
my_int = int(my_float)

print(my_int) # 2
print(type(my_int)) # <class 'int'>

my_str_int = "23"
my_str_float = "3.14"

converted_int = int(my_str_int)
converted_float = float(my_str_float)

print(converted_int, type(converted_int)) # 23 <class 'int'>
print(converted_float, type(converted_float)) # 3.14 <class 'float'>

# Numeric methods

# Round

my_num_1 = 2.965
my_num_2 = 4.253

rounded_num_1 = round(my_num_1)
rounded_num_2 = round(my_num_2, 1)

print(rounded_num_1) # 3
print(rounded_num_2) # 4.3

# Abs

num = -15

absolute_value = abs(num)
print(absolute_value) # 15

# Pow

result_1 = pow(2, 3) # 2 ** 3
print(result_1) # 8

result_2 = pow(2, 3, 5) # (2 ** 3) % 5
print(result_2) # 3