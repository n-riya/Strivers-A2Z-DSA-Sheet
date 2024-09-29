# def nStarTriangle(n: int) -> None:
#     a = n-1
#     for i in range(1,n*2,2):
#         print(" "* a +"*" * i)
#         a -= 1

def nStarTriangle(n: int) -> None:
    for i in range(n):
        #space
        for x in range(n-i-1):
            print(" ", end='')
        
        #star
        for y in range(2*i+1):
            print("*", end='')
        print()
n = 5
nStarTriangle(n)