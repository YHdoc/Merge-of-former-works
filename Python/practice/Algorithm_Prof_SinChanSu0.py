
# ?옱洹?1.?옱洹?瑜? ?씠?슜?븳 a遺??꽣 b源뚯???쓽 ?닽?옄 ?뜑?븯湲?
# def sum(a,b):
#     if a>b: return 0
#     elif a==b: return a #諛붾떏議곌굔
#     m=(a+b)//2
#     return sum(a,m) + sum(m+1,b)
# a,b = tuple(map(int, input("?닽?옄瑜? ?엯?젰?븯?꽭?슂: ").split()))
# print(sum(a,b))


#?옱洹?2.?옱洹?瑜? ?씠?슜?븳 ?뙥?넗由ъ뼹 援ы쁽
# def factorial(n):
#     if n==1: return n
#     else: return n*factorial(n-1)
# a = int(input("?닽?옄= "))
# print(factorial(a))


#?옱洹?3.list A?뿉 ?엳?뒗 媛??옣 ?겙 ?닔瑜? 李얜뒗 ?옱洹??븿?닔 find_max(A,n)
# def find_max1(A,n):
#     minA = A[0]
#     for i in range(n):
#         if minA > A[i]: minA = A[i]
#     return minA


# def find_max2(A,n):
#     if n<=1 or len(A) == 1: return A
#     else:
#         if A[n-1]>
# 紐삵???뼱?꽌 ?씪?떒 ?뒪?궢

#鍮꾩옱洹? reverse ?뿰?궛

# def reverse(A):
#     n, i = len(A), 0
#     while i < (n//2):
#         A[i], A[n-1-i] = A[n-1-i], A[i]
#         i += 1

# A = list(input())  # 臾몄옄?뿴?쓣 ?엯?젰諛쏆븘 由ъ뒪?듃濡? 蹂??솚
# reverse(A)
# print(''.join(str(x) for x in A))

# def reverse(L, a):
#     n = len(L)
#     if a < n//2:
#         L[a], L[n-a-1] = L[n-a-1], L[a]
#         print(L)
#         reverse(L, a+1)



# L = list(input())  # 臾몄옄?뿴?쓣 ?엯?젰諛쏆븘 由ъ뒪?듃濡? 蹂??솚
# reverse(L, 0)
# print(''.join(str(x) for x in L))



# prefixSum ?몢 媛?吏? 踰꾩쟾
# import time, random

# def prefixSum1(X,n):
#     S = [0]*n
#     before_t = time.process_time()
#     for i in range(n):
#         for j in range(i+1):
#             S[i]+=X[j]
#     return time.process_time()-before_t

# def prefixSum2(X,n):
#     before_t = time.process_time()
#     S = [0]*n
#     S[0] = X[0]
#     for i in range(1,n):
#         S[i]=S[i-1]+X[i]
#     return time.process_time()-before_t

# random.seed()
# n = int(input())
# X = [random.randint(-999,999) for i in range(n)]
# # X=[3,1,-2,6,7]
# print("prefixSum1?쓽 ?닔?뻾?떆媛? : %.15lf" %prefixSum1(X,n))
# print("prefixSum2?쓽 ?닔?뻾?떆媛? : %.15lf" %prefixSum2(X,n))
# # print(X)




# Select - "Quick_select"
# def QuickSelect(List, num):
#     if(len(List)==0): return
#     print(List)
#     pivot=List[len(List)//2]
#     A,M,B=[],[],[]
#     for i in List:
#         if i<pivot: A.append(i)
#         elif i>pivot: B.append(i)
#         else: M.append(i)
#     if len(A)>num: return QuickSelect(A,num)
#     elif len(A)+len(M)<num: return QuickSelect(B,num-len(A)-len(M))
#     else: return pivot
# n,k = tuple(map(int,input().split()))
# L = list(map(int, input().split()))
# print(QuickSelect(L,k))


# def QuickSelect(List, num):
#     List.sort()
#     if len(List)==0: return
#     pivot=List[len(List)//2-1]
#     A,M,B=[],[],[]
#     for i in List:
#         if i<pivot: A.append(i)
#         elif i>pivot: B.append(i)
#         else: M.append(i)
#     if len(A)>num: return QuickSelect(A,num)
#     elif len(A)+len(M)<num: return QuickSelect(B,num-len(A)-len(M))
#     else: return pivot

