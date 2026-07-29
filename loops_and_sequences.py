# Sequence Types

# Lists

cities = ['New York', 'Los Angeles', 'Tokyo']
cities[0] # 'New York'
cities[-1] # 'Tokyo'

# list()

name = 'Jessica'
list(name) # ['J', 'e', 's', 's', 'i', 'c', 'a']

# len()

numbers = [1, 2, 3, 4, 5]
len(numbers) # 5

# Updating values

programming_languages = ['Python', 'Java', 'C++']
programming_languages[0] = 'JavaScript'
print(programming_languages) # ['JavaScript', 'Java', 'C++']

# del()

developer = ['Jane Doe', 23, 'Python']
del developer[1]
print(developer) # ['Jane Doe', 'Python']

# in

programming_languages = ['Python', 'Java', 'C++']
'C++' in programming_languages # True
'JavaScript' in programming_languages # False

# Nested lists

developer = ['Jane Doe', 23, ['Python', 'Java', 'C++']]
developer[2][1] # Accessing nested list values, 'Java'

# Unpacking values

developer = ['Jane Doe', 23, 'Python']
name, age, language = developer

print(name) # 'Jane Doe'
print(age) # 23
print(language) # 'Python'

name, *rest = developer
print(name) # 'Jane Doe'
print(rest) # [23, 'Python']

# Slicing

desserts = ['Cookie', 'Ice Cream', 'Cake', 'Pie', 'Brownie']
desserts[1:4] # ['Ice Cream', 'Cake', 'Pie']

numbers = [1, 2, 3, 4, 5, 6]
numbers[1::2] # [2, 4, 6]

# append()

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers) # [1, 2, 3, 4, 5, 6]

even_numbers = [6, 8, 10]
numbers.append(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, [6, 8, 10]]

# extend()

numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]
numbers.extend(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, 6, 8, 10]

# insert()

numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2.5)
print(numbers) # [1, 2, 2.5, 3, 4, 5]

# remove()

numbers = [10, 20, 30, 40, 50, 50]
numbers.remove(50)
print(numbers) # [10, 20, 30, 40, 50]

numbers = [10, 20, 30, 40, 50, 50, 50]
numbers.remove(50)
print(numbers) # [10, 20, 30, 40, 50, 50]

# pop()

numbers = [1, 2, 3, 4, 5]
numbers.pop(1) # The number 2 is returned

numbers = [1, 2, 3, 4, 5]
numbers.pop() # The number 5 is returned

# clear()

numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers) # []

# sort()

numbers = [19, 2, 44, 100, 0]
numbers.sort()
print(numbers) # [0, 2, 19, 44, 100]

# sorted()

numbers = [19, 2, 44, 100, 0]
sorted_numbers = sorted(numbers)
print(sorted_numbers) # [0, 2, 19, 44, 100]
print(numbers) # [19, 2, 44, 100, 0]

# reverse()

numbers = [5, 4, 3, 2, 1]
numbers.reverse()
print(numbers) # [1, 2, 3, 4, 5]

# index()

programming_languages = ['Python', 'Java', 'C++']
programming_languages.index('Java') # 1


# Tuples

developer = ('Jane Doe', 23, 'Python')
developer[1] # 23

numbers = (1, 2, 3, 4, 5)
numbers[-2] # 4

# tuple()
# Tuples are immutable so you can't use append(), pop(), insert(), del, etc.

developer = 'Jessica'
tuple(developer) # ('J', 'e', 's', 's', 'i', 'c', 'a')

# in

programming_languages = ('Python', 'Java', 'C++')
'Python' in programming_languages # True
'JavaScript' in programming_languages # False

# Unpacking values

developer = ('Jane Doe', 23, 'Python')
name, age, language = developer
print(name) # 'Jane Doe'
print(age) # 23
print(language) # 'Python'

developer = ('Jane Doe', 23, 'Python')
name, *rest = developer
print(name) # 'Jane Doe'
print(rest) # [23, 'Python']

# Slicing

desserts = ('cake', 'cookie', 'pie', 'ice cream')
desserts[1:3] # ('cookie', 'pie')

# count()

programming_languages = ('Python', 'Java', 'C++', 'Python')
programming_languages.count('Python') # 2
programming_languages.count('JavaScript') # 0

# index()

programming_languages = ('Python', 'Java', 'C++')
programming_languages.index('Java') # 1

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
programming_languages.index('Python', 3) # 5

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')
programming_languages.index('Python', 2, 5) # 2

