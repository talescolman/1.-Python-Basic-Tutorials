# Python complete tutorial

# 1) Hello World:
print("Hello, world!")

# 2) COMMENTS

# this is a single line comment

''' this is
a multipl line
comment '''

# 3) MULTI-LINE STATEMENTS

a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9

# you can use \, (), {}, or [] to implement multi-line statements
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9

a = [1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9]

# 4) MULTIPLE STATEMENTS IN THE SAME LINE, using ; 
a = 1; b = 2; c = 3

# 5) IDENTATION, usually 4 spaces (and not TAB):

for i in range(1,11):
    print(i)
    if i == 5:
        break

# 6) DOCSTRINGS """ docstring """:

def double(num):
    """Function to double the value"""
    return 2*num

# 7) VARIABLES (Python is a type-inferred language, so you don't have to explicitly define the variable type):
first_name = "Godot" # use _ to separate words in the variable's name
age = 27 # you should never start a variable with a digit

# you can assigning multiple values to multiple variables
a, b, c = "Facebook", "Instagram", 27

# you can also assign the same value to multiple variables:
a = b = c = "Tik Tok"

# CONSTANTS (type of variable whose value should stay the same):
# Since Python don't have constants, we use CAPITAL LETTERS and store the constants in another file
# This is just a convention
PI = 3.14
GRAVITY = 9.8

# 8) DATATYPES
#Numbers: int 4, float 1.7, complex 8+4j (always in the x + yj way, X = real, Y = Imaginary)

# Lists []: ordered sequence of items of different (or same) type. It can be altered:
l = ["this is my list", 24]

# Tuple (): Just like lists, but immutable
t = ("This is a Tuple", 13)

# Strings '' or "". They are immutable.
s = "This is a string"

s = '''This is a 
multiline string'''

# Set {}. Unordered collection of unique items (they eliminate duplicates:
se = {4,3,2,8,10}

# Dictionary {key:value}. Unordered collection of key-value pairs.
d = {'name':'Peter', 'Age':27, 'City':'Bratislava'}

# 9) INPUT AND OUTPUT

# print() used to output
print("This is an output.")

age = 88
print("I'm ", age)

# print() formatting

print(1, 2, 3, 4, 5, 6, sep=' ') # you can use as separator anything

# format(x,y)
name = "Godot"
age = 27
print("We are waiting for {}, he is {} years old.".format(name,age))

# format() using keyholders
print("We are waiting for {name}, he is {age} years old.".format(name = 'Godot',age = 27)

# input()
name = input('Enter your name: ')

# 10) IMPORT
# to import Python files (.py extensions, also called modules) you can use the import nameofmodule
import brands

from brands import carbrand #in order to import some attributes and functions only

# 11) OPERATORS

# a) Arithmetic operators
1+1 
4-2
2*18 # multiply
243/147 # divide
88%77 # Modulus, remainder of the division of left operand by the right
77//4 # Floor division - division that results into whole number adjusted to the left in the number line
32**17 # Exponent - left operand raised to the power of right

# b) Comparison operators
10>5 # Greater than - True if left operand is greater than the right
4<8 # Less than - True if left operand is less than the right
5==5 # Equal to - True if both operands are equal
12!=4 # Not equal to - True if operands are not equal
19>=15 # Greater than or equal to - True if left operand is greater than or equal to the right
22<=34 # Less than or equal to - True if left operand is less than or equal to the right

# c) Logical operators
x = True
y = True

x and y # True if both the operands are true
x or y # True if either of the operands is true
not x # True if operand is false (complements the operand)

# d) Bitwise operators (to use with binary)
x & y = 0 # AND
x | y = 14 # OR
~x = -11 # NOT
x ^ y = 14 # XOR
x >> 2 = 2 # Right shift
x << 2 = 40 # Left shift

# e) Assignment operators (to assign values to variables)
x = 10
x += 10 # x = x + 10
x -= 10 # x = x - 10
x *= 10 # x = x * 10
x /= 10 # x = x / 10
x %= 10 # x = x % 10
x //= 10 # x = x // 10
x **= 10 # x = x ** 10
x &= 10 # x = x & 10
x |= 10 # x = x | 10
x ^= 10 # x = x ^ 10
x >>= 10 # x = x >> 10
x <<= 10 # x = x << 10

# f) Identity operators (used to check if two values (or variables) are located on the same part of the memory)
x is True # if the operands are located on the same part of the memory
x is not True # if the operands are located on different parts of the memory

# g) Membership operators (to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary))
in # True if value/variable is found in the sequence
not in # True if value/variable is not found in the sequence

x = ['Volvo', 'VW', 'Opel']

print('Ford' not in x) # Output: True
print('Volvo' in x) # Output: True

# 11) FLOW CONTROL
# a) if / elif / else 
''' if test expression:
    Body of if
else:
    Body of else '''

num = 1.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# Nested if / else / else
num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

# B) For Loop
''' for val in sequence:
	Body of for '''

numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum = 0

for val in numbers:
	sum = sum+val
else:
	print("No items left.")

student_name = 'Soyuj'

marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break # else is executed if break is not executed
else:
    print('No entry with that name found.')

for letter in 'Python':
   if letter == 'h':
      continue # rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop.
   print 'Current Letter :', letter



n = 10
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1 #update counter

counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")

# 12) PASS STATEMENT (used as a placeholder for future implementation of functions, loops, etc)

sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass

# pass can be used with functions and class

def function(args):
    pass

class Example:
    pass    


# 13) FUNCTIONS

def my_function():
  print("Hello from a function") 

my_function() # calling a function function_name()

# arguments
def my_function(house, number, price)

my_function("Villa Blu", 14, 589.000 ) # a function must be called with the correct number of arguments

def my_function(*kids): #* before the arg is used when you don't know exactly the number of args that you need, this creates a tuple
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus") 

# Default argument arg="default value", If a value is provided, it will overwrite the default value.
# once we have a default argument, all the arguments to its right must also have default values.

def greet(name, msg="Good morning!"): 
	print("Hello", name + ', ' + msg)

greet("Kate") # will print: Hello Kate, Good morning!
greet("Bruce", "How do you do?") # will print: Hello Bruce, How do you do?

# Parameters and variables defined inside a function are not visible from outside the function

def my_func():
	x = 10
	print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)

# BUT variables outside of the function are visible from inside

# Functions can be:
# a) Built-in functions (built by Python)
# b) User-defined functions (created by Users)

# Recursive function (a function that calls itself)

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 3
print("The factorial of", num, "is", factorial(num))

# the maximum depth of recursion is 1000. If the limit is crossed, it results in RecursionError. 

# Lambda functions (defined without a name, also called Anonymous Function)
# lambda syntax: lambda arguments: expression
double = lambda x: x * 2

print(double(5))







