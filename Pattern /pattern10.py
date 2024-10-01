def nStarTriangle(n: int) -> None:
    # for i in range(1,n):
    #     print("*" * i)
    
    # print("*" * n)

    # for i in range(n-1,0,-1):
    #     print("*" * i)

    for i in range(1,2*n+1):
        star = i
        if(i> n):
            star = 2 * n - i
        for j in range(1,star+1):
            print("*", end='')
        print()

n = 5
nStarTriangle(n)