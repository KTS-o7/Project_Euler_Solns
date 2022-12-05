def summer(num):
    total = 0
    while (num > 0):
        total += num % 10
        num = num//10
    print(total)


t = int(input())
for i in range(0, t):
    n = int(input())
    num = pow(2, n)

    summer(num)
