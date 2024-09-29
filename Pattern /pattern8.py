# def nStarTriangle(n: int) -> None:
#     s = 0
#     for i in range(1,2*n,2):
#         print(" "* s+"*"*((2*n)-i))
#         s += 1

def nStarTriangle(n: int) -> None:
    for i in range(n):
        #space
        for x in range(i+1):
            print(" ", end='')
        
        #star
        for y in range(2*n-i*2-1):
            print("*", end='')

        print()

n = 5
nStarTriangle(n)
