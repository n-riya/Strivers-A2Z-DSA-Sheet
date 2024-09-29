def right_tri_with_no(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=' ')
        print()

n  = 5
right_tri_with_no(n)