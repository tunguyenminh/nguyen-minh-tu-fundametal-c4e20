a = True
while a :
    Crud = input("Welcome to our shop, what do you want (C, R, U, D) ?")
    item = ["T-Shirts", "Sweater"]
    if Crud =="R":
        print ("Our item : ",end = "")
        print (*item, sep=", ")
    elif Crud == "C" :
        new = input("Enter new item: ")
        item.apend(new)
        print("Our items: ", end="")
        print(*items, sep=", ")
    elif Crud == "U":
        items.append(ni)
        p = int(input("Update position? ")) 
        b = input("New item? ")
        items[p-1] = b
        print("Our items: ", end="")
        print(*items, sep=", ")
    else:
        items.append(ni)
        items[1] = b
        d = int(input("Delete position? "))
        del items[d-1]
        print(*items, sep=", ")
