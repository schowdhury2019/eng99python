# Don't
# Repeat
# Yourself

def multiply_numbers(args : tuple) -> int:
    product = 1
    for i in args:
        product *= i

    return product

def divide_by_two(num : int) -> int:
    return num//2

def composite(func1, func2, *args: int) -> int:
    return func2(func1(args))

# print(composite(multiply_numbers,divide_by_two, 2,4,6,2))

def q1a(n : int) -> [int]:
    ans = []
    for i in range(1,n+1):
        if n % i == 0:
            ans.append(i)
    return ans

def q1b(x : int,y : int) -> bool:
    if x == y:
        return True
    if x < y:
        x,y = y,x
    if x % y == 0:
        return True
    return False

# --------------------------------------- #

def q2a(char:str) -> int:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

    return alphabet.index(char)

def q2b(name:str) -> str:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

    ID = ""
    for i in name:
        ID += str(alphabet.index(i))
    return ID

def q2c(name:str) -> int:
    ID = q2b(name)

    total = 0
    for i in ID:
        total += int(i)

    return int(ID) - total


def q3a(num):
    for i in range(1, num+1):
        count = 1
        for j in range(2, i+1):
            if i%j == 0:
                count =j
                break

        print(count)

print(q3a(100))