# n,k = tuple(map(int,input().split()))
# L = list(map(int, input().split()))
# print(QuickSelect(L,k))





# ===============================================

# #MoM ?븣怨좊━利?

# def find_median_five(listA):
#     if len(listA)==0: return
#     piv=listA[len(listA)//2]
#     A,M,B=[],[],[]
#     for i in listA:
#         if i<piv: A.append(i)
#         elif i>piv: B.append(i)
#         else: M.append(i)
#     listB=A+M+B
#     return min(listB)

# # # A=[5,1,4,2,3]
# # # print(find_median_five(A))
# def MoM(A, k): # L?쓽 媛? 以묒뿉?꽌 k踰덉㎏濡? ?옉??? ?닔 由ы꽩
#     if len(A) == 1: # no more recursion
#         return A[0]
#     i = 0
#     S, M, L, medians = [], [], [], []
#     while i+4 < len(A): 
#         medians.append(find_median_five(A[i: i+5]))
#         i+=4
#     if i < len(A) and i+4 >= len(A): medians.append(find_median_five(A[i:]))
#     mom = MoM(medians,k)
#     for v in A:
#         if v < mom: S.append(v)
#         elif v > mom: L.append(v)			
#         else: M.append(v)
#     if  k<len(S): return MoM(S,k)
#     elif k>len(S)+len(M): return MoM(L,k-len(S)-len(M))
#     else: return mom

# # # n怨? k瑜? ?엯?젰?쓽 泥? 以꾩뿉?꽌 ?씫?뼱?뱾?씤?떎
# # # n媛쒖쓽 ?젙?닔瑜? ?씫?뼱?뱾?씤?떎. (split ?씠?슜 + int濡? 蹂??솚)
# n,k=map(int,input().split())
# A=list(map(int,input().split()))
# print(MoM(A, k))



# ===============================================



#?옓_?뒳?젆?뀡

# import heapq
# def find_min(Alist):
#     if len(Alist)==0: return None
#     return Alist[0]
# def solve(A, k): 
#     #諛⑹떇4
#     #?옓?뿉 ?엳?뒗 理쒖넖媛믪쓣 李⑤?????濡? ?깉濡쒖슫 諛곗뿴?뿉 ?꽔?뼱二쇰㈃?꽌 ?궘?젣
#     #?궘?젣?릺?뼱?룄 ?옓 ?꽦吏덉쓣 ?쑀吏??빐?빞 ?븿?뿉 ?쑀?쓽
#     NewL = list()
#     while len(A) != 0:
#         a=find_min(A)
#         NewL.append(a)
#         A.pop(0)
#         heapq.heapify(A)    #O(n) ?떆媛꾩씠 嫄몃┛?떎=>O(logn)?씠 ?릺?룄濡? 留뚮뱾?뼱二쇱뼱?빞 ?븿.
#     print(NewL)
#     return NewL[k-1]    #?씤?뜳?뒪媛? 0遺??꽣 ?엳?쑝誘?濡? 1?쓣 鍮쇱???떎.
# k = int(input())
# A = [int(x) for x in input().split()]
# heapq.heapify(A) # A is now a min-heap
# print(solve(A, k))



# import heapq
# def HeapifyDown(A,k,n):
#     while 2*k+1<n:
#         L,R=2*k+1,2*k+2
#         if L<n and A[L]<A[k]:m=L
#         else: m=k
#         if R<n and A[R]<A[m]:m=R
#         if m!=k:
#             A[k],A[m]=A[m],A[k]
#             k=m
#         else: break
    
    # i=0
    # while i*2+1 < len(A)-2:
    #     L,R = i*2+1, i*2+2
        
    #     if A[0]>A[i*2+1]: A[0],A[i*2+1] = A[i*2+1],A[0]
    #     elif A[i*2+1]==A[i*2+2]:A[i*2+1]==A[i*2+2]
    #     elif A[i*2+2]<A[i*2+1]: A[i*2+2],A[i*2+1]=A[i*2+1],A[i*2+2]
    #     i+=1


