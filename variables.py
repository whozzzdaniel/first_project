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
