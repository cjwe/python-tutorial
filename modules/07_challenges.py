# === MINI PROJECTS ===

# 1. Grocery List Program:
# Ask user to input items, add them to a list, then print the list.

# 2. Simple Calculator:
# Write functions for add, subtract, multiply, divide. Ask user for numbers and operation.

# 3. Animal Zoo (OOP Challenge):
# Use classes + inheritance to model animals in a zoo. Include a method to describe each animal.

# Pick one and build it! No pressure :)

# 1. 
print()
print("Lets get a hoppin' and a shoppin'! Somebunny's hungry...")
print()
grocery_list = input("What's on your grocery list?\n")
print()
print(f"Delicious! What are you going to make with {grocery_list}? I prefer carrots myself.")
print()
print("---")


# 2.
print()
print()

def answer():
    print("The answer to your super duper difficult question that you definitely couldn't do in your head is: ")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide (x , y):
    if x == 0 or y == 0:
        return "...actually, now I get why you needed my help. Because you can't actually divide by zero. :) That's pretty basic, actually."
    return x / y

print("I get it, math is hard. If you give me two numbers I can help you add, subtract, multiply or divide them.")

x = int(input("What is the first number? "))

y = int(input("And the second number? "))

request = input("Okay smarty pants, and what would you like to do with these numbers? Add, subtract, multiply, or divide them? ").lower()

if request == "add":
    answer()
    print(add(x, y))
elif request == "subtract":
    answer()
    print(subtract(x, y))
elif request == "multiply":
    answer()
    print(multiply(x, y))
elif request == "subtract":
    answer()
    print(subtract(x, y))
elif request == "divide":
    answer()
    print(divide(x, y)) 
else:
    print(f"I don't really know what you're talking about. Try checking your spelling, like I said I can only add, subtact, multiply or divide.")

print()
print("---")

# 3. WIP - Not done yet :)
print()

class Animal:
    def __init__(self,name):
        self.name = name

    def intro(self):
        print(self.name)

class Lion(Animal):
    def intro(self):
        super().intro()

class Zebra(Animal):
    def intro(self):
        super().intro()

class Elephant(Animal):
    def intro(self):
        super().intro()

Simba = Lion("lion")
Dumbo = Elephant("elephant")
Marty  = Zebra("zebra")

print(f"We have so many animals at the zoo, three whole animals--if you can believe it! Simba, a {Simba.name}, Dumbo, an {Dumbo.name}, and Marty, a {Marty.name}.")

# Grade pending (changes needed..)

# Potential changes:
# - your division part has a smal hiccup (Hint: it's in an if statement)
# - hmmm.. your specific animals aren't really all that different from a generic animal. Don't they each have something special they're good at? ( •͡˘ _•͡˘)ノð