class Counter:
    count = 0  # atrybut klasy

    def __init__(self):
        Counter.count += 1

    def how_many(self):
        print(f"Liczba utworzonych obiektów: {Counter.count}")


# Test działania
if __name__ == "__main__":
    c1 = Counter()
    c1.how_many()

    c2 = Counter()
    c2.how_many()

    c3 = Counter()
    c3.how_many()
