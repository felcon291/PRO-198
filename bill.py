while True:
    total=0
    name=input("Name of the customer:")
    while True:
        print("Enter the cost and quantity of the item:")
        cost=float(input("Item cost:"))
        quantity=int(input("Quantity:"))
        total+=cost*quantity
        repeat=input("Do you want to add more items? (y/Y/n/N)")
        if repeat=="n" or repeat=="N":
            break
    print("_"*50)
    print("Name:",name)
    print("Total bill:",total)
    print()
    print("***Thank You for shopping with us***")
    print("_"*50)
    repeat=input("Next customer? (y/Y/n/N)")
    if repeat=="n" or repeat=="N":
        break