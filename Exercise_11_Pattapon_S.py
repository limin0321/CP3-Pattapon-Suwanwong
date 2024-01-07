number = int(input("your number : "))
i = 0
for x in range(number):
    print((number - x )* " " ,(i+1)*"*")
    i += 2