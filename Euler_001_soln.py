

t = int(input().strip())
index = 0
answers = []
"""for a0 in range(t):
    n = int(input().strip())
    limit3 = n % 3
    if limit3 == 0:
        upper3 = n-3 

    else:
        upper3 = n-limit3
    #print("Limit of 3 is:",upper3)
    #
    a=int(upper3/3)
    sum3 = int(3*(a*(a+1)/2))
    #for i in range(1, int(upper3/3+1)):
        #sum3 += (3*i)
    #print("Sum of 3 is :",sum3)
    limit5 = n % 5
    if limit5 == 0:
        upper5 = n-5

    else:
        upper5 = n-limit5
    #print("Limit of 5 is:", upper5)
    #sum5 = 0
    a=int(upper5/5)
    sum5 = int(5*(a*(a+1)/2))
    
    #for i in range(1, int(upper5/5+1)):
     #   sum5 += (5*i)
    #print("Sum of 5 is :", sum5)
    limit15 = n % 15
    if limit15 == 0:
        upper15 = n-15

    else:
        upper15 = n-limit15
    #sum15 = 0
    a=int(upper15/15)
    sum15 = int(15*(a*(a+1)/2))
    #for i in range(1, int(upper15/15 + 1)):
        #sum15 += (15*i)
    #print("Sum of 15 is :", sum15)
    total = 0
    total = sum3+sum5-sum15
    
    
    answers.insert(index,total)
    index+=1"""

"""for a0 in range(t):
    n = int(input().strip())
    upper =n-1
    #print("Limit of 3 is:",upper3)
    #
    a=int(upper/3)
    sum3 = int(3*(a*(a+1)/2))
    #for i in range(1, int(upper3/3+1)):
        #sum3 += (3*i)
    #print("Sum of 3 is :",sum3)
   
    
    #print("Limit of 5 is:", upper5)
    #sum5 = 0
    a=int(upper/5)
    sum5 = int(5*(a*(a+1)/2))
    
    #for i in range(1, int(upper5/5+1)):
     #   sum5 += (5*i)
    #print("Sum of 5 is :", sum5)
   
    #sum15 = 0
    a=int(upper/15)
    sum15 = int(15*(a*(a+1)/2))
    #for i in range(1, int(upper15/15 + 1)):
        #sum15 += (15*i)
    #print("Sum of 15 is :", sum15)
    total = 0
    total = sum3+sum5-sum15
    
    
    answers.insert(index,total)
    index+=1"""

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
