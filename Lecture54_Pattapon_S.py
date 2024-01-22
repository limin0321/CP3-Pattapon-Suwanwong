def login():

    for x in range(3):

        userName = input("username :")
        password = input("password : ")

        if userName == "admin" and password == "123456":
            print("Passed")
            return True
        
        elif userName != "admin" or password != "123456":
            print("Not Passed")

    else:
        print("BLOCK")


def MenuShow():
    print('''    ______SHOP
          
          1.VatCalculator >> 1
          
          2.PriceCalculator >> 2''')
    

def SelectMenu():
    urSelect = int(input("SERVICE : "))
    return urSelect


def VatCalculator(price):
    vat = 0.07
    return price + (price*vat)

def PriceCalculator():
    price1 = int(input("Firsrt_Price : "))
    price2 = int(input("Second_Price : "))
    return price1 + price2

def __Shop():
    if login():
        MenuShow()
        select_Service = SelectMenu()
        if select_Service == 1 :
            price_t = int(input("Price : "))
            print(VatCalculator(price_t))
        elif select_Service == 2 :
            print(PriceCalculator())

__Shop()