# def HeapifyDown(Alist):
#     IDX=0
#     a=0
#     while IDX*2+1<len(A)-1:
#         L,R=IDX*2+1,IDX*2+2
#         if L<A[IDX]:
#             if R<A[IDX]:
#                 if L<R : a=R
#                 else: a=L
#             else: a=L
#         else: break
#         A[IDX],A[a]=A[a],A[IDX]
#         IDX+=1


# def find_min(Alist):
#     if len(Alist)==0: return None
#     return Alist[0]


# import heapq
# def HeapifyDown(A,k):
#     while 2*k+1<len(A):
#         L,R=2*k+1,2*k+2
#         if L<len(A) and A[L]<A[k]:m=L
#         else: m=k
#         if R<len(A) and A[R]<A[m]:m=R
#         if m!=k:
#             A[k],A[m]=A[m],A[k]
#             k=m
#         else: break    


# def solve(A, k): 
#     #諛⑹떇4
#     #?옓?뿉 ?엳?뒗 理쒖넖媛믪쓣 李⑤?????濡? ?깉濡쒖슫 諛곗뿴?뿉 ?꽔?뼱二쇰㈃?꽌 ?궘?젣
#     #?궘?젣?릺?뼱?룄 ?옓 ?꽦吏덉쓣 ?쑀吏??빐?빞 ?븿?뿉 ?쑀?쓽
#     NewL = list()
#     while len(A) != 0:
#         # a=find_min(A)
#         NewL.append(A[0])
#         A[0],A[len(A)-1]=A[len(A)-1],A[0] #理쒖넖媛믨낵 理쒕뙎媛? ?쐞移섎?? ?뒪?솑?빐以??떎(?엳?뵾?뙆?씠 ?떎?슫 ?뿰?궛?쓣 ?쐞?빐)
#         # A.pop(0)
#         A.pop()
#         # HeapifyDown(A,0,len(A))    #O(n) ?떆媛꾩씠 嫄몃┛?떎=>O(logn)?씠 ?릺?룄濡? 留뚮뱾?뼱二쇱뼱?빞 ?븿.
#         HeapifyDown(A,0) 
#         # HeapifyDown(A)
#         # print(A)
#     print(NewL)
#     return NewL[k-1]    #?씤?뜳?뒪媛? 0遺??꽣 ?엳?쑝誘?濡? 1?쓣 鍮쇱???떎.


# k = int(input())
# A = [int(x) for x in input().split()]
# heapq.heapify(A) # A is now a min-heap
# print(A)
# print(solve(A, k))





# =============================================================
# 怨쇱젣4. median, 理쒕?? 援ш컙 ?빀



# import sys
# import heapq
# input = sys.stdin.readline

# # def QuickS(ListA):
# #     if len(ListA)<2: return ListA
# #     piv=ListA[len(ListA)//2]
# #     left,right,middle=[],[],[]
# #     for i in ListA:
# #         if i<piv : left.append(i)
# #         elif i>piv : right.append(i)
# #         else: middle.append(i)
# #     return QuickS(left)+middle+QuickS(right)



# def HeapifyDown(A,k):
#     while 2*k+1<len(A):
#         L,R=2*k+1,2*k+2
#         if L<len(A) and A[L]<A[k]:m=L
#         else: m=k
#         if R<len(A) and A[R]<A[m]:m=R
#         if m!=k:
#             A[k],A[m]=A[m],A[k]
#             k=m
#         else: break  


# def HeapS(A):
#     #諛⑹떇4
#     #?옓?뿉 ?엳?뒗 理쒖넖媛믪쓣 李⑤?????濡? ?깉濡쒖슫 諛곗뿴?뿉 ?꽔?뼱二쇰㈃?꽌 ?궘?젣
#     #?궘?젣?릺?뼱?룄 ?옓 ?꽦吏덉쓣 ?쑀吏??빐?빞 ?븿?뿉 ?쑀?쓽
#     NewL = list()
#     while len(A) != 0:
#         NewL.append(A[0])
#         A[0],A[len(A)-1]=A[len(A)-1],A[0] #理쒖넖媛믨낵 理쒕뙎媛? ?쐞移섎?? ?뒪?솑?빐以??떎(?엳?뵾?뙆?씠 ?떎?슫 ?뿰?궛?쓣 ?쐞?빐)
#         A.pop()
#         HeapifyDown(A,0) 
#     return NewL
    


