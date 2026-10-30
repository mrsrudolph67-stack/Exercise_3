import math
# Question 1
print ("Question 1")

def greet ():
    print ("Hello, World!")
greet ()

# Question 2
print ("Question 2")

def personalized_greeting (name):
    print ("Hello, "+name)
personalized_greeting ("Shakeer. you're so smart.")

# Question 3
print ("Question 3")

def square (number):
    return number ** 2
result = square (5)
print (result)

# Question 4
print ("Question 4")

def rectangle_area (length, width):
    return length * width

result_1 = rectangle_area (4, 5)
print (result_1)

# Question 5
print ("Question 5")

def apply_operation (function, number):
    return function (number)

def double (number):
    return number * 2

print (apply_operation(double, 7))
print (apply_operation(square, 3))