#โปรแกรมสำหรับขายผลไม้ เลือกสินค้า สรุปยอดราคา
userName = input("ID : ")
passWord = input("Password : ")
if userName == "Naomi" and passWord == "123456":
    print('''
            Hi,Naomi Welcome to My Fruit Shop
                 ----------------------
            What kind of fruit would you like?
                            .
        Our store has the following list of fruits.
                ---------------------------
                    1.Apple : 20 THB         
          
                    2.Mango : 65 THB

                    3.Orange : 45 THB
        ''')
    fruit = input("What kind of fruit would you like? : ")
    if fruit == "Apple":
        num_1 = 20
        calcu = input("How many pieces? : ")
        result = num_1 * 1.07 *float(calcu)
        print("Summary(THB): ",result)
    elif fruit == "Mango":
        num_2 = 65
        calcu = input("How many pieces? : ")
        result_2 = num_2 * 1.07 *float(calcu)
        print("Summary(THB): ",result_2)
    elif fruit == "Orange":
        num_3 = 45
        calcu = input("How many pieces? : ")
        result_3 = num_3 * 1.07 *float(calcu)
        print("Summary(THB): ",result_3)
    else:
        print("Bye bye")