class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Hau!")

# Tworzenie obiektu
my_dog = Dog("Burek", 3)

# Wywołanie metody
my_dog.bark()
