a=int(input("enter the no:"))
if a%7==0 and a%5!=4:
    print("the no is divisible by 7 and last digit is not 5 ")
    if a%7==4 and a%5==0:
        print("the no is divisible by 7 and last digit is 5")
else:
    print("the no is not divisible by 7 and last digit is 5")