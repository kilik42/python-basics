#comments in Python start with the '#' symbol.
# The purpose of comments is to explain
#  the code and make it more understandable for humans.
# Comments are ignored by the Python interpreter.
# they are notes for anyone reading the code. 

# variables are used to store data values.
name = "Bob"  # This is a string variable
#string variables are used to store text data.
# noted by the quotation marks around the text.
age = 30        # This is an integer variable
# Integer variables are used to store whole numbers.
height = 5.5    # This is a float variable
# Float variables are used to store decimal numbers.
is_student = True  # This is a boolean variable
# Boolean variables are used to store True or False values.
# Now we will print the variables to the console.
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# when we make sentences in python
# we can use the + symbol to join strings together.
#concatenation is the process of joining strings using the + operator.
print("Hello, my name is " + name + ". I am " + str(age) + " years old.")
# Note: We use the str() function to convert the integer 'age' to a string
# so that we can concatenate it with other strings.
print("I am " + str(height) + " feet tall.")
# this is the old or classic way of formatting strings in python.
# There are newer methods like f-strings and the format() method.
print(f"My name is {name}, I am {age} years old and {height} feet tall.")
#challenge: create 5 more strings using f-strings
date = "2024-06-15"
weather = "sunny"
mood = "happy"
hobby = "painting"
city = "New York"
#print a sentence using all the variables above using f-strings


print("we did it!")