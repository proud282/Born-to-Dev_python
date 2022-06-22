#  Lecture 54 : ตัวอย่างการพัฒนาโปรแกรมรูปแบบฟังก์ชัน

def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = int(input(">>"))
    return userSelected

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

if login() == True:
    print(showMenu())
    if menuSelect() == 1:
        price = int(input("Price (THB) : "))
        print(vatCalculator(price))
    elif menuSelect() == 2:
        print(priceCalculator())
    else:
        print("Please select number 1 and 1 only")

else:
    print("Please Try Agian")
    login()

########################################
'''usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "admin" and passwordInput == "1234":
    print("Done !")
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    userSelected = int(input(">>"))
    if userSelected == 1:
        price = int(input("Price (THB) : "))
        vat = 7
        result = price + (price * vat / 100)
        print(result)
    elif userSelected == 2:
        price1 = int(input("First Product Price : "))
        price2 = int(input("Second Product Price : "))
        print(price1 + price2)'''

#login
#Show_Menu
#Select_Menu
#Vat
#Price
