import sys


def fibonacci(n):
    "Return n first elements of Fibonacci sequence"
    a = 0
    b = 1
    yield a
    if n > 1:
        yield b
    inc = 3
    while inc <= n:
        a, b = b, a+b
        yield b 
        inc += 1


def main():
    print("Add test cases here")
    for item in fibonacci(8):
        print(item)


if __name__ == "__main__":
    main() 