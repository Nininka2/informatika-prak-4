def hello():
    print("Привет из ветки conflict!")


hello()
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


print("2 + 3 =", add(2, 3))
print("5 - 2 =", subtract(5, 2))
def multiply(a, b):
    return a * b


print("4 * 5 =", multiply(4, 5))