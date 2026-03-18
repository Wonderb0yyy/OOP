class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height

# Sprawdzenie działania
if __name__ == "__main__":
    rect = Rectangle(5, 10)
    print(f"Boki prostokąta: {rect.width} x {rect.height}")
    print(f"Pole: {rect.area()}")
    print(f"Obwód: {rect.perimeter()}")
