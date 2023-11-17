userName = input("USERNAME : ")
passWord = input("Password : ")
if userName == "admin" and passWord == "1234":
    print("Welcome To my Service")
    print('''
          Tax Calculator = 1
          ---------------
          Price Calculator = 2
''')
    Tax = input("Tax/Price : ")
    if Tax == "1":
        urPice = int(input("Price : "))
        print("Price + Tax = ",urPice*0.07+urPice)
    elif Tax == "2":
        Pri_1 = int(input("First Price : "))
        Pri_2 = int(input("Second Price : "))
        print(Pri_1 + Pri_2)
elif userName == "Guest" and passWord == "0000":
    the_price = int(input("first price : "))
    the_Secprice = int(input("Second price : "))
    the_Thirdprice = int(input("Third price : "))
    print("sum = ",the_price + the_Secprice + the_Thirdprice)
elif userName == "abc" or passWord == "Sawasdee":
    num_1 = int(input("origin.one : "))
    num_2 = int(input("origin.two : "))
    num_3 = int(input("origin.three : "))
    num_4 = int(input("origin.four : "))
    num_5 = int(input("origin.five : "))
    num_6 = int(input("origin.six : "))
    num_7 = int(input("origin.seven : "))
    num_8 = int(input("origin.eight: "))
    print("sum_se",num_1*num_2*num_3*num_4*num_5*num_6*num_7*num_8)
else:
    print("Bye Bye")