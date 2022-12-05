def hcf(a,b):
    if a>b:
        num=a
        den=b
    else:
        num =b
        den = a
    ans = num%den
    if ans ==0:
        return den
    elif ans ==1:
        return 1
    else :
        return hcf(den,ans)


def findlcm(a,b):
    if a>b:
        return int((a*b)/hcf(a,b))
    else:
        return int((a*b)/hcf(b,a))
        

answers=[]
index=0
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    lcm = 1
    for i in range(2,n+1):
        lcm = findlcm(lcm,i)
    answers.insert(index,lcm)
    index+=1
    
for i in range(0,t):
    print(answers[i])