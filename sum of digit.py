n = int(input("Enter a number: "))
total = 0
num = abs(n)   # handle negative numbers too
while num > 0:
    total += num % 10
    num //= 10
print(total)
