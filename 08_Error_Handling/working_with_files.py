# file = open("order.txt")
#
# with open("order.txt","r") as file:
#     lines = file.read().splitlines()
#     print(lines)
#     for i in lines:
#         print(i)

# file.close()

try:

    with open("order.txt","r") as file:
        print(file, type(file))
        orders = file.read().split("\n")

    # file.close()

except FileNotFoundError as err:
    print(err)
    # raise # stops the rest of the code from running
finally:
    print("A: Always do this, whatever happens")

print(orders)

with open("tickets.txt","a") as file:       #for append - adds without overwriting

    for order in orders:
        file.write(f"One {order} coming right up!\n")

# a - append
# x - exclusive: fails if file exists
# + -