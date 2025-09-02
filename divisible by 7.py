a=int(input("enter the no:"))
if a%3==0 and a%10!=4:
    print("the no is divisible by 3 and last digit is not 4 ")
    if a%3==4 and a%10==0:
        print("the no is divisible by 3 and last digit is 4")
else:
    print("the no is not divisible by 3 and last digit is 4")