# sorted()

numbers = (32, 100, 12, 4, 67, 112, 0 , 5)
sorted(numbers) # [0, 4, 5, 12, 32, 67, 100, 112]

programming_languages = ('Python', 'Java', 'C++', 'Rust', 'JavaScript')
print(sorted(programming_languages, key=len)) # ['C++', 'Java', 'Rust', 'Python', 'JavaScript']

print(sorted(programming_languages, key=len, reverse=True)) # ['JavaScript', 'Python', 'Java', 'Rust', 'C++']


# Loops

# for loop

programming_languages = ['Python', 'Java', 'C++']

for language in programming_languages:
	print(language)
# Output:
# Python
# Java
# C++

for char in 'code':
	print(char)
# Output:
# c
# o
# d
# e

# nested for loops

categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
	for food in foods:
		print(category, food)
# Output:
# Fruit Apple
# Fruit Carrot
# Fruit Banana
# Vegetable Apple
# Vegetable Carrot
# Vegetable Banana


# while loop

secret_number = 3
guess = 0

# while guess != secret_number:
# 	guess = int(input('Guess a number (1-5): '))
# 	if guess != secret_number:
# 		print('You guessed wrong. Try again.')

print('You got it!')

# break

developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
	if developer == 'Naomi':
		break
	print(developer) # Jess

# continue

developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
	if developer == 'Naomi':
		continue
	print(developer)
# Output:
# 'Jess'
# 'Tom'

# else in loops

words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
	for letter in word:
		if letter.lower() in 'aeiou':
			print(f"'{word}' contains the vowel '{letter}'")
			break
	else:
		print(f"'{word}' has no vowels")
# Output:
# 'sky' has no vowels
# 'apple' contains the vowel 'a'
# 'rhythm' has no vowels
# 'fly' has no vowels
# 'orange' contains the vowel 'o'


# range()

for num in range(3):
	print(num)
# Output:
# 0
# 1
# 2

for num in range(3, 5):
	print(num)
# Output:
# 3
# 4

for num in range(2, 11, 2):
	print(num)
# Output:
# 2
# 4
# 6
# 8
# 10

for num in range(40, 0, -10):
	print(num)
# Output:
# 40
# 30
# 20
# 10

numbers = list(range(2, 11, 2))
print(numbers) # [2, 4, 6, 8, 10]


# enumerate()

languages = ['Spanish', 'English', 'Russian', 'Chinese']
print(list(enumerate(languages))) # [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]

languages = ['Spanish', 'English', 'Russian', 'Chinese']
for index, language in enumerate(languages):
	print(f'Index {index} and {language} language')
# Output:
# Index 0 and Spanish language
# Index 1 and English language
# Index 2 and Russian language
# Index 3 and Chinese language

languages = ['Spanish', 'English', 'Russian', 'Chinese']
for index, language in enumerate(languages, 1):
	print(f'Index {index} and {language} language')
# Output:
# Index 1 and Spanish language
# Index 2 and English language
# Index 3 and Russian language
# Index 4 and Chinese language

# zip()

developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]
print(list(zip(developers, ids))) # [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]

developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]
for name, dev_id in zip(developers, ids):
	print(f'Name: {name}')
	print(f'ID: {dev_id}')
# Output:
# Name: Naomi
# ID: 1
# Name: Dario
# ID: 2
# Name: Jessica
# ID: 3
# Name: Tom
# ID: 4


# List Comprehensions

even_numbers = []
for num in range(21):
	if num % 2 == 0:
		even_numbers.append(num)
print(even_numbers) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# or

even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result) # [(1, 'Odd'), (2, 'Even'), (3, 'Odd'), (4, 'Even'), (5, 'Odd')]

# filter()

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
	return len(word) > 4

long_words = list(filter(is_long_word, words))
print(long_words) # ['mountain', 'river', 'cloud']

# map()

celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
	return (temp * 9 / 5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit) # [32.0, 50.0, 68.0, 86.0, 104.0]

# sum()

numbers = [5, 10, 15, 20]
total = sum(numbers)
print(total) # 50

numbers = [5, 10, 15, 20]
total = sum(numbers, 10) # positional argument, initial value
print(total) # 60

numbers = [5, 10, 15, 20]
total = sum(numbers, start=10) # keyword argument, initial value
print(total) # 60


# Lambda Functions

def is_even(x):
	return x % 2 == 0
# or

lambda x: x % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]