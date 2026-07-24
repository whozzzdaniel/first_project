# Conditional Statements and Logical Operators

# Comparison Operators

print(3 > 4) # False
print(3 < 4) # True
print(3 == 4) # False
print(3 != 4) # True
print(4 == 4) # True
print(3 >= 4) # False
print(3 <= 4) # True

# Conditional Statements

# If statement
age = 18

if age >= 18:
	print('You are an adult') # You are an adult

age = 12

if age >= 18:
	print('You are an adult') # Nothing shows up in the terminal

# If...else statement

age = 12

if age >= 18:
	print('You are an adult')
else:
	print('You are not an adult yet') # You are not an adult yet

# If...elif...else statement

age = 12

if age >= 18:
	print('You are an adult')
elif age >= 13:
	print('You are a teenager')
else:
	print('You are a child') # You are a child

# Truthy and Falsy values

print(bool(False)) # False
print(bool(0)) # False
print(bool('')) # False

print(bool(True)) # True
print(bool(1)) # True
print(bool("Hello")) # True

# Logical operators

# And Operator

is_citizen = True
age = 25

print(is_citizen and age) # 25

if is_citizen and age >= 18:
	print('You are eligible to vote') # You are eligible to vote
else:
	print('You are not eligible to vote')

# Or Operator

age = 19
is_employed = False

print(age or is_employed) # 19

age = 19
is_student = True

if age < 18 or is_student:
	print('You are eligible for a student discount') # You are eligible for a student discount
else:
	print('You are not eligible for a student discount')

# Not Operator

print(not "") # True
print(not False) # True
print(not 0) # True

print(not True) # False
print(not 1) # False
print(not "Hello") # False

is_admin = False

if not is_admin:
	print('Access denied for non-administrators') # Access denied for non-administrators
else:
	print('Welcome, Administrator!')