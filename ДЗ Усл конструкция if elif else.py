
def numbers(a, b, c):
    if a != b and a != c and b != c:
        result = 0
    elif a == b and a == c and b == c:
        result = 3
    else:
        result = 2
    print(result)

numbers(3,1,1)

