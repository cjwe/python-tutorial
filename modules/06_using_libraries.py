# === STANDARD LIBRARIES ===
import datetime

now = datetime.datetime.now()
print("Current time:", now.strftime("%Y-%m-%d %H:%M:%S"))
print()
print()

# Practice:
# 1. Import the `random` module
# 2. Use `random.choice()` to pick a random fruit from a list
# 3. Use `random.randint(1, 100)` to simulate a dice roll

# 1. 
import random

# 2.
fruits = ["grape", "banana", "cherry", "passion fruit", "pineapple", "orange", "blueberry", "melon"]
eatMe = random.choice(fruits)
print(f"I would love to eat a {eatMe}.")
print()
print()

# 3.
feelinLucky = random.randint(2,12)
print(f"I rolled a {feelinLucky}.")
print()

# Grade 9/10