import iterators
import pytest

class TestFibonacci:
    expected = [0, 1, 1, 2, 3, 5, 8, 13]
    count = len(expected)

    def test_fibonacci(self):
        actual = [number for number in iterators.Fibonacci(self.count)]
        assert actual == self.expected


    def test_fibonacci_next(self):
        fib = iterators.Fibonacci(self.count)
        for item in range(self.count):
            assert next(fib) == self.expected[item] 
    

    def test_fibonacci_next_stop_iteration(self):
        with pytest.raises(StopIteration):
            fib = iterators.Fibonacci(self.count)
            for item in range(self.count+1):
                assert next(fib) == self.expected[item] 
    




