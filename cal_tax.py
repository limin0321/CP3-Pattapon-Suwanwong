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
        print("Price + Tax",urPice*0.07+urPice)
    elif Tax == "2":
        Pri_1 = int(input("First Price : "))
        Pri_2 = int(input("Second Price : "))
        print(Pri_1 + Pri_2)