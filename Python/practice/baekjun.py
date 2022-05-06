# 2941백준
# string = input()
# arr = [i for i in string]
# cnt,x=0,0
# while x!= len(arr):
#     if arr[x:x+3] == ['d','z','=']:
#         cnt+=1
#         x+=3
#     elif arr[x:x+2] == ['c','='] or arr[x:x+2] == ['c','-'] or arr[x:x+2] == ['d','-'] or arr[x:x+2] == ['l','j'] or arr[x:x+2] == ['n','j'] or arr[x:x+2] == ['s','='] or arr[x:x+2] == ['z','=']: 
#         cnt+=1
#         x+=2
#     else: 
#         cnt+=1
#         x+=1
# print(cnt)
   
#2941백준-더 간단한 방법
# word = input()
# cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
# for i in cro:
#     word = word.replace(i,"A")
# print(len(word))


#1316백준

# n = int(input())
# StrList=[]
# for i in range(n):
#     String = input()
#     StrList.append(String)
# cnt=0
# for i in range(len(StrList)):
#     A=[]
#     for j in StrList[i]: A.append(j)
    
    
#2292백준
# num=int(input())
# cnt,order,init=1,6,1
# while(num>init):
#     init+=order
#     order+=6
#     cnt+=1
# print(cnt)    


#1075번
import sys
a=sys.stdin.readline
N=int(a())
F=int(a())

# 만약 N이 10보다 작다면 10을 곱해준다.
if N<10: N*=10
# 가장 앞 두자리만 제외하고 0으로 바꾸고(N=(N//100)*100)
N=(N//100)*100
# N이 F로 나누어떨어질 때 까지(while(N%F!=0):)
#     1씩 더한다.(N+=1)
while(N%F!=0):
    N+=1
# N의 마지막 두 자리를 추려낸다.(result=N-(N//100)*100)
N=N-(N//100)*100
result=str(N)
# if result==0: print("00")
# elif result<10: print('0',result)
# else: print(result)
print(result.zfill(2)) #.zfill메소드 : 문자열에 사용가능하며, 매개변수로 들어가는 수 보다 길이가 짧은 문자열이면 앞에 모자르는 만큼 0을 붙여준다.


#다른 사람이 푼 것
n = int(input())
f = int(input())
n = n // 100 * 100
while n % f != 0:
    n += 1
n = str(n)
print(n[-2:])






