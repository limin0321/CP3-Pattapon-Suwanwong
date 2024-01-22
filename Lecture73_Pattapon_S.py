#กรอกแค่ชื่ออาหาร จะรวมราคาให้เลย

menulist = {"a":10, "b":20,"c":30}
menuName = []

def stroe():
    total = 0
    print("store".center(20,"-"))
    for i,e in menuName:
        print(i,e)
        total += e
    print("total : ",total)



while True:
    menu_name = input("What u want? : ")
    if menu_name.lower() == "np":
        print("exit")
        break 
    else: 
        menuName.append([menu_name,menulist[menu_name]])

stroe()