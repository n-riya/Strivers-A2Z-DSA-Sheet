def nStarDiamond(n: int) -> None:
    c = n-1
    for i in range(n):
        print(' ' * c + '*' * (i*2+1))
        c -= 1

    for i in range(n):
        c += 1
        print(' ' * c +'*' * ( (2*n-1)-(i*2)))

n = 5
nStarDiamond(n)