# sum,i = 0,0

# A=list(map(int,input().split()))

# while (i<len(A)):
#     ListA=A[:i+1]
#     heapq.heapify(ListA)
#     ListA=HeapS(ListA)
#     print(ListA)
#     median = ListA[((len(ListA)+1)//2)-1]
#     i+=1
#     sum+=median
        
# print(sum)



#======?떎瑜? 諛⑸쾿======#

# import sys
# input = sys.stdin.readline

# def QuickS(ListA):
#     if len(ListA)<2: return ListA
#     piv=ListA[len(ListA)//2]
#     left,right,middle=[],[],[]
#     for i in ListA:
#         if i<piv : left.append(i)
#         elif i>piv : right.append(i)
#         else: middle.append(i)
#     return QuickS(left)+middle+QuickS(right)

# #洹뱁븳?쓽 ?삤由꾩감?닚?씠嫄곕굹 

# def IsAscending(List):
#     for i in range(len(List)-1):
#         if List[i]>List[i+1]: return False
#     return True

# #洹뱁븳?쓽 ?궡由쇱감?닚?씠嫄곕굹

# def IsDescending(List):
#     for i in range(len(List)-1):
#         if List[i]<List[i+1]: return False
#     return True    
        
# sum,i=0,0
# A=list(map(int,input().split()))

# if IsAscending(A):
#     for i in range(len(A)):
#         median=A[((i+2)//2)-1]
#         print(median)
#         print("IsAscending")
#         sum+=median
# elif IsDescending(A):
#     for i in range(len(A)):
#         median=A[-((i+2)//2)]
#         print(median)
#         print("IsDescending")
#         sum+=median
# else:
#     while(i<len(A)):
#         A[:i+1]=QuickS(A[:i+1])
#         median = A[((i+2)//2)-1]
#         i+=1
#         sum+=median

# print(sum)




#===========================================#


# import sys
# import heapq
# input = sys.stdin.readline



# def HeapifyDown(A,k):
#     while 2*k+1<len(A):
#         L,R=2*k+1,2*k+2
#         if L<len(A) and A[L]<A[k]:m=L
#         else: m=k
#         if R<len(A) and A[R]<A[m]:m=R
#         if m!=k:
#             A[k],A[m]=A[m],A[k]
#             k=m
#         else: break  
    


# def HeapS(A):
#     #諛⑹떇4
#     #?옓?뿉 ?엳?뒗 理쒖넖媛믪쓣 李⑤?????濡? ?깉濡쒖슫 諛곗뿴?뿉 ?꽔?뼱二쇰㈃?꽌 ?궘?젣
#     #?궘?젣?릺?뼱?룄 ?옓 ?꽦吏덉쓣 ?쑀吏??빐?빞 ?븿?뿉 ?쑀?쓽
#     # NewL = list()
#     # while len(A) != 0:
#     r=((len(A)+1)//2)-1
#     Key=0
#     for i in range(r+1):
#         # NewL.append(A[0])
#         Key=A[0]
#         A[0],A[len(A)-1]=A[len(A)-1],A[0] #理쒖넖媛믨낵 理쒕뙎媛? ?쐞移섎?? ?뒪?솑?빐以??떎(?엳?뵾?뙆?씠 ?떎?슫 ?뿰?궛?쓣 ?쐞?빐)
#         A.pop()
#         HeapifyDown(A,0) 
#         # print(NewL)
#     return Key
    


# sum,i = 0,0

# A=list(map(int,input().split()))

# while (i<len(A)):
#     ListA=A[:i+1]
#     heapq.heapify(ListA)
#     median=HeapS(ListA)
#     # ListA=HeapS(ListA)
#     # print(ListA)
#     # median = ListA[((len(ListA)+1)//2)-1]
#     i+=1
#     # print(median)
#     sum+=median
# print(sum)





#======Merge Sort======#

