# This is a comment in Python
# variables are used to store data values
x = 5           # integer
y = 3.14        # float
name = "Alice"  # string
# a letter is a list of characters in 
# quotation marks 
is_student = True  # boolean True or False
# Print the values of the variables
print(x)
print(y)
print(name)
print(is_student)
#place in sentence without f-strings
print("My name is " + name + ", I am " + str(x) + " years old.")
#the plus sign (+) is used to concatenate strings
# str(x) converts the integer x to a string
# type() function returns the type of a variable
print(type(x))          # <class 'int'>
print(type(y))          # <class 'float'>
print(type(name))       # <class 'str'>
print(type(is_student)) # <class 'bool'>
# lets make a new set of variables to practice
a = 10
b = 2.5
c = "Bob"
d = False
# Print the values of the new variables in a sentence
# using concatenation
print("My name is " + c + ", I have " + str(a) + " apples.")
# using the f string method
print(f"My name is {c}, I have {a} apples.")