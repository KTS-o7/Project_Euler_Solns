t = int(input().strip())
answer=[]
index=0
for a0 in range(t):
    n = int(input().strip())
    term1 =1
    term2 = 1
    fib = term1+term2
    sumfib =0
    while(fib<n):
        if fib%2==0:
            sumfib = sumfib+fib
            
        
        term1=term2
        term2=fib
        fib=term1+term2
    answer.insert(index,sumfib) 
    
    index+=1

for i in range(t):
    print(answer[i])