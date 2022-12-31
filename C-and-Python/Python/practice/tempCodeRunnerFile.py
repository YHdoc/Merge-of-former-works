def BS(A,a,b,x):
    if a>b: return None
    m=(a+b)//2
    if x<A[m]: return BS(A,a,m-1,x)
    elif x>A[m]: return BS(A,m+1,b,x)
    else: return m


def do_something(A,k):
    A.sort()
    for x in A:
        if BS(A,0,len(A),k-x) == True: return True
        print(k-x)
    return False


A=[3, 6, 9, 11 ,12, 18, 10, 2, 5, 1]
for i in range(10):
    print(do_something(A,i))
    