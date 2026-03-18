class Counter:
    count = 0  # atrybut klasy

    def __init__(self):
        Counter.count += 1

    @classmethod
    def how_many(cls):
        print(f"Liczba utworzonych obiektów: {cls.count}")

# Test działania
if __name__ == "__main__":
    Counter.how_many()
    c1 = Counter()
    c2 = Counter()
    Counter.how_many()
    c3 = Counter()
    Counter.how_many()
