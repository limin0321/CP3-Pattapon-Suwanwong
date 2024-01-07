def cal_tax():
    vat = int(input(": "))
    price = int(input(": "))
    result = ((vat/100)+1)*price 
    return result


def calcu_tax(real_price):
    real_vat = real_price + (real_price*0.07)
    return real_vat

real_price = int(input(": "))
print(calcu_tax(real_price))