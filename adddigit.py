//esai
num = int(input())
result = 0
hold = num
while num > 0:
    rem = num % 10
    result = result + rem
    num = int(num/10)
print(result)
