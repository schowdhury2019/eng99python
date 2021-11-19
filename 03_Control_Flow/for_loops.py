
numbers = [x for x in range(1,11)]

print(numbers)

menu = [
    {"food":"pizza", "price": 13.00},
    {"food":"ice-cream", "price": 121.00},
    {"food":"stake", "price": 1.00},
    {"food":"lobster", "price": 5.00},
    {"food":"ramen", "price": 8.00}
]

total = 0
for i in menu:
    total += i.get("price") if i.get("price") else 0

print(f"Total price: {total}")

matrix = []
for x in range(1,3):
    for y in range(1,3):
        matrix.append([x,y])

print(matrix)
