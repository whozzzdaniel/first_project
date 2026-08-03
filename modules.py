# Ways to import a module or function from a module

# import math
# import math as m
# from math import sin as s, cos as c

from math import sin, cos, radians
import datetime

# Math

angle_degrees = 40
angle_radians = radians(angle_degrees)

sine_value = sin(angle_radians)
cosine_value = cos(angle_radians)

print(sine_value) # 0.6427876096865393
print(cosine_value) # 0.766044443118978

# Datetime

birthday = datetime.date(2006, 10, 22)
print(birthday.year) # 2006
print(birthday.month) # 10
print(birthday.day) # 22

