# for i in range(3):
#     for j in range(3-i):
#         print("* ",end=" ")
#     print()
# for i in range(1,-1, -1):
#     for j in range(3-i):
#         print("* ",end=" ")
#     print()



# CodeTree - Novice Low <?‹¤ì¤‘ë°˜ë³µë¬¸>
# ?–‰ê³? ?—´
# ?–‰ê³? ?—´?˜ ?ˆ˜ë¥? a, bë¡? ?…? ¥ë°›ì•„ ì¶œë ¥?•˜?Š” ?”„ë¡œê·¸?¨?„ ?‘?„±?•´ë³´ì„¸?š”.
# -----------ê¸°ë³¸ê°œë…ë¬¸ì œ---------
# A, B = map(int, input().split(" "))
# num = 0
# for x in range(A):
#     for y in range(B):
#         num += 1
#         print(num, end = " ")
#     print()
# ---------?—°?Šµë¬¸ì œ---------
# A, B = map(int, input().split(" "))
# num = 0
# for x in range(1,A+1):
#     for y in range(1,B+1):
#         print(x*y, end = " ")
#     print()





# ?ˆ«? ?‚¼ê°í˜•
# ? •?ˆ˜ n?˜ ê°’ì´ ì£¼ì–´ì§?ë©? ?ˆ«?ë¡? ?´ë£¨ì–´ì§? ?‚¼ê°í˜•?„ ì¶œë ¥?•˜?Š” ?”„ë¡œê·¸?¨?„ ?‘?„±?•´ë³´ì„¸?š”.
# n = int(input())
# for x in range(n):
#     for y in range(x+1):
#         print(y+1, end=" ")
#     print()



# ì½”ë“œ?„¤?„
# 5ëª…ì˜ ì½”ë“œ?„¤?„ê³? ? ?ˆ˜ë¥? ?…? ¥ë°›ì•„ ? ?ˆ˜ê°? ? œ?¼ ?‚®??? ?š”?›?˜ ? •ë³´ë?? ì¶œë ¥?•˜?Š” 
# ?”„ë¡œê·¸?¨?„ ?‘?„±?•´ë³´ì„¸?š”. 
# ?‹¨, c?–¸?–´?˜ ê²½ìš° êµ¬ì¡°ì²´ë??, ?‹¤ë¥? ?–¸?–´?˜ ê²½ìš° classë¥? ?´?š©?•˜?—¬ 
# ê°? ?‚¬?Œ?˜ ? •ë³´ë?? ?‹´??? ê°ì²´ë¥? 5ê°? ë§Œë“¤?–´ ë¬¸ì œë¥? ?•´ê²°í•´ì£¼ì„¸?š”.
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
#     if int(a.score)>int(agents[i].score): #tuple?—?Š” str ?˜•?ƒœë¡? ?“¤?–´ê°”ìœ¼?‹ˆ int ?˜•?ƒœë¡? ê³ ì³ì£¼ì–´?•¼ ë¬¸ì?¼ë¦¬ê?? ?•„?‹ˆ?¼ ?ˆ«??¼ë¦? ë¹„êµë¥? ?•´ ? œ???ë¡? ?œ ê²°ê³¼ê°? ?‚˜?˜¨?‹¤
#         a=agents[i]
# print(a.c_name, a.score)



#Top k ?ˆ«? êµ¬í•˜ê¸?
#Nê°œì˜ ?ˆ«?ê°? ì£¼ì–´ì¡Œì„ ?•Œ, ?˜¤ë¦„ì°¨?ˆœ?œ¼ë¡? ? •? ¬?–ˆ?„ ?•Œ kë²ˆì§¸ ?ˆ«?ë¥? ì¶œë ¥?•˜?Š” ?”„ë¡œê·¸?¨?„ ?‘?„±?•´ë³´ì„¸?š”.
# N, k = map(int ,input().split())
# arr = list(map(int, input().split()))
# arr.sort()
# print(arr[k-1])



# ?‘ ê°œì˜ ?™?¼?•œ ?ˆ˜?—´
# nê°œì˜ ?›?†Œë¡? ?´ë£¨ì–´ì§? ?ˆ˜?—´ A??? nê°œì˜ ?›?†Œë¡? ?´ë£¨ì–´ì§? ?ˆ˜?—´ Bê°? ì£¼ì–´ì¡Œì„ ?•Œ, 
# ?‘ ?ˆ˜?—´?´ ?„œë¡? ê°™ì?? ?›?†Œ?“¤ë¡? ?´ë£¨ì–´? ¸ ?ˆ?Š”ì§?ë¥? ?Œ?‹¨?•˜?Š” ?”„ë¡œê·¸?¨?„ ?‘?„±?•´ë³´ì„¸?š”.
# ?˜ˆë¥? ?“¤?–´ ?ˆ˜?—´ A = [1, 2, 3], ?ˆ˜?—´ B = [3, 1, 2] ?¼ë©? ê°™ì?? ?›?†Œë¡? ?´ë£¨ì–´? ¸ ?ˆì§?ë§?, 
# ?ˆ˜?—´ A = [1, 2, 5], ?ˆ˜?—´ B = [3, 1, 2] ?¼ë©? ê°™ì?? ?›?†Œë¡? ?´ë£¨ì–´? ¸ ?ˆì§? ?•Š?Šµ?‹ˆ?‹¤.
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


# ê°ì²´ ? •? ¬ - ?‚¤ë¥? ê¸°ì???œ¼ë¡? ? •? ¬
# nëª…ì˜ ?´ë¦?, ?‚¤, ëª¸ë¬´ê²Œê?? ì£¼ì–´ì§?ë©? ?‚¤ë¥? ê¸°ì???œ¼ë¡? ?˜¤ë¦„ì°¨?ˆœ?œ¼ë¡? ? •? ¬?•˜?—¬ 
# ì¶œë ¥?•˜?Š” ?”„ë¡œê·¸?¨?„ ?‘?„±?•´ë³´ì„¸?š”. 
# ?‹¨, ?™?¼?•œ ?‚¤ê°? ì£¼ì–´ì§?ì§? ?•Š?Š”?‹¤ê³? ê°?? •?•´?„ ì¢‹ìŠµ?‹ˆ?‹¤.

# ?Šœ?”Œë²„ì „
# n = int(input())
# parr = [0]*n
# for i in range(n):
#     people = tuple(input().split())
#     parr[i]= people
# parr.sort(key = lambda x: int(x[1]))
# for i in range(n):
#     name, height, weigh = parr[i]
#     print(name, height, weigh)
    
# ?´?˜?Š¤ë²„ì ¼ 
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



# êµ??˜?ˆ˜ ?ˆœ?´ì§?
# n?´ ì£¼ì–´ì§?ê³?, nëª…ì¸ ?•™?ƒ?ˆ˜?˜ ?´ë¦„ê³¼ êµ??–´, ?˜?–´, ?ˆ˜?•™ ?„¸ ê³¼ëª©?˜ ? ?ˆ˜ê°? ì£¼ì–´ì§?ë©? 
# êµ??–´, ?˜?–´, ?ˆ˜?•™ ?ˆœ?„œ???ë¡? ?š°?„ ?ˆœ?œ„ë¡? ?•˜?—¬ ê³¼ëª© ? ?ˆ˜ê°? ?†’??? ?•™?ƒë¶??„° ì¶œë ¥?•˜?Š” 
# ?”„ë¡œê·¸?¨?„ ?‘?„±?•´ë³´ì„¸?š”.
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


# ?ë¥? ?‹œê°? ê³„ì‚°
# 2011?…„ 11?›” 11?¼ a?‹œ bë¶„ì—?„œ ?‹œ?‘?•˜?—¬ 2011?…„ 11?›” 11?¼ c?‹œ dë¶„ê¹Œì§? ëª? ë¶„ì´ ê±¸ë¦¬?Š”ì§?ë¥? ê³„ì‚°?•˜?Š” ?”„ë¡œê·¸?¨?„ ?‘?„±?•´ë³´ì„¸?š”.
# a,b,c,d = tuple(map(int, input().split()))
# print(abs((c * 60 + d) - (a * 60 + b)))



