pricelist = []

def Store():
    total = 0
    for a,b in pricelist:
        total += b
    print("ยอดรวม : ",total)

while True: 
    menuName = input("what do you want: ")
    if menuName.lower() == "nope":
        print("ByeBye")
        break 
    else: 
        menuPrice = int(input("Price: "))
        pricelist.append([menuName,menuPrice])

Store()
