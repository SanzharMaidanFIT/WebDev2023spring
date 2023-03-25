if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

if __name__ == '__main__':
    n = int(input())
for i in range(n):
    print(i*i)

def is_leap(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
year = int(input())
print(is_leap(year))

if __name__ == '__main__':
    n = int(input())
for i in range(1, n+1):
    print(str(i), end='')
print()

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
s=set()
for i in arr:
    s.add(i)
s.remove(max(s))
print(max(s))

def swap_case(s):
    swapped_s = s.swapcase()
    return(swapped_s)
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

def split_and_join(line): 
    return line.replace(' ', '-')  
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

def print_full_name(first, last):
    print(f'Hello {first} {last}! You just delved into python.')

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)