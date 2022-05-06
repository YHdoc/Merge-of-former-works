# W = int(input())
# words = input().split()

# #print(words) ->단어별 리스트
# #print(len(words[0])) -> 맨 처음 단어 길이
# #print(len(words[0]+words[1])) -> 맨 처음 단어와 두 번째 단어 길이 합
# NumberofWords = len(words) #전체 단어 수
# TotalPenalty=0 #penalty의 누적합이 저장될 변수
# listA=[0]*NumberofWords #각 단어 길이 저장할 리스트, len(words)의 값은 단어의 수이다.


"""
DP의 개념은 '기억하며 풀기'이다.(혹은 "모든 방법을 일일이 검토하여 최적의 해를 구하는 법")
공백을 기준으로 띄어져 있는 각 단어의 경우마다 다음 혹은 그 다음.. k번째 단어까지 한번에 묶었을 때 그 패널티가 최소값이 되어야 한다.
ape eats가 되어야 할지 그냥 ape까지 하고 그 다음에 eats apple 를 해야 할지 결정하는 것은..
결국 한줄한줄의 패널티를 구함으로써가 아니라 전체 문장의 패널티를 구함으로써 어떤 조합이 가장 최소 패널티를 갖는 조합인지 찾아야 하는 것이다.
그 조합을 어떻게 찾을까?

일일이 기억하는 방법이 있다.
ape가 나은지 ape eats가 나은지 
cider이 나은지 cider a가 나은지 그 경우에 따른 전체 패널티 값을 어딘가에 하나하나 기억하는 것이다.
그러려면? 그 기억 장소의 형태와 기억방식을 어떻게 해야 할까?
일단 기억 장소는 DP특성상 리스트가 되어야 할것이다.
문제는 기억방식이다. 어떻게 기억해야 여러 개의 패널티값 중에서 최소값을 찾아 뽑아낼 수 있을까?

우선, 가장 작은 해의 값이 어떻게 되는지 생각해보자.
"""

"""
맨 마지막 줄과 나머지 줄을 나눠서 생각해본다.
1차원 DP테이블로 충분하다.
"""
    
    
# idx=0   

# while idx != NumberofWords:
#     PartialPenalty=0
#     WordsLength=0
#     NumberofSpace=0    
#     for i in range(NumberofWords-idx):
#         A=len(words[idx])
#         WordsLength += A
#         if WordsLength < W: 
#             NumberofSpace = i
#             idx+=1
#             #마지막 
#             if idx == NumberofWords:
#                 PartialPenalty = (W-WordsLength-NumberofSpace)**3
#                 TotalPenalty += PartialPenalty 
#                 # print(f"Penalty : {PartialPenalty}\nTotal Penalty : {TotalPenalty}")
#                 break   
#         else: 
#             PartialPenalty = (W-(WordsLength-A)-NumberofSpace)**3
#             TotalPenalty += PartialPenalty
#             # print(f"Penalty : {PartialPenalty}\nTotal Penalty : {TotalPenalty}")
#             break
# print(f"Total Penalty : {TotalPenalty}")
        
        
        

    
    
# ================================================================================== #

W = int(input())
words = input().split()

PenaltyListforFormerLines = list()
PenaltyListforLastLine = list()
PenaltyforTotalLines = list()
PenaltyforLastLine,PenaltyforFormerLines=0,0
#마지막 줄 먼저 패널티 경우의 수를 구해준다.
NumberofWordsinLastLine,WordsLength1,i=0,0,1
TotalLengthoftheSentence=len(words)

while NumberofWordsinLastLine <= W:
    PenaltyforLastLine=0
    A = len(words[-i])
    WordsLength1 += A
    NumberofSpace1=i-1
    if NumberofWordsinLastLine+A+NumberofSpace1>W: break
    # print(WordsLength1, NumberofSpace1)
    NumberofWordsinLastLine += A  
    PenaltyforLastLine = (W-WordsLength1-NumberofSpace1)**3
    PenaltyListforLastLine.append(PenaltyforLastLine)
    i+=1

    print(PenaltyListforLastLine)
    
    # 마지막 줄의 패널티가 계산될 때마다 처음~마지막 줄 전 까지의 패널티의 모든 경우의 수를 구해 가장 적은 패널티가 나오는 경우를 찾는다.
    # 마지막 줄에서 포함한 단어 수 만큼 이전 줄까지 포함되는 단어의 수가 감소한다.
    # 이 점을 반영해 남은 단어 중에서 최소 패널티가 나오는 조합을 찾는다.
    
    # 한 가지 중요한 사실
    # 패널티는 (W-전체단어길이-공백수)**3이다. 
    # W-전체단어길이-공백수 의 결과가 작으면 작을 수록 패널티도 작아진다.
    # W-전체단어길이-공백수 의 값이 최소가 되도록 하는 조합을 찾아야 한다.
   
   
   



   
# idx=0   
# Range = TotalLengthoftheSentence-i-1

# while idx != Range:
#     PartialPenalty=0
#     WordsLength=0
#     NumberofSpace=0    
#     for i in range(Range-idx):
#         A=len(words[idx])
#         WordsLength += A
#         if WordsLength < W: 
#             NumberofSpace = i
#             idx+=1
#             #마지막 
#             if idx == Range:
#                 PartialPenalty = (W-WordsLength-NumberofSpace)**3
#                 PenaltyforFormerLines += PartialPenalty 
#                 # print(f"Penalty : {PartialPenalty}\nTotal Penalty : {TotalPenalty}")
#                 break   
#         else: 
#             PartialPenalty = (W-(WordsLength-A)-NumberofSpace)**3
#             PenaltyforFormerLines += PartialPenalty
#             # print(f"Penalty : {PartialPenalty}\nTotal Penalty : {TotalPenalty}")
#             break
# print(f"Total Penalty : {PenaltyforFormerLines}")
   
   
   
   
   
   
   
   
   
   
   
# WordIndexofFormerLines,j = 0,0
# while WordIndexofFormerLines < TotalLengthoftheSentence-i:
#     WordsLength2=0
#     PenaltyforFormerLines = 0
#     while WordsLength2 <= W:
#         if WordsLength2+j > W: break
#         B = len(words[WordIndexofFormerLines])
#         WordsLength2+=B
#         WordIndexofFormerLines+=1
#         j+=1
#     WordsLength2-=B
#     PenaltyforFormerLines = (W-WordsLength2-j)**3
#     PenaltyListforFormerLines.append(PenaltyforFormerLines)

        