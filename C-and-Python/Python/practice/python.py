# for i in range(3):
#     for j in range(3-i):
#         print("* ",end=" ")
#     print()
# for i in range(1,-1, -1):
#     for j in range(3-i):
#         print("* ",end=" ")
#     print()



# CodeTree - Novice Low <?��중반복문>
# ?���? ?��
# ?���? ?��?�� ?���? a, b�? ?��?��받아 출력?��?�� ?��로그?��?�� ?��?��?��보세?��.
# -----------기본개념문제---------
# A, B = map(int, input().split(" "))
# num = 0
# for x in range(A):
#     for y in range(B):
#         num += 1
#         print(num, end = " ")
#     print()
# ---------?��?��문제---------
# A, B = map(int, input().split(" "))
# num = 0
# for x in range(1,A+1):
#     for y in range(1,B+1):
#         print(x*y, end = " ")
#     print()





# ?��?�� ?��각형
# ?��?�� n?�� 값이 주어�?�? ?��?���? ?��루어�? ?��각형?�� 출력?��?�� ?��로그?��?�� ?��?��?��보세?��.
# n = int(input())
# for x in range(n):
#     for y in range(x+1):
#         print(y+1, end=" ")
#     print()



# 코드?��?��
# 5명의 코드?��?���? ?��?���? ?��?��받아 ?��?���? ?��?�� ?��??? ?��?��?�� ?��보�?? 출력?��?�� 
# ?��로그?��?�� ?��?��?��보세?��. 
# ?��, c?��?��?�� 경우 구조체�??, ?���? ?��?��?�� 경우 class�? ?��?��?��?�� 
# �? ?��?��?�� ?��보�?? ?��??? 객체�? 5�? 만들?�� 문제�? ?��결해주세?��.
# class Agent:
#     def __init__(self, c_name, score=0):
#         self.c_name = c_name
#         self.score = score
# agents = []
# for i in range(5):
#     c_name, score = tuple(input().split())
#     agents.append(Agent(c_name, score))
# a = agents[0]
# for i in range(5):
#     if int(a.score)>int(agents[i].score): #tuple?��?�� str ?��?���? ?��?��갔으?�� int ?��?���? 고쳐주어?�� 문자?��리�?? ?��?��?�� ?��?��?���? 비교�? ?�� ?��???�? ?�� 결과�? ?��?��?��
#         a=agents[i]
# print(a.c_name, a.score)



#Top k ?��?�� 구하�?
#N개의 ?��?���? 주어졌을 ?��, ?��름차?��?���? ?��?��?��?�� ?�� k번째 ?��?���? 출력?��?�� ?��로그?��?�� ?��?��?��보세?��.
# N, k = map(int ,input().split())
# arr = list(map(int, input().split()))
# arr.sort()
# print(arr[k-1])



# ?�� 개의 ?��?��?�� ?��?��
# n개의 ?��?���? ?��루어�? ?��?�� A??? n개의 ?��?���? ?��루어�? ?��?�� B�? 주어졌을 ?��, 
# ?�� ?��?��?�� ?���? 같�?? ?��?��?���? ?��루어?�� ?��?���?�? ?��?��?��?�� ?��로그?��?�� ?��?��?��보세?��.
# ?���? ?��?�� ?��?�� A = [1, 2, 3], ?��?�� B = [3, 1, 2] ?���? 같�?? ?��?���? ?��루어?�� ?���?�?, 
# ?��?�� A = [1, 2, 5], ?��?�� B = [3, 1, 2] ?���? 같�?? ?��?���? ?��루어?�� ?���? ?��?��?��?��.
# n = int(input())
# same = True
# arr1 = list(map(int,input().split()))
# arr2 = list(map(int,input().split()))
# arr1.sort(); arr2.sort()
# for i in range(n):
#     if arr1[i] != arr2[i]:
#         same = False; break;
        
# if same == True: print("Yes")
# else: print("No")


# 객체 ?��?�� - ?���? 기�???���? ?��?��
# n명의 ?���?, ?��, 몸무게�?? 주어�?�? ?���? 기�???���? ?��름차?��?���? ?��?��?��?�� 
# 출력?��?�� ?��로그?��?�� ?��?��?��보세?��. 
# ?��, ?��?��?�� ?���? 주어�?�? ?��?��?���? �??��?��?�� 좋습?��?��.

# ?��?��버전
# n = int(input())
# parr = [0]*n
# for i in range(n):
#     people = tuple(input().split())
#     parr[i]= people
# parr.sort(key = lambda x: int(x[1]))
# for i in range(n):
#     name, height, weigh = parr[i]
#     print(name, height, weigh)
    
# ?��?��?��버젼 
# class Info:
#     def __init__(self,name, h=0, w=0):
#         self.name = name
#         self.h = h
#         self.w = w
# n = int(input())
# Group = []
# for i in range (n):
#     name, h, w = tuple(input().split())
#     Group.append(Info(name,int(h),int(w)))
# Group.sort(key = lambda i: i.h)
# for i in Group:
#     print(i.name,i.h,i.w)



