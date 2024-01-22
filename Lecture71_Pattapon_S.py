menuName = []
menuPrice = []

def stroe():
    total = 0
    print("store".center(20,"-"))
    for i in range(len(menuPrice)):
        print(menuName[i],menuPrice[i])
        total += menuPrice[i]
    print("total",total)

while True:
    menu_name = input("Menu : ")
    if menu_name.lower() =="nope":
        print("Bye Bye")
        break
    else:
        menu_Price = int(input("price : "))
        menuName.append(menu_name)
        menuPrice.append(menu_Price)

stroe()

