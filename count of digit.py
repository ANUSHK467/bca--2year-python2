n = int(input("Enter an integer: "))
count = 0
num = abs(n)
while num > 0:
    count += 1
    num //= 10
if n == 0:
    count = 1
print(count)
