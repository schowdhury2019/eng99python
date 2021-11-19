info = {
    "name": None,
    "age" : None,
    "net_worth" : None
}

for i in info.keys():
    if info[i] == None:
        while info[i] == None:
            info[i] = input(f"Please enter a valid {i}: \n")

