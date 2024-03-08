a = int(input())
num = a
cnt = 0
sum = 0
while a>0:
    cnt +=1
    a = a//10
print(cnt)
a = num
for i in range (cnt):
    b = a%10
    sum = sum + (b**cnt)
    a = a//10

print(sum)
if sum == num:
    print('Armstrong Number')
else:
    print('Not Armstrong Number')