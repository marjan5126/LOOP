a = int(input())
sum = 0
while a>0:
    b = a%10
    sum += b
    a //= 10
print(sum)