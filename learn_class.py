class Dog:
    def __init__(self, name, age):
        self.name = name   # attribute
        self.age = age     # attribute

    def bark(self):       # method
        print("Woof!")

my_dog = Dog("Buddy", 3)
print(my_dog.name)  # Buddy
my_dog.bark()       # Woof!