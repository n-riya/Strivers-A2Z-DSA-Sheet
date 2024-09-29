# def triangle( n:int) ->None:
#     for i in range(1,n+1):
#         print((str(i)+' ') * i)

def triangle( n:int) ->None:
    for i in range(1,n+1):
        for j in range(i):
            print(i, end=' ')
        print()

n = 5
triangle(n)