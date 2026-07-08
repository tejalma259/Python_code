# A small, clean calculator utility.
# Four basic operations, each in its own function.


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # Guard against dividing by zero, which is undefined and would crash.
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b


if __name__ == "__main__":
    x = 10
    y = 5

    print("Addition:", add(x, y))
    print("Subtraction:", subtract(x, y))
    print("Multiplication:", multiply(x, y))
    print("Division:", divide(x, y))
