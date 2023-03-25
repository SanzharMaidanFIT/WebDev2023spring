n = int(input())
power = True
while n > 1:
    if n % 2 != 0:
        power = False
        break
    n = n // 2
if power:
    print("YES")
else:
    print("NO")