# === LISTS ===

fruits = ["apple", "banana", "cherry"]
print("First fruit:", fruits[0])
fruits.append("kiwi")
print("Updated list:", fruits)

# === DICTIONARIES ===

person = {
    "name": "Bob",
    "age": 30,
    "is_employed": True
}

print("Person's name:", person["name"])
person["city"] = "San Francisco"
print("Updated person:", person)

# Practice:
# 1. Create a list of 3 favorite movies
# 2. Create a dictionary for a car (brand, model, year)
# 3. Print a sentence like: "My car is a 2020 Toyota Corolla"


print()
print()
print()
print()
favmovies = ["You've Got Mail", "Pride & Prejudice"]
print("Favorite movie numero uno:", favmovies[0])
print()
favmovies.append("Parasite")
print("Favorite movies new and improved:", favmovies)
print()

car = {
    "brand": "Renault",
    "model": "Zoe",
    "year": 2021
}
print()
print(f"My favorite car is a {car["year"]} {car["brand"]} {car["model"]}.") 
print()
