

t = int(input().strip())
index = 0
answers = []
for a0 in range(t):
    n = int(input().strip())
    num = n-1
    n3 = (num)//3
    n5 = (num)//5
    n15 = (num)//15
    sum3 = n3*(n3+1)*3
    sum5 = n5*(n5+1)*5
    sum15 = n15*(n15+1)*15

    total = 0
    total = (sum3+sum5-sum15)//2

    answers.insert(index, total)
    index += 1

for i in range(0, t):
    print(answers[i])
