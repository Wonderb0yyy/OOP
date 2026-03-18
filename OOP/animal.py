class Animal:
    def make_sound(self):
        print("Zwierzę daje głos")

class Cat(Animal):
    def make_sound(self):
        print("Miau!")

class Cow(Animal):
    def make_sound(self):
        print("Muu!")

# Test działania
if __name__ == "__main__":
    animals = [Animal(), Cat(), Cow()]
    for animal in animals:
        animal.make_sound()
