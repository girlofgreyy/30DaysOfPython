# DAY 4
letter = 'P'
print(letter)
print(len(letter))

greeting = 'Hello World!'
print(greeting)
print(len(greeting))        

sentence = 'I am enjoying 30 days of Python challange'
print(sentence)

multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

first_name = 'Mine'
last_name = 'Sunar'
space = ' '
full_name = first_name  +  space + last_name
print(full_name)

# Trying sh*t
print('I am trying to learn Python. \nAm I?')        # \n  alt satıra geçer

print('Days\tTopics\tExercises')                     # \t sekme alanı ya da boşluk ekler tablomtrak şeyler
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')

print('This is backslash symbol (\\)')
print('In every programming language it starts with \"Hello, World!\"')

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# "%.number of digitsf" - Floating point numbers with fixed precision


a = 5
b = 4
print('{} + {} = {}'.format(a, b, a + b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)

a = 4
b = 3
print(f'{a} + {b} = {a +b}')

language = 'Mine'
a,b,c,d, = language # unpacking sequence characters into variables
print(a) 
print(b)  
print(c)  
print(d)  

language = ' ARDA'
first_letter = language [0]
second_letter = language [1]
third_letter = language [2]
fourth_letter = language [3]
fifth_letter = language [1]
print(first_letter)
print(second_letter)
print(third_letter)
print(fourth_letter)
print(fifth_letter)

language = 'MİNE'
first_two = language[0:2]
second_two = language [2:4]
print(first_two)
print(second_two)

greeting = 'I LOVE YOU'
print(greeting[::-1])

language = 'Mine'
mn = language[0:4:2] 
print(mn) 

challange = 'i love my life'
print(challange.capitalize())
print(challange.count('i'))
print(challange.endswith('fe'))

challange = 'i\tlove\tmy\tlife'
print(challange.expandtabs(10))

challange = 'i love my life'
print(challange.find('li'))
print(challange.rfind('li'))

# 26 Nisan 
# format()
first_name = 'Mine'
last_name = 'Sunar'
age = '23'
job = 'Junior Product Manager'
country = 'Turkey'
sentence = 'I am {} {}. I am {} years old. I am a {}. I live in {}.'.format(first_name, last_name, age, job, country)
print(sentence)

radius = 10
pi = 3.14
area = pi * radius **2
result = 'The area of a circle with radius {} is {}.'.format(str(radius), str(area))
print(result)

