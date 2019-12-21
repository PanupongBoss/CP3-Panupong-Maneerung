usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "admin" and passwordInput == "2499":
    print("------------------------------------")
    print("      Wellcome To BB BooM Shop      ")
    print("------------------------------------")
    print("            Product Menu            ")
    print("------------------------------------")
    print("1. Cabbage    Price    50.-  (THB) ")
    print("2. Banana     Price    20.-  (THB) ")
    print("3. Coconut    Price    60.-  (THB) ")
    print("4. Lemon      Price    15.-  (THB) ")
    print("5. Fish       Price    100.- (THB) ")
    print("6. If you want to cancel your order")
    print("------------------------------------")
    userProducts = int(input("Please select products : "))   #เมนูสินค้าที่ต้องการ
    if userProducts == 1:
        amount1 = int(input("How many products do you want to buy ? >> : "))  # จำนวนที่ต้องการ
        sum1 = 50 * amount1
        print("------------------------------------")
        print("Total Price   : ", sum1, ".- (THB)")
        print("------------------------------------")
        print("         !!! Thank you !!!          ")
        print("------------------------------------")
    elif userProducts == 2:
        amount2 = int(input("How many products do you want to buy ? >> : "))  # จำนวนที่ต้องการ
        sum2 = 20 * amount2
        print("------------------------------------")
        print("Total Price  : ", sum2, ".- (THB)")
        print("------------------------------------")
        print("        !!! Thank you !!!          ")
        print("------------------------------------")
    elif userProducts == 3:
        amount3 = int(input("How many products do you want to buy ? >> : "))  # จำนวนที่ต้องการ
        sum3 = 60 * amount3
        print("------------------------------------")
        print("Total Price  : ", sum3, ".- (THB)")
        print("------------------------------------")
        print("        !!! Thank you !!!          ")
        print("------------------------------------")
    elif userProducts == 4:
        amount4 = int(input("How many products do you want to buy ? >> : "))  # จำนวนที่ต้องการ
        sum4 = 15 * amount4
        print("------------------------------------")
        print("Total Price  : ", sum4, ".- (THB)")
        print("------------------------------------")
        print("        !!! Thank you !!!          ")
        print("------------------------------------")
    elif userProducts == 5:
        amount5 = int(input("How many products do you want to buy ? >> : "))  # จำนวนที่ต้องการ
        sum5 = 100 * amount5
        print("------------------------------------")
        print("Total Price  : ", sum5, ".- (THB)")
        print("------------------------------------")
        print("        !!! Thank you !!!          ")
        print("------------------------------------")
    else:
        print("         See you again         ")
else:
    print("Login Error ! ")









