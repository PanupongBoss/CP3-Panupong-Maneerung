userinput = int(input("Enter your number : "))
def vatcalculate(totalprice):
    result = totalprice+(totalprice*7/100)
    return result
print(vatcalculate(userinput))