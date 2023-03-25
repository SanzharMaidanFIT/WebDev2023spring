x = int(input())
count = 0
for i in range(x):
    if x % (i+1) == 0:
        count+=1

print(count)