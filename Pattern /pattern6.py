def nNumberTriangle(n: int) -> None:
    for i in range(n+1):
        for j in range(1,n-i+1):
            print(j, end=' ')
        print()

n = 5
nNumberTriangle(n)