# === CLASSES ===

class Animal:
    """ This is an Animal. """
    
    def __init__(self, name):
        self.name = name

    def speak(self):
        """
        This is an example of a doctring.
        """

        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        super().speak()
        print(f"{self.name} barks!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows!")

dog = Dog("Rex")
cat = Cat("Whiskers")

dog.speak()
cat.speak()
print()
print()
# Practice:
# 1. Create a class `Person` with `name` and `age` attributes
# 2. Add a method `introduce()` that prints: "Hi, I'm [name], and I'm [age] years old."
# 3. Create a class `Student` that inherits from `Person`, and add a `grade` attribute

# 1. 

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age 

    def introduce(self):
        intro = f"Hi, I'm {self.name}, and I'm {self.age} years old."
        print(intro)

person1 = Person("Christa", 30)
person1.introduce()
print()
print()

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    
    def introduce(self):
        super().introduce()
        intro = f"I'm in the {self.grade}."
        print(intro)

student1 = Student("Creestah", 30, "12th Grade")
student1.introduce()
print()
print()

student2 = Student("Vladino", 37, "12th Grade")
student2.introduce()
print()
print()

# Grade 10/10
