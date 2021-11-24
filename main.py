a = 5
b = a
b += 5


print(a,b)


x = [
    {'item': 'Risotto', 'price': 12.5, 'quantity': 2},
    {'item': 'Burrito', 'price': 20.43, 'quantity': 4}
]

print("x: ", x[0])

y = x[0]

y["quantity"] += 10

print("x: ",x[0])
print("y: ",y)

i = [1,2,3]
j = i[0]

j += 10

print(i, j)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