# def MergeTwoSortedLists(A,first,last):
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
#     for k in range(i,m+1):
#         B.append(A[k])
#     for k in range(j,last+1):
#         B.append(A[k])
#     for i in range(first,last+1):
#         A[i]=B[i-first]
#     # print(A)

# def MergeSort(A,first,last):
#     if first>=last:return
    
#     MergeSort(A,first,(first+last)//2)
#     MergeSort(A,(first+last)//2+1,last)
#     MergeTwoSortedLists(A,first,last)
    


# sum,i = 0,0
# A=list(map(int,input().split()))

# while (i<len(A)):
#     #A[:i+1]=sorted(A[:i+1])
#     B=A[:i+1]
#     MergeSort(B,0,i)
#     # print(A[:i+1])
#     median=B[((i+2)//2)-1]
#     # print(median)
#     i+=1
#     sum+=median
# print(sum)




#======Inplace ??듭젙?젹======#

# def QuickSort(A,first, last):
#     if first>=last:return
#     left,right=first+1,last
#     p=A[first]
#     while left<=right:
#         while left <= last and A[left]<p:
#             left+=1
#         while right>first and A[right]>p:
#             right-=1
#         if left <=right:
#             A[left],A[right]=A[right],A[left]
#             left+=1; right-=1;
#     A[first],A[right]=A[right],A[first]
#     QuickSort(A,first,right-1)
#     QuickSort(A,right+1,last)


# A=list(map(int,input().split()))

# sum,i = 0,0
# while (i<len(A)):
#     #A[:i+1]=sorted(A[:i+1])
#     B=A[:i+1]
#     QuickSort(B,0,i)
#     # print(A[:i+1])
#     median=B[((i+2)//2)-1]
#     # print(median)
#     i+=1
#     sum+=median
# print(sum)





# import sys
 
# # ?옱洹??븿?닔瑜? ?옉?꽦?븯湲? ?쐞?븳 怨쇱젙
# # 1. ?븿?닔瑜? 留먮줈 ?젙?쓽?븳?떎.
# # 2. 湲곗??議곌굔?씪 ?븣 ?젣???濡? ?룞?옉?븯寃? ?옉?꽦?븳?떎.
# # 3. ?븿?닔媛? ?젣???濡? ?룞?옉?븳?떎怨? 媛??젙?븯怨? ?셿?꽦?븳?떎.
 
# def getSubMax(start, end):
#   # data?쓽 start遺??꽣 end源뚯?? 援ш컙 以? ?뿰?냽遺?遺? 理쒕???빀?쓣 援ы빐二쇰뒗 ?븿?닔.
#   # 湲곗??議곌굔 : data?쓽 ?닽?옄媛? ?븯?굹諛뽰뿉 ?뾾?쓣 ?븣
#   if start >= end:  
#     return data[start]
#   else:
#     mid = (start + end)//2
    
#     left = getSubMax(start, mid)
#     right = getSubMax(mid+1, end)
  
#     # 以묎컙遺?遺꾩쓣 ?룷?븿?븯?뒗 ?뿰?냽遺?遺? 以? 理쒕???빀?쓣 援ы븯?옄.
#     # 1 8 -5 3 | 2 5 -10 2
#     leftSum, leftMax = 0, -987987987
#     for i in range(mid, start-1, -1):
#       leftSum += data[i]
#       if leftMax < leftSum:
#         leftMax = leftSum
      
#     rightSum, rightMax = 0, -987987987
#     for i in range(mid+1, end+1):
#       rightSum += data[i] 
#       if rightMax < rightSum:
#         rightMax = rightSum
    
#     myMax = leftMax + rightMax
    
#     if left >= right and left >= myMax: return left
#     elif right >= left and right >= myMax: return right
#     else: return myMax
    
    
# if __name__ == "__main__":
#   n = int(sys.stdin.readline())
#   data = list(map(int, sys.stdin.readline().split()))
#   print(getSubMax(0, n-1))







# import matplotlib
# import matplotlib.pyplot as plt


from math import radians
import numpy as np # installed with matplotlib
import matplotlib.pyplot as plt


plt.plot([1,2,3,4],[1,4,9,16])
plt.ylabel("y numbers")
plt.xlabel('x numbers')
plt.show()