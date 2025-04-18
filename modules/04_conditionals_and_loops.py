# === CONDITIONALS ===

age = 20

if age >= 18:
    print("You're an adult.")
elif age >= 10:
    print("You're a teenager.")
else:
    print("You're a minor.")
print()
print()

# === LOOPS ===

print("Counting with for loop:")
for i in range(5):
    print(i)

print("Counting with while loop:")
count = 0
while count < 3:
    print(count)
    count += 1
print()
print()

# Practice:
# 1. Write a for loop that prints every number from 1 to 10
# 2. Write a while loop that stops when a counter reaches 5
# 3. Write an if-else to check if a number is even or odd


# 1. Use range function with start and stop 
print("For loop counting:")
for i in range(1,11):
    print(i)
print()
print()

# 2. 
print("Counting with while loop:")
count = 0
while count <= 5:
    print(count)
    count += 1
print()
print()

# 3.
number = 47631
print("Is it even even?")
if number % 2 == 0:
    print(f"{number} is even even!")
else: 
    print(f"{number} is an odd ball.")
print()
print()

# Vlad fun addition
def is_even(number):
    print("Is it even even?")
    print()
    print("I guess we'll find out..")
    print()
    print("Looks like..")
    if number % 2 == 0:
        print(f"{number} is even even!")
    else: 
        print(f"{number} is an odd ball.")

is_even(47631)
print()
is_even(47632)


# Grade 10/10