"""insertion sort for quick"""
#가장 작은/큰 수부터 차례대로 찾는 방식
def insertion_sort(A,left,right):
    global Qc2, Qs2
    for i in range(left+1,right):
        j=i-1
        while j >= 0 and A[j] >A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
            Qs2+=1
            j-=1
            


"""insertion sort for merge"""
# #가장 작은/큰 수부터 차례대로 찾는 방식
# def insertion_sort2(A,left,right):
#     global Mc2, Ms2
#     for i in range(left+1,right):
#         j=i-1
#         while j >= 0 and A[j] >A[j+1]:
#             A[j], A[j+1] = A[j+1], A[j]
#             Ms2+=1
#             j-=1
            

            
"""
Quicksort algorithm is efficient if the size of the input is very large. 
But, insertion sort is more efficient than quick sort in case of small arrays as the number of comparisons and swaps are less compared to quicksort. 
So we combine the two algorithms to sort efficiently using both approaches.

퀵 정렬은 입력 크기가 정말 클 경우 효율적이지만 배열 크기가 작을 경우 삽입 정렬이 더 효과적이다.
비교와 교환 횟수가 더 적기 때문.

"""

"""Quick 정렬 mix"""	
def quick_sort2(A,first, last):  #first = 0, last = len(n)-1이 될 것이다.
    global Qc2, Qs2
    if first>=last: #first=0이므로 이 경우는 빈 리스트인 경우이다.
        return
    left,right=first+1,last     #빈 리스트가 아니라면 first에 1을 추가한다. 그 값을 left라는 변수에 저장한다. 추가적으로 right라는 변수에 마지막 인덱스를 저장한다.
    ## if first<last:            #필요 없는 비교
    
    if last-first+1 < 10:                 #비교 범위가 25 미만으로 줄어들었을 때 : insertion 정렬 적용
        Qc2+=1
        insertion_sort(A,first,last+1)   
    else:    
        
        p=A[first]  #피벗 값은 리스트의 첫번째에 있는 수이다.

        
        while left<=right:
            while left <= last and A[left]<p:   #left가 리스트 크기보다 작고 A[left]가 피벗 A[first]보다 작다면 
                left+=1                         #left에 1을 더한다.(비교 1회)
                Qc2+=1
            while right>first and A[right]>p:   #right이 first보다 크고 A[right]이 A[first]보다 크다면
                right-=1                        #right 에서 1을 뺀다.(비교 1회)
                Qc2+=1
            if left <=right:                    #만약 left보다 right이 크다? 서로 교환(교환 1회)
                A[left],A[right]=A[right],A[left]
                left+=1; right-=1;              #역시 left에 1을 더해주고 right에 1을 뺴줌
                Qs2+=1

            
        A[first],A[right]=A[right],A[first]
        Qs2+=1
        quick_sort2(A,first,right-1)
        quick_sort2(A,right+1,last)
    # return A


"""Merge 정렬 Mix"""
# def MergeTwoSortedLists2(A,first,last):
#     global Mc2, Ms2
#     m=(first+last)//2
#     i,j=first,m+1
#     B=[]
#     while i<=m and j<=last:
#         if A[i]<=A[j]:
#             B.append(A[i])
#             i+=1
#         else: 
#             B.append(A[j])
#             j+=1
#         Mc2+=1
#     for k in range(i,m+1):
#         B.append(A[k])
#     for k in range(j,last+1):
#         B.append(A[k])
#     for i in range(first,last+1):
#         A[i]=B[i-first]
#     Ms2+=2*(last-first) 

# def merge_sort2(A,first,last):
#     if first>=last:
#         return 
#     if last-first<10:
#         insertion_sort2(A,first,last+1)
#         print(A)
#     else:
#         merge_sort2(A,first,(first+last)//2)
#         merge_sort2(A,(first+last)//2+1,last)
#         MergeTwoSortedLists2(A,first,last)
#         # return A





import random, timeit
import pandas as pd
import matplotlib.pyplot as plt


# global Qc, Qs, Mc, Ms, Hc, Hs
##
## 여기에 세 가지 정렬함수를 위한 코드를...
##

"""Heap 정렬"""
def HeapifyDown(A,k,n):
    global Hc, Hs
    while 2*k+1<n:
        L,R=2*k+1,2*k+2
        if L<n and A[L]>A[k]:
            maxi=L
        else:
            maxi=k
        if R<n and A[R]>A[maxi]:
            maxi=R
        Hc+=2
        if maxi!=k:
            A[k],A[maxi]=A[maxi],A[k]
            Hs+=1
            k=maxi
        else:break

def make_heap(A):
    n=len(A)
    for k in range(n-1,-1,-1):
        HeapifyDown(A,k,n)


def heap_sort(A):
    global Hc, Hs
    make_heap(A)
    n=len(A)

    for i in range(len(A)-1,-1,-1):
        A[0],A[i]=A[i],A[0]
        Hs+=1
        n-=1
        HeapifyDown(A,0,n)
    # return A

	
"""Quick 정렬"""	
def quick_sort(A,first, last):
    global Qc, Qs
    if first>=last:
        return
    left,right=first+1,last
    p=A[first]
    while left<=right:
        while left <= last and A[left]<p:
            left+=1
            Qc+=1
        while right>first and A[right]>p:
            right-=1
            Qc+=1
        if left <=right:
            A[left],A[right]=A[right],A[left]
            left+=1; right-=1;
            Qs+=1
    A[first],A[right]=A[right],A[first]
    Qs+=1
    quick_sort(A,first,right-1)
    quick_sort(A,right+1,last)
    # return A

	

"""Merge 정렬"""
def MergeTwoSortedLists(A,first,last):
    global Mc, Ms
    m=(first+last)//2
    i,j=first,m+1
    B=[]
    while i<=m and j<=last:
        if A[i]<=A[j]:
            B.append(A[i])
            i+=1
        else: 
            B.append(A[j])
            j+=1
        Mc+=1
    for k in range(i,m+1):
        B.append(A[k])
    for k in range(j,last+1):
        B.append(A[k])
    for i in range(first,last+1):
        A[i]=B[i-first]
    Ms+=2*(last-first) #왜 이럴까? 이유를 모르면 사용할 수 없음
    #이유:

def merge_sort(A,first,last):
    if first>=last:
    
        return
    
    merge_sort(A,first,(first+last)//2)
    merge_sort(A,(first+last)//2+1,last)
    MergeTwoSortedLists(A,first,last)
    # return A
		
# 아래 코드는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음
#

def check_sorted(A):
	for i in range(n-1):
		if A[i] > A[i+1]: return False
	return True

#
# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
#
Qc, Qs, Mc, Ms, Hc, Hs, Qc2, Qs2, Mc2, Ms2 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0


N1=[]
A1,B1,C1,D1,E1=[],[],[],[],[]
for i in range(1,100000, 5000):
    n = i
    random.seed()
    A = []
    for i in range(n):
        A.append(random.randint(-1000,1000))
    B = A[:]
    C = A[:]
    D = A[:]
    # E = A[:]
        
        
        
    quick_sort(A, 0, n-1)
    # print("")
    # print("Quick sort:")
    # print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
    # print("  comparisons = {:10d}, swaps = {:10d}, total = {:10d}\n".format(Qc, Qs, Qc+Qs))
    A1.append(Qc+Qs)
    
    
    quick_sort2(D, 0, n-1)
    # print("Quick sort_mixed:")
    # print("time =", timeit.timeit("quick_sort2(D, 0, n-1)", globals=globals(), number=1))
    # print("  comparisons = {:10d}, swaps = {:10d}, total = {:10d}\n".format(Qc2, Qs2, Qc2+Qs2))
    D1.append(Qc2+Qs2)
    
    
    merge_sort(B, 0, n-1)
    # print("Merge sort:")
    # print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
    # print("  comparisons = {:10d}, moves = {:10d}, total = {:10d}\n".format(Mc, Ms, Mc+Ms))
    B1.append(Mc+Ms)
    
    
    heap_sort(C)
    # print("Heap sort:")
    # print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
    # print("  comparisons = {:10d}, swaps = {:10d}, total = {:10d}\n".format(Hc, Hs, Hc+Hs))
    C1.append(Hc+Hs)
    
    # # merge_sort2(E, 0, n-1)
    # print("Merge sort2:")
    # print("time =", timeit.timeit("merge_sort2(E, 0, n-1)", globals=globals(), number=1))
    # print("  comparisons = {:10d}, moves = {:10d}, total = {:10d}\n".format(Mc2, Ms2, Mc2+Ms2))
    # E1.append(Mc2+Ms2)
    
    N1.append(n)
    
assert(check_sorted(A))
assert(check_sorted(B))
assert(check_sorted(C))
assert(check_sorted(D))
# assert(check_sorted(E))
    

x_values = N1
Qs1 = A1
Qs2 = D1
Ms = B1
Ms2 = E1
Hs = C1


plt.plot(N1, A1)
plt.plot(N1, D1)
plt.plot(N1, B1)
# plt.plot(N1, E1)
plt.plot(N1, C1)
plt.legend(['Quick','Quick+Insertion','Merge','Heap'])
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Comparison between sortings")

plt.show()


