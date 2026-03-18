class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        print(f"Książka: '{self.title}', autor: {self.author}")

# Sprawdzenie działania (opcjonalne, ale przydatne)
if __name__ == "__main__":
    my_book = Book("Władca Pierścieni", "J.R.R. Tolkien")
    my_book.describe()
