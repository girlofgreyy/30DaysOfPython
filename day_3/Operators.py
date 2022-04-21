
# Declaring the variable at the top first

from math import remainder


a = 3
b = 2 

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b                      # Kalan sayıyı veriyor
floor_division = a // b                # Kalansız bölme
exponential = a ** b

print('a + b = ', total)
print('a - b =', diff)
print('a * b = ', product)
print('a / b=', division)
print('a % b =',remainder)
print('a// b =', floor_division)
print('a ** b=', exponential)


print('== Addition, Subtraction, Multiplication, Division, Modulus ==')
num_one = 3
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

print('total:', total)
print('difference:', diff)
print('product:', product)
print('division:', div)
print('remainder:', remainder)

# Calculating area of a circle
radius = 10 
area_of_circle = 3.14 * radius ** 2  
print('Area of circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3

# Comparison Operators
print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Comparing something gives either a True or False
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

# is: Returns true if both variables are the same object(x is y)
# is not: Returns true if both variables are not the same object(x is not y)
# in: Returns True if the queried list contains a certain item(x in y)
# not in: Returns True if the queried list doesn't have a certain item(x in y)

print('1 is 1', 1 is 1)                # True - because the data values are the same
print('1 is not 2', 1 is not 2)        # True - because 1 is not 2
print('M in Mine', 'M' in 'Mine')      # True - becouse M found in the string
print('İ in Mine', 'İ' in 'Mine')      # False - there is no uppercase İ
print('coding' in 'coding for all')    # True - coding for all has the word coding
print('4 is 2 ** 2:', 4 is 2 ** 2)     # True

# Logical Operators
print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False
print(not not not True) # FUNNY 

# EXERCISES

my_age = 23 
my_height = 1.63
a_complex_number = 5 + 1j

# Exercise 4
base = 20
height = 10
area_of_triangle = 0.5 * base * height
print('Area of triangle:', area_of_triangle)

# Exercise 5
side_a = 5
side_b = 4
side_c = 3
perimeter_of_triangle = side_a + side_b + side_c
print('Perimeter of triangle:', perimeter_of_triangle)

# Exercise 6
length = 10
width = 5
area_of_rectangle = length * width
permeter_of_rectangle = 2 * (length + width)
print('Area of rectangle:', area_of_rectangle)
print('Permeter of rectangle:', permeter_of_rectangle)

# Exercise 7
radius = 7
π = 3.14
area_of_circle = π * radius **2 
print('Area of circle:',area_of_circle)
circumference_of_circle = 2 * π * radius
print('circumference of circle:', circumference_of_circle)

radius = 7
π = 3.14
area_of_circle = π * radius **2 
print('Area of circle:',area_of_circle)
circumference_of_circle = 2 * π * radius
print('circumference of circle:', circumference_of_circle)





