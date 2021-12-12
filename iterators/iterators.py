class Fibonacci:
    """Generate n first fibonacci numbers"""
    def __init__(self, n):
        """Initialize object at creation"""
        self.a = 0
        self.b = 1
        self.n = n
        self.count = 1

    def __iter__(self):
        """
        Return an object itself but as an iterator.
        Make it possible to use object in 'for' and 'in' statements
        """
        return self

    def __next__(self):
        """Return the next value"""
        if self.count > self.n:
            raise StopIteration
        if self.count == 1:
            self.count += 1
            return 0
        if self.n == 2:
            self.count += 1
            return 1
        self.a, self.b = self.b, self.a + self.b
        self.count += 1 
        return self.a

def main():
    pass

if __name__ == "__main__":
    main() 