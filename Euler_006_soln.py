if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        sumsqr = ((n*(n+1))/2)**2
        sqrsum = (n*(n+1)*(2*n+1))/6
        print(int(sumsqr-sqrsum))
