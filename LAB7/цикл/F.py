x = int(input())
reverse = 0
while x > 0:
    reverse = reverse * 10 + x % 10
    x //= 10
print(reverse)