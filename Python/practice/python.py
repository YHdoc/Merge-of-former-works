# for i in range(3):
#     for j in range(3-i):
#         print("* ",end=" ")
#     print()
# for i in range(1,-1, -1):
#     for j in range(3-i):
#         print("* ",end=" ")
#     print()



# CodeTree - Novice Low <?ค์ค๋ฐ๋ณต๋ฌธ>
# ?๊ณ? ?ด
# ?๊ณ? ?ด? ?๋ฅ? a, b๋ก? ?? ฅ๋ฐ์ ์ถ๋ ฅ?? ?๋ก๊ทธ?จ? ??ฑ?ด๋ณด์ธ?.
# -----------๊ธฐ๋ณธ๊ฐ๋๋ฌธ์ ---------
# A, B = map(int, input().split(" "))
# num = 0
# for x in range(A):
#     for y in range(B):
#         num += 1
#         print(num, end = " ")
#     print()
# ---------?ฐ?ต๋ฌธ์ ---------
# A, B = map(int, input().split(" "))
# num = 0
# for x in range(1,A+1):
#     for y in range(1,B+1):
#         print(x*y, end = " ")
#     print()





# ?ซ? ?ผ๊ฐํ
# ? ? n? ๊ฐ์ด ์ฃผ์ด์ง?๋ฉ? ?ซ?๋ก? ?ด๋ฃจ์ด์ง? ?ผ๊ฐํ? ์ถ๋ ฅ?? ?๋ก๊ทธ?จ? ??ฑ?ด๋ณด์ธ?.
# n = int(input())
# for x in range(n):
#     for y in range(x+1):
#         print(y+1, end=" ")
#     print()



# ์ฝ๋?ค?
# 5๋ช์ ์ฝ๋?ค?๊ณ? ? ?๋ฅ? ?? ฅ๋ฐ์ ? ?๊ฐ? ? ?ผ ?ฎ??? ??? ? ๋ณด๋?? ์ถ๋ ฅ?? 
# ?๋ก๊ทธ?จ? ??ฑ?ด๋ณด์ธ?. 
# ?จ, c?ธ?ด? ๊ฒฝ์ฐ ๊ตฌ์กฐ์ฒด๋??, ?ค๋ฅ? ?ธ?ด? ๊ฒฝ์ฐ class๋ฅ? ?ด?ฉ??ฌ 
# ๊ฐ? ?ฌ?? ? ๋ณด๋?? ?ด??? ๊ฐ์ฒด๋ฅ? 5๊ฐ? ๋ง๋ค?ด ๋ฌธ์ ๋ฅ? ?ด๊ฒฐํด์ฃผ์ธ?.
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
#     if int(a.score)>int(agents[i].score): #tuple?? str ??๋ก? ?ค?ด๊ฐ์ผ? int ??๋ก? ๊ณ ์ณ์ฃผ์ด?ผ ๋ฌธ์?ผ๋ฆฌ๊?? ???ผ ?ซ??ผ๋ฆ? ๋น๊ต๋ฅ? ?ด ? ???๋ก? ? ๊ฒฐ๊ณผ๊ฐ? ??จ?ค
#         a=agents[i]
# print(a.c_name, a.score)



#Top k ?ซ? ๊ตฌํ๊ธ?
#N๊ฐ์ ?ซ?๊ฐ? ์ฃผ์ด์ก์ ?, ?ค๋ฆ์ฐจ??ผ๋ก? ? ? ฌ?? ? k๋ฒ์งธ ?ซ?๋ฅ? ์ถ๋ ฅ?? ?๋ก๊ทธ?จ? ??ฑ?ด๋ณด์ธ?.
# N, k = map(int ,input().split())
# arr = list(map(int, input().split()))
# arr.sort()
# print(arr[k-1])



# ? ๊ฐ์ ??ผ? ??ด
# n๊ฐ์ ??๋ก? ?ด๋ฃจ์ด์ง? ??ด A??? n๊ฐ์ ??๋ก? ?ด๋ฃจ์ด์ง? ??ด B๊ฐ? ์ฃผ์ด์ก์ ?, 
# ? ??ด?ด ?๋ก? ๊ฐ์?? ???ค๋ก? ?ด๋ฃจ์ด? ธ ??์ง?๋ฅ? ??จ?? ?๋ก๊ทธ?จ? ??ฑ?ด๋ณด์ธ?.
# ?๋ฅ? ?ค?ด ??ด A = [1, 2, 3], ??ด B = [3, 1, 2] ?ผ๋ฉ? ๊ฐ์?? ??๋ก? ?ด๋ฃจ์ด? ธ ?์ง?๋ง?, 
# ??ด A = [1, 2, 5], ??ด B = [3, 1, 2] ?ผ๋ฉ? ๊ฐ์?? ??๋ก? ?ด๋ฃจ์ด? ธ ?์ง? ??ต??ค.
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


# ๊ฐ์ฒด ? ? ฌ - ?ค๋ฅ? ๊ธฐ์???ผ๋ก? ? ? ฌ
# n๋ช์ ?ด๋ฆ?, ?ค, ๋ชธ๋ฌด๊ฒ๊?? ์ฃผ์ด์ง?๋ฉ? ?ค๋ฅ? ๊ธฐ์???ผ๋ก? ?ค๋ฆ์ฐจ??ผ๋ก? ? ? ฌ??ฌ 
# ์ถ๋ ฅ?? ?๋ก๊ทธ?จ? ??ฑ?ด๋ณด์ธ?. 
# ?จ, ??ผ? ?ค๊ฐ? ์ฃผ์ด์ง?์ง? ???ค๊ณ? ๊ฐ?? ?ด? ์ข์ต??ค.

# ??๋ฒ์ 
# n = int(input())
# parr = [0]*n
# for i in range(n):
#     people = tuple(input().split())
#     parr[i]= people
# parr.sort(key = lambda x: int(x[1]))
# for i in range(n):
#     name, height, weigh = parr[i]
#     print(name, height, weigh)
    
# ?ด??ค๋ฒ์ ผ 
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



# ๊ต??? ??ด์ง?
# n?ด ์ฃผ์ด์ง?๊ณ?, n๋ช์ธ ???? ?ด๋ฆ๊ณผ ๊ต??ด, ??ด, ?? ?ธ ๊ณผ๋ชฉ? ? ?๊ฐ? ์ฃผ์ด์ง?๋ฉ? 
# ๊ต??ด, ??ด, ?? ?????๋ก? ?ฐ? ??๋ก? ??ฌ ๊ณผ๋ชฉ ? ?๊ฐ? ???? ??๋ถ??ฐ ์ถ๋ ฅ?? 
# ?๋ก๊ทธ?จ? ??ฑ?ด๋ณด์ธ?.
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


# ?๋ฅ? ?๊ฐ? ๊ณ์ฐ
# 2011? 11? 11?ผ a? b๋ถ์? ????ฌ 2011? 11? 11?ผ c? d๋ถ๊น์ง? ๋ช? ๋ถ์ด ๊ฑธ๋ฆฌ?์ง?๋ฅ? ๊ณ์ฐ?? ?๋ก๊ทธ?จ? ??ฑ?ด๋ณด์ธ?.
# a,b,c,d = tuple(map(int, input().split()))
# print(abs((c * 60 + d) - (a * 60 + b)))



# ๋ธ๋ญ?? ๋ช๋ น2
# 1๋ฒ? ์นธ๋???ฐ N๋ฒ์งธ ์นธ๊น์ง? ์ด? N๊ฐ์ ์นธ์ด ??ต??ค. ?ด ์ค? Ai?? Bi๊น์?? ๊ฐ๊ฐ ๋ธ๋ญ? 1?ฉ ??ผ?ผ? ๋ช๋ น?ด K๋ฒ? ์ฃผ์ด์ง๋?ค. 
# ๋ช๋ น? ?ค ??? ?ด? 1๋ฒ? ์นธ๋???ฐ N๋ฒ? ์นธ๊น์ง? ??ธ ๋ธ๋ญ? ? ์ค? ์ต๋๊ฐ์ ์ถ๋ ฅ?? ?๋ก๊ทธ?จ? ??ฑ?ด๋ณด์ธ?.
        
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




#์ต๋??๋ก? ๊ฒน์น? ๊ตฌ๊ฐ
# 1์ฐจ์ ์ง์  ?? n๊ฐ์ ? ๋ถ์ด ??ฌ ??ต??ค. 
# ๊ฐ??ฅ ๋ง์ด ๊ฒน์น? ๊ตฌ๊ฐ???, ๋ช? ๊ฐ์ ? ๋ถ์ด ๊ฒน์น?์ง?๋ฅ? ๊ตฌํ? ?๋ก๊ทธ?จ? ??ฑ?ด๋ณด์ธ?. 
# ?จ, ๊ฒน์น? ๊ตฌ๊ฐ? ์ฐพ๋ ๋ฌธ์ ?ด๋ฏ?๋ก? ?? ?? ?ฟ? ๊ฒฝ์ฐ? ๊ฒน์น? ๊ฒ์ผ๋ก? ?๊ฐํ์ง? ??ต??ค.

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




# ?ฌ๊ฐํ? ์ด? ??ด 2
# 2์ฐ? ?๋ฉ? ?? N๊ฐ์ ์ง์ฌ๊ฐํ?ด ์ฃผ์ด์ง๋?ค. ?ด ์ง์ฌ๊ฐํ?ค?ด ๋ง๋ค?ด?ด? ์ด? ??ด๋ฅ? ๊ตฌํ? ?๋ก๊ทธ?จ? ??ฑ?ด๋ณด์ธ?.
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




#๊ฒน์น์ง? ?? ?ฌ๊ฐํ? ??ด
# ์ขํ?๋ฉด์? ์ง์ฌ๊ฐํ A, B๋ฅ? ๋จผ์?? ๋ถ์ด๊ณ? ๊ท? ?? ์ง์ฌ๊ฐํ M? ๋ถ์???ต??ค. 
# ?์ง? ?จ??? (M?ผ๋ก? ?ฎ?ด์ง? ๋ชปํ) ์ง์ฌ๊ฐํ A, B? ??ด? ?ฉ? ๊ตฌํ? ?๋ก๊ทธ?จ? ??ฑ?ด๋ณด์ธ?. 
# ?จ, ์ง์ฌ๊ฐํ A, B? ๊ฒน์น์ง? ?๊ฒ? ์ฃผ์ด์ง๋ค๊ณ? ๊ฐ?? ?ด? ์ข์ต??ค

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
            
        
        
        
        
  
  
  
  