# ë¸”ëŸ­?Œ“?Š” ëª…ë ¹2
# 1ë²? ì¹¸ë???„° Në²ˆì§¸ ì¹¸ê¹Œì§? ì´? Nê°œì˜ ì¹¸ì´ ?ˆ?Šµ?‹ˆ?‹¤. ?´ ì¤? Ai?—?„œ Biê¹Œì?? ê°ê° ë¸”ëŸ­?„ 1?”© ?Œ“?œ¼?¼?Š” ëª…ë ¹?´ Kë²? ì£¼ì–´ì§‘ë‹ˆ?‹¤. 
# ëª…ë ¹?„ ?‹¤ ?ˆ˜?–‰?•œ ?´?›„ 1ë²? ì¹¸ë???„° Në²? ì¹¸ê¹Œì§? ?Œ“?¸ ë¸”ëŸ­?˜ ?ˆ˜ ì¤? ìµœëŒ“ê°’ì„ ì¶œë ¥?•˜?Š” ?”„ë¡œê·¸?¨?„ ?‘?„±?•´ë³´ì„¸?š”.
        
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




#ìµœë??ë¡? ê²¹ì¹˜?Š” êµ¬ê°„
# 1ì°¨ì› ì§ì„  ?ƒ?— nê°œì˜ ?„ ë¶„ì´ ?†“?—¬ ?ˆ?Šµ?‹ˆ?‹¤. 
# ê°??¥ ë§ì´ ê²¹ì¹˜?Š” êµ¬ê°„?—?„œ?Š”, ëª? ê°œì˜ ?„ ë¶„ì´ ê²¹ì¹˜?Š”ì§?ë¥? êµ¬í•˜?Š” ?”„ë¡œê·¸?¨?„ ?‘?„±?•´ë³´ì„¸?š”. 
# ?‹¨, ê²¹ì¹˜?Š” êµ¬ê°„?„ ì°¾ëŠ” ë¬¸ì œ?´ë¯?ë¡? ?? ?—?„œ ?‹¿?Š” ê²½ìš°?Š” ê²¹ì¹˜?Š” ê²ƒìœ¼ë¡? ?ƒê°í•˜ì§? ?•Š?Šµ?‹ˆ?‹¤.

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




# ?‚¬ê°í˜•?˜ ì´? ?„“?´ 2
# 2ì°? ?‰ë©? ?œ„?— Nê°œì˜ ì§ì‚¬ê°í˜•?´ ì£¼ì–´ì§‘ë‹ˆ?‹¤. ?´ ì§ì‚¬ê°í˜•?“¤?´ ë§Œë“¤?–´?‚´?Š” ì´? ?„“?´ë¥? êµ¬í•˜?Š” ?”„ë¡œê·¸?¨?„ ?‘?„±?•´ë³´ì„¸?š”.
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




#ê²¹ì¹˜ì§? ?•Š?Š” ?‚¬ê°í˜•?˜ ?„“?´
# ì¢Œí‘œ?‰ë©´ìœ„?— ì§ì‚¬ê°í˜• A, Bë¥? ë¨¼ì?? ë¶™ì´ê³? ê·? ?œ„?— ì§ì‚¬ê°í˜• M?„ ë¶™ì???Šµ?‹ˆ?‹¤. 
# ?•„ì§? ?‚¨?•„?ˆ?Š” (M?œ¼ë¡? ?®?´ì§? ëª»í•œ) ì§ì‚¬ê°í˜• A, B?˜ ?„“?´?˜ ?•©?„ êµ¬í•˜?Š” ?”„ë¡œê·¸?¨?„ ?‘?„±?•´ë³´ì„¸?š”. 
# ?‹¨, ì§ì‚¬ê°í˜• A, B?Š” ê²¹ì¹˜ì§? ?•Šê²? ì£¼ì–´ì§„ë‹¤ê³? ê°?? •?•´?„ ì¢‹ìŠµ?‹ˆ?‹¤

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
            
        
        
        
        
  
  
  
  
