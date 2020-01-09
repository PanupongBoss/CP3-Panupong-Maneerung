menuList = []
priceList = []
def showBill():
    print("My Food".center(21,"-"))
    for number in range(len(menuList)):
        print(menuList[number],priceList[number],".-")
    print("-".center(21,"-"))
    print("Total : ", sum(priceList),".-")
    print("-".center(21, "-"))
while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
