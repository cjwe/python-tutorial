# === FUNCTIONS ===

def greet(name):
    return f"Hello, {name}!"

print(greet("Jamie"))

def multiply(x, y):
    return x * y

print("3 * 4 =", multiply(3, 4))

# Practice:
# 1. Write a function that returns the square of a number
# 2. Write a function that takes a list and returns how many items it has
# 3. BONUS: Write a function that returns the last item in a list

print()
print()
print()

# 1.
def text(x):
    return f"The square of {x} is"

def square(x):
    return x * x

# Method 1
print(text(4), square(4), ".")
print()

# Method 2
print("The square of 4 is", square(4), ".")
print()

# Method 3
print(f"The square of 4 is {square(4)}.")

print()
print()
print()

# 2.

pastas = ["macaroni","bowtie","spaghetti"]

def eatPasta(pasta):
    return f"{pasta}"    

print(eatPasta(pastas))

