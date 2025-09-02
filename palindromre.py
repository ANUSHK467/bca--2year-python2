a = int(input("Enter an integer: "))
original = a
reverse = 0
num = a
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
if original == reverse:
    print("Yes")
else:
    print("No")