# �??��?�� ?��?���?
# n?�� 주어�?�?, n명인 ?��?��?��?�� ?��름과 �??��, ?��?��, ?��?�� ?�� 과목?�� ?��?���? 주어�?�? 
# �??��, ?��?��, ?��?�� ?��?��???�? ?��?��?��?���? ?��?�� 과목 ?��?���? ?��??? ?��?���??�� 출력?��?�� 
# ?��로그?��?�� ?��?��?��보세?��.
#
# class Student:
#     def __init__(self, name, korean, english, math):
#         self.name = name
#         self.korean = korean
#         self.english = english
#         self.math = math
# 
# n = int(input())
# given_inputs = [
#     tuple(input().split())
#     for _ in range(n)
# ]
# students = [
#     Student(name, int(korean), int(english), int(math))
#     for (name, korean, english, math) in given_inputs
# ]
# 
# students.sort(key = lambda x: (-x.korean, -x.english, -x.math))
# 
# for student in students:
#     print(student.name, student.korean, student.english, student.math)


# ?���? ?���? 계산
# 2011?�� 11?�� 11?�� a?�� b분에?�� ?��?��?��?�� 2011?�� 11?�� 11?�� c?�� d분까�? �? 분이 걸리?���?�? 계산?��?�� ?��로그?��?�� ?��?��?��보세?��.
# a,b,c,d = tuple(map(int, input().split()))
# print(abs((c * 60 + d) - (a * 60 + b)))



# 블럭?��?�� 명령2
# 1�? 칸�???�� N번째 칸까�? �? N개의 칸이 ?��?��?��?��. ?�� �? Ai?��?�� Bi까�?? 각각 블럭?�� 1?�� ?��?��?��?�� 명령?�� K�? 주어집니?��. 
# 명령?�� ?�� ?��?��?�� ?��?�� 1�? 칸�???�� N�? 칸까�? ?��?�� 블럭?�� ?�� �? 최댓값을 출력?��?�� ?��로그?��?�� ?��?��?��보세?��.
        
# n, k = map(int, input().split())
# arr = [0 for i in range(n+1)]
# for i in range(k):
#     a, b = map(int,input().split())
#     for j in range(a,b+1):
#         arr[j] += 1

# max_num = arr[0]
# for i in range(n):
#     if max_num < arr[i]:
#         max_num = arr[i]
        
# print(max_num)




#최�??�? 겹치?�� 구간
# 1차원 직선 ?��?�� n개의 ?��분이 ?��?�� ?��?��?��?��. 
# �??�� 많이 겹치?�� 구간?��?��?��, �? 개의 ?��분이 겹치?���?�? 구하?�� ?��로그?��?�� ?��?��?��보세?��. 
# ?��, 겹치?�� 구간?�� 찾는 문제?���?�? ?��?��?��?�� ?��?�� 경우?�� 겹치?�� 것으�? ?��각하�? ?��?��?��?��.

# OFFSET = 100
# SIZE = 200

# n = int(input())
# checked = [0]*(SIZE+1)

# for i in range(n):
#     x1, x2 = map(int, input().split())
#     x1, x2 = x1+OFFSET, x2+OFFSET
#     for j in range(x1, x2):
#         checked[j] += 1

# max_num = max(checked)
# print(max_num)




# ?��각형?�� �? ?��?�� 2
# 2�? ?���? ?��?�� N개의 직사각형?�� 주어집니?��. ?�� 직사각형?��?�� 만들?��?��?�� �? ?��?���? 구하?�� ?��로그?��?�� ?��?��?��보세?��.
# OFFSET = 100
# MAX_R = 200

# ar_2d = [[0]*(MAX_R+1) for i in range(MAX_R+1)]
# n = int(input())
# for i in range(n):
#     x1,y1,x2,y2 = tuple(map(int, input().split()))
#     x1,y1 = x1 + OFFSET, y1 + OFFSET
#     x2, y2 = x2 + OFFSET, y2 + OFFSET
#     for x in range(x1,x2):
#         for y in range(y1,y2):
#             ar_2d[x][y] = 1
            
# cnt=0
# for x in range(0,MAX_R+1):
#     for y in range(0,MAX_R+1):
#         if ar_2d[x][y] == 1:
#             cnt += 1
        
# print(cnt)   




#겹치�? ?��?�� ?��각형?�� ?��?��
# 좌표?��면위?�� 직사각형 A, B�? 먼�?? 붙이�? �? ?��?�� 직사각형 M?�� 붙�???��?��?��. 
# ?���? ?��?��?��?�� (M?���? ?��?���? 못한) 직사각형 A, B?�� ?��?��?�� ?��?�� 구하?�� ?��로그?��?�� ?��?��?��보세?��. 
# ?��, 직사각형 A, B?�� 겹치�? ?���? 주어진다�? �??��?��?�� 좋습?��?��

# from tkinter import OFF


# OFFSET = 1000
# MAX_R = 2000

# arr_2d = [[0]*(MAX_R+1) for i in range(MAX_R+1)]

# rects = [tuple(map(int, input().split())) for i in range(3)]
# for i, (x1,y1,x2,y2) in enumerate(rects, start=1):
#     x1,y1 = x1+OFFSET, y1+OFFSET
#     x2,y2 = x2+OFFSET, y2+OFFSET
#     for x in range(x1,x2):
#         for y in range(y1,y2):
#             arr_2d[x][y] = i

# cnt = 0
# for x in range(0,MAX_R+1):
#     for y in range(0,MAX_R+1):
#         if arr_2d[x][y] == 1 or arr_2d[x][y] == 2:
#             cnt += 1
# print(cnt)
            
        
        
        
        
  
  
  
  
