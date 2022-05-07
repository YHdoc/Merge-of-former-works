
# =================================================_Selection_Heap__k踰덉㎏濡�_�옉���_�닔_李얘린================================================#

# import heapq

# def HeapifyDown(A,k):
# 	while 2*k+1<len(A):
# 		L,R=2*k+1,2*k+2
# 		if L<len(A) and A[L]<A[k]:mini=L
# 		else: mini=k
# 		if R<len(A) and A[R]<A[mini]:mini=R
# 		if mini!=k:
# 			A[k],A[mini]=A[mini],A[k]
# 			k=mini
# 		else:break
	
	
# def find_min(Alist):
# 	if len(Alist)==0: return None
# 	return Alist[0]

# def solve(A, k): # return k-th smallest key, 1 <= k <= n
# 	NewL=list()
# 	while len(A) != 0:
# 		# a=find_min(A)
# 		NewL.append(A[0])
# 		A[0],A[len(A)-1]=A[len(A)-1],A[0]
# 		A.pop()
# 		HeapifyDown(A,0)
# 		# heapq.heapify(A)
# 	# print(NewL)
# 	return NewL[k-1]

# def solve(A,k):
# 	for i in range(len(A)):
# 		if i==k-1:break
# 		A[0],A[len(A)-1]=A[len(A)-1],A[0]
# 		A.pop()
# 		HeapifyDown(A,0)
# 	return A[0]


# k = int(input())
# A = [int(x) for x in input().split()]
# heapq.heapify(A) # A is now a min-heap
# print(solve(A, k))
# 二쇱꽍
# -�븣怨좊━利� �꽕紐�-
# �쐞 solve �븿�닔�쓽 �떎�뻾 �썝由щ뒗 �쁽�옱 �옓�씠 理쒖냼�옓�씠�씪怨� 媛��젙�뻽�쓣 �븣, �엯�젰�븳 �닔 k踰덉㎏濡� �옉��� �닔媛� �굹�삱 �븣源뚯�� 洹� �옓�뿉 議댁옱�븯�뒗 理쒖넖媛믪쓣 pop �븯硫� �젣嫄고븯�뒗 寃껋씠�떎.
# �쁽�옱�쓽 �옓�뿉�꽌 理쒖넖媛믪씠 pop�맂 �썑�뿉�룄 �옓 �꽦吏덉쓣 �쑀吏��빐�빞 �븳�떎. �썝�냼媛� �븯�굹 �뾾�뼱吏� �긽�깭�뿉�꽌 由ъ뒪�듃�쓽 �썝�냼媛� 理쒖냼�옓�쓣 �쑀吏��븯�룄濡� �븯�뒗 �옉�뾽�씠 �븘�슂�븳�뜲, �쐞�쓽 肄붾뱶�뿉�꽌 HeapifyDown �븿�닔媛� �씠 �뿭�븷�쓣 �닔�뻾�븳�떎.

# 1.solve �븿�닔�쓽 �꽕紐�
# solve �븿�닔�뒗 heqpq.heapify()濡� 理쒖냼�옓�씠 �맂 A由ъ뒪�듃�뿉�꽌 k踰덉㎏濡� �옉��� �닽�옄瑜� 諛섑솚�븯�뒗 �븿�닔�씠�떎.
# �씠 �븣 A�뒗 理쒖냼�옓�쑝濡�, 猷⑦듃�끂�뱶�씤 A[0]媛� 理쒖냼媛믪씤 �삎�깭�씠�떎. �썑�닠�븷 HeapifyDown�븿�닔瑜� �쟻�슜�븯湲� �쐞�빐�꽌�뒗 �씠 A[0]瑜� 媛��옣 留덉��留� �썝�냼�씠�옄 媛��옣 �겙 媛믪쓣 媛�吏��뒗 由ы봽�끂�뱶 A[len(A)-1]怨� �쐞移섎�� 諛붽퓭�빞 �븳�떎.
# �씠�젃寃� �쐞移섍�� 諛붾�� �뮘�뿉 由ъ뒪�듃�쓽 媛��옣 �걹�쑝濡� 媛� A[0], 利� 理쒖넖媛믪�� pop�뿰�궛�쓣 �넻�빐 �궗�씪吏�怨� �쁽�옱 �옓��� HeapifyDown�븿�닔瑜� �넻�빐 �궓��� �썝�냼 以� 媛��옣 �옉��� 媛믪쓣 A[0]�쓽 �쐞移섎줈 蹂대궡怨� �썝�냼�뱾�씠 理쒖냼�옓 �꽦吏덉쓣 留뚯”�븯�룄濡� �븳�떎.(理쒖냼�옓 �꽦吏덉�� 遺�紐� �끂�뱶�쓽 �궎媛믪씠 �옄�떇 �끂�뱶�쓽 �궎媛믩낫�떎 媛숆굅�굹 �옉��� �꽦吏덉씠�떎.)
# �씠瑜� �엯�젰�븳 �닔 k蹂대떎 1 �옉��� �슏�닔 留뚰겮 諛섎났�쓣 �븯�뒗�뜲, �씠�뒗 諛섎났�슏�닔瑜� �쓽誘명븯�뒗 吏��뿭蹂��닔 i媛� 0遺��꽣 �떆�옉�븯�뒗 �씠�쑀�룄 �엳怨� 留뚯빟 k留뚰겮 諛섎났�쓣 �븯硫� �뮘�쓽 pop �뿰�궛 �븣臾몄뿉 �젙�옉 諛섑솚�빐�빞 �븷 �빐�떦 李⑤���쓽 A[0]媛믪씠 �뾾�뼱吏�湲� �븣臾몄씠湲곕룄 �븯�떎.

# 2.HeapifyDown �븿�닔�쓽 �꽕紐�
# HeapifyDown�쓽 �뿭�븷��� 留ㅺ컻蹂��닔濡� �뱾�뼱�삩 由ъ뒪�듃 A媛� 理쒖냼�옓 �꽦吏덉쓣 留뚯”�븯�룄濡� �썝�냼瑜� �옱諛곗뿴 �븯�뒗 寃껋씠�떎.
# 留ㅺ컻蹂��닔濡� �옓�쑝濡� 留뚮뱾 由ъ뒪�듃 �븯�굹��� 蹂��닔 k瑜� 諛쏅뒗�뜲, �쐞 寃쎌슦 蹂��닔 k�뒗 猷⑦듃�끂�뱶�쓽 �씤�뜳�뒪�씤 0�씠�떎. �씠�뒗 solve�븿�닔�뿉�꽌 HeapifyDown �븿�닔 �씠�쟾�뿉 理쒖넖媛믨낵 理쒕뙎媛믪쓽 �쐞移섍�� 諛붾�뚯뿀湲곗뿉 理쒖냼�옓�뿉�꽌 媛��옣 �옉��� �썝�냼媛� �옄由ы뻽�뼱�빞 �븷 猷⑦듃�끂�뱶 A[0]�뿉 媛��옣 �겙 �썝�냼�씤 A[len(A)-1]�씠 �옄由ы뻽湲� �븣臾몄씠�떎. A[0]�뿉 �옄由ы븳 �씠 �썝�냼瑜� �젣�옄由щ줈 �룎�젮蹂대궡�빞 �븯湲� �븣臾몄뿉 k=0�씠 �릺�뒗 寃껋씠�떎.
# �씠�젃寃� �몢 媛�吏�瑜� 留ㅺ컻蹂��닔濡� 諛쏆�� HeapifyDown��� �궡遺��뿉�꽌 諛섎났臾몄쓣 �떎�뻾�븯�뒗�뜲, 諛섎났臾몄�� 2*k+1�씠 �쟾泥� �썝�냼�쓽 媛쒖닔蹂대떎 �옉��� �룞�븞 �떎�뻾�븳�떎. 
# �씠�뒗 2*k+1�씠 k踰덉㎏ �끂�뱶�쓽 �쇊履쎌옄�떇�끂�뱶�쓽 �씤�뜳�뒪瑜� �쓽誘명븯�뒗�뜲 �씠寃껋씠 len(A)瑜� �씠�긽�씠�씪�뒗 寃껋�� 由ъ뒪�듃�쓽 �씤�뜳�뒪瑜� 踰쀬뼱�굹�뒗 寃껋씠湲� �븣臾몄뿉 �엳�쓣 �닔 �뾾湲� �븣臾몄씠�떎.
# �씠 議곌굔�씠 �쑀吏��릺�뒗 �룞�븞 �븿�닔�뒗 遺�紐⑤끂�뱶(k�씤�뜳�뒪瑜� 媛�吏��뒗 �썝�냼)��� �옄�떇�끂�뱶�뱾 �궗�씠�뿉 �뼱�뼡 �씤�뜳�뒪�쓽 �썝�냼媛� 媛��옣 理쒖넖媛믪쓣 媛뽯뒗吏� 李얜뒗�떎.
# 洹몃젃寃� 李얠븘吏� 理쒖넖媛믪쓽 �씤�뜳�뒪�뒗 m�씠�씪�뒗 �깉濡쒖슫 蹂��닔�뿉 ����옣�맂�떎. 媛��옣 �옉��� �썝�냼媛� �옓�쓽 媛��옣 �쐞�뿉 �엳�뼱�빞 �븳�떎�뒗 理쒖냼�옓�쓽 �듅�꽦�긽 �씠�젃寃� 李얠븘吏� 理쒖넖媛믪쓽 �씤�뜳�뒪 m��� k��� �씪移섑빐�빞 �븳�떎.
# 洹몃옒�꽌 �씪移섑븯硫� break瑜� �넻�빐 諛섎났臾몄쓣 以묐떒�븯怨� �씪移섑븯吏� �븡�쑝硫� m�씤�뜳�뒪�쓽 媛믨낵 k�씤�뜳�뒪�쓽 媛믪쓣 諛붽퓭二쇰뒗 議곗튂瑜� 痍⑦븳�떎. �뜦�떖�븘 �씠 怨쇱젙�뿉�꽌 k�뒗 �뒛 理쒖넖媛믪쓽 �씤�뜳�뒪�뿬�빞 �븯誘�濡� k�뒗 m�씠 k媛� �릺�뿀�뱺 L�씠 �릺�뿀�뱺 R�씠 �릺�뿀�뱺 �긽愿��뾾�씠 m�쑝濡� 諛붽퓭二쇱뼱�빞 �븳�떎.
# �씠 怨쇱젙�쓣 �넻�빐 由ъ뒪�듃 A�뒗 理쒖냼�옓�쓽 �꽦吏덉쓣 留뚯”�븯寃� �맂�떎.


# �쐞 怨쇱젙�쓣 �쓽�궗肄붾뱶濡� ����왂�쟻�쑝濡� �굹����궡硫� �떎�쓬怨� 媛숇떎.

# def solve(A,k):
# 	�엯�젰�븳 �슏�닔 k蹂대떎 1 �옉��� �슏�닔�룞�븞 
# 	1.猷⑦듃�끂�뱶A[0]怨� 留덉��留� 由ы봽�끂�뱶A[len(A)-1]�쓣 �뒪�솑(swap)�븳�떎.
# 	2.1�뿉�꽌 swap�쓣 �넻�빐 留먮떒�쑝濡� 蹂대궡吏� 理쒖넖媛믪쓣 pop �븳�떎
# 	3.由ъ뒪�듃�쓽 �궓��� �슂�냼�뱾�씠 理쒖냼�옓 �삎�깭瑜� �쑀吏��븯�룄濡� 議곗튂瑜� 痍⑦븳�떎.(HeapifyDown)
# 	4.諛섎났�슏�닔媛� k-1踰덉㎏媛� �릺�뿀�떎硫� 諛섎났臾몄쓣 鍮좎졇�굹��� k踰덉㎏濡� �옉��� �닔媛� �엳�뒗 �끂�뱶�씤 A[0]�쓣 諛섑솚 �븳�떎

# -�닔�뻾�떆媛� 遺꾩꽍-

# 1.HeapifyDown�쓽 �닔�뻾�떆媛�
# HeapifyDown�뿉�꽌�뒗 �씤�뜳�뒪 k瑜� 媛�吏��뒗 �썝�냼媛� 諛묒쑝濡� �궡�젮媛�硫댁꽌 理쒖븙�쓽 寃쎌슦 由ы봽�끂�뱶源뚯�� �궡�젮媛� �닔�룄 �엳�떎. �븳 踰� �궡�젮媛� �븣留덈떎 鍮꾧탳�슏�닔�뒗 �긽�닔�떆媛�(C)�씠�굹 猷⑦듃�끂�뱶�뿉�꽌 由ы봽�끂�뱶源뚯�� �궡�젮媛��뒗 理쒖븙�쓽 寃쎌슦�뿉�뒗 �옓�쓽 �넂�씠留뚰겮 �씠瑜� 諛섎났�빐�빞 �븳�떎. �씠吏꾪듃由ъ뿉�꽌 �옓�쓽 �넂�씠�뒗 log2�쓽n�씠�떎. �뵲�씪�꽌 HeapifyDown�쓽 �닔�뻾�떆媛꾩�� O(log2�쓽n)�씠 �맂�떎.
# 2.solve�쓽 �닔�뻾�떆媛�
# solve�븿�닔媛� �떎�뻾�릺�뒗 �닔�뻾�떆媛꾩뿉 �엳�뼱 理쒖븙�쓽 寃쎌슦�뒗 n媛쒖쓽 �썝�냼媛� �엳�뒗 由ъ뒪�듃�뿉�꽌 n踰덉㎏�뿉 �엳�뒗 �썝�냼瑜� 李얜뒗 寃쎌슦�씠�떎. �씠 寃쎌슦 for臾� �궡�쓽 鍮꾧탳, ����엯, pop�뿰�궛��� �븳 踰� 吏꾪뻾�븯�뒗 �뜲 �긽�닔�떆媛꾩씠 嫄몃━�굹 HeapifyDown �뿰�궛�쓽 寃쎌슦 O(log2�쓽n)�떆媛꾩씠 嫄몃┛�떎. �씠瑜� 媛먯븞�빐 solve�븿�닔�쓽 �닔�뻾�떆媛꾩쓣 鍮낆삤�몴湲곕쾿�쑝濡� �굹����궡硫� n x log n �씠誘�濡� O(nlogn)�쓽 �떆媛꾩씠 嫄몃┛�떎.
# �쟾泥댁퐫�뱶�쓽 �닔�뻾�떆媛꾩�� �긽�닔�떆媛꾩씠 嫄몃━�뒗 �뿰�궛�쓣 �젣�쇅�븯怨� heaqp.heapify(), solve() �쓽 �닔�뻾�떆媛꾩쓣 �뜑�븳 寃껋씠誘�濡�  n + nlogn�씠 �맂�떎. �씠�뒗 鍮낆삤�몴湲곕쾿�쑝濡� O(nlogn)�씠 �맂�떎.

# -�떎瑜� �븣怨좊━利섍낵�쓽 �옣,�떒�젏 鍮꾧탳-
# �뿬湲곗꽌 援ы쁽�븳 �븣怨좊━利섏�� �옓�젙�젹 諛⑹떇�씠�떎. �씠 諛⑹떇��� �씠吏꾪듃由ъ�� 理쒖냼 �삉�뒗 理쒕���옓�쓽 �꽦吏덉쓣 �씠�슜�빐 n媛쒖쓽 �썝�냼 �븯�굹�븯�굹媛� �븘�땲�씪 遺�紐�-�옄�떇媛꾩쓽 愿�怨꾨줈 �씠猷⑥뼱吏� �썝�냼�뱾濡� 鍮꾧탳�쟻 鍮좊Ⅸ �젙�젹�쓣 �븯�뒗 寃껋씠 媛��뒫�븯�떎�뒗 �옣�젏�씠 �엳�떎. �븳 �삁濡� selection �븣怨좊━利섏뿉�꽌�뒗 �뼱�뼡 �븣怨좊━利섏쓣 �벐�뜑�씪�룄 n媛쒖쓽 �썝�냼�뿉�꽌 理쒕뙎媛믪쓣 李얠븘 諛섑솚�븯�뒗 寃껋씠 n-1踰덉쓽 鍮꾧탳瑜� �슂援ы븯湲� �븣臾몄뿉 寃곌낵�쟻�쑝濡� O(n^2)�쓽 �닔�뻾�떆媛꾩씠 嫄몃━吏�留� �옓�젙�젹�뿉�꽌�뒗 �옓�쓣 �궗�슜�빐 �씠瑜� O(nlogn)踰� 留뚯뿉 �븯�뒗 寃껋씠 媛��뒫�븯�떎. �삉�븳 �옓�젙�젹��� �궫�엯怨� �궘�젣,理쒕뙎媛� �삉�뒗 理쒖넖媛� �깘�깋�뿰�궛�뿉 �듅�솕�릺�뼱 O(logn) �샊��� O(1)留뚯뿉 �빐�떦 �뿰�궛�뱾�쓣 �븯�뒗 寃껋씠 媛��뒫�븯�떎.
# 洹몃윭�굹 �씠 �븣怨좊━利섏뿉�꽌 �듅�젙 �궎媛믪쓣 �슚�쑉�쟻�쑝濡� 李얘만 湲곕���븯湲곕뒗 �옒�뱾�떎. �뼱�뼡 �궎媛믪쓣 �옓�뿉�꽌 李얜뒗�떎怨� �븷 �븣, �씠 �궎媛믪씠 �쇊履� �옄�떇�끂�뱶�뿉 �엳�뒗吏� �삤瑜몄そ �옄�떇�끂�뱶�뿉 �엳�뒗吏� �븣 �닔媛� �뾾湲� �븣臾몄씠�떎.
# �빆�긽 �닔�뻾�떆媛꾩씠 O(nlogn)�씠 蹂댁옣�맂�떎�뒗 �젏�뿉�꽌 理쒖븙�쓽 寃쎌슦 �떎�뻾�떆媛꾩씠 湲곕낯�젙�젹�씠�굹 Quick�젙�젹蹂대떎 鍮좊Ⅴ硫� MoM�븣怨좊━利섎낫�떎 �븞�젙�쟻�씠�씪�뒗 �옣�젏�룄 �엳�떎.




# ================================================[DS+AL] Stream of medians======================================================#




#======泥� 踰덉㎏ 諛⑸쾿 Heap Sort======#

# import sys
# import heapq
# input=sys.stdin.readline

# def HeapifyDown(A,k):
# 	while 2*k+1<len(A):
# 		L,R=2*k+1,2*k+2
# 		if L<len(A) and A[L]<A[k]:m=L
# 		else: m=k
# 		if R<len(A) and A[R]<A[m]:m=R
# 		if m!=k:
# 			A[k],A[m]=A[m],A[k]
# 			k=m
# 		else:break
		
# def HeapS(A):
# 	NewL=list()
# 	while len(A) != 0:
# 		NewL.append(A[0])
# 		A[0],A[len(A)-1]=A[len(A)-1],A[0]
# 		A.pop()
# 		HeapifyDown(A,0)
# 	return NewL

# sum,i=0,0
# A=list(map(int,input().split()))

# while i<len(A):
# 	ListA=A[:i+1]
# 	heapq.heapify(ListA)
# 	ListA=HeapS(ListA)
# 	median=ListA[(len(ListA)+1)//2-1]
# 	i+=1
# 	sum+=median
# print(sum)
	


#======�몢 踰덉㎏ 諛⑸쾿 : Quick Sort======#



# def QuickS(ListA):
# 	if len(ListA)<2: return ListA
# 	piv=ListA[len(ListA)//2]
# 	left,right,middle=[],[],[]
# 	for i in ListA:
# 		if i<piv : left.append(i)
# 		elif i>piv : right.append(i)
# 		else: middle.append(i)
# 	return QuickS(left)+middle+QuickS(right)


# sum,i=0,0
# A=list(map(int,input().split()))

# while (i<len(A)):
# 	# A[:i+1]=sorted(A[:i+1])
# 	#sorted瑜� �궗�슜�븯吏� �븡怨� �삤由꾩감�닚 �젙�젹�븷 �닔 �엳�쓣源�?
# 	A[:i+1]=QuickS(A[:i+1])
# 	median = A[((i+2)//2)-1]
# 	i+=1
# 	sum+=median
	
# print(sum)






#======�꽭 踰덉㎏ 諛⑸쾿 Heap�젙�젹 �닔�젙======#

# import sys
# import heapq
# input = sys.stdin.readline

# def HeapifyDown(A,k):
# 	while 2*k+1<len(A):
# 		L,R=2*k+1,2*k+2
# 		if L<len(A) and A[L]<A[k]:m=L
# 		else: m=k
# 		if R<len(A) and A[R]<A[m]:m=R
# 		if m!=k:
# 			A[k],A[m]=A[m],A[k]
# 			k=m
# 		else: break
		
		
# def HeapS(A):
# 	r=((len(A)+1)//2)-1
# 	Key=0
# 	for i in range(r+1):
# 		Key=A[0]
# 		A[0],A[len(A)-1]=A[len(A)-1],A[0]
# 		A.pop()
# 		HeapifyDown(A,0) 
# 	return Key

# sum,i = 0,0
# A=list(map(int,input().split()))

# while (i<len(A)):
# 	ListA=A[:i+1]
# 	heapq.heapify(ListA)
# 	median=HeapS(ListA)
# 	i+=1
# 	sum+=median
# print(sum)



#======�꽕 踰덉㎏ 諛⑸쾿 Merge Sort======#
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

# def MergeSort(A,first,last):
#     if first>=last:return
    
#     MergeSort(A,first,(first+last)//2)
#     MergeSort(A,(first+last)//2+1,last)
#     MergeTwoSortedLists(A,first,last)
    


# sum,i = 0,0
# A=list(map(int,input().split()))

# while (i<len(A)):
#     B=A[:i+1]
#     MergeSort(B,0,i)
#     median=B[((i+2)//2)-1]
#     i+=1
#     sum+=median
# print(sum)





#======�떎�꽢踰덉㎏ 諛⑸쾿 Inplace QuickSorting �븣怨좊━利�======#

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



#======�뿬�꽢踰덉㎏ 諛⑸쾿 : heap�젙�젹 �옱�닔�젙======#
# import heapq

# def HeapifyDown(A,k):
# 	while 2*k+1<len(A):
# 		L,R=2*k+1,2*k+2
# 		if L<len(A) and A[L]<A[k]:mini=L
# 		else: mini=k
# 		if R<len(A) and A[R]<A[mini]:mini=R
# 		if mini!=k:
# 			A[k],A[mini]=A[mini],A[k]
# 			k=mini
# 		else:break

# def solve(A,k):
# 	for i in range(len(A)):
# 		if i==k:break
# 		A[0],A[len(A)-1]=A[len(A)-1],A[0]
# 		A.pop()
# 		HeapifyDown(A,0)
# 	return A[0]


# ##Main
# sum,i = 0,0
# A=list(map(int,input().split()))

# while (i<len(A)):

#     B=A[:i+1]
#     heapq.heapify(B)
#     median=solve(B,((i+2)//2)-1)

#     i+=1
#     sum+=median
# print(sum)






#======�씪怨깅쾲吏몃갑踰� 議곌굔異붽�� ��듭젙�젹======#

#�씠 �븣怨좊━利섏�� �씪諛섏쟻�씤 ��듭젙�젹�씠�떎. 
# 洹몃윭�굹 ��듭젙�젹��� �뙆�씪誘명꽣濡� �뱾�뼱�삤�뒗 由ъ뒪�듃A媛� �삤由꾩감�닚, �샊��� �궡由쇱감�닚�쑝濡� �젙�젹�릺�뼱 �엳怨� pivot�씠 A[0] �삉�뒗 A[len(A)-1]�씪 寃쎌슦�뿉 理쒖븙�쓽 �떆媛꾨났�옟�룄瑜� 媛�吏꾨떎.
# �씠 �몢 寃쎌슦瑜� 媛��젙�빐 �몢 寃쎌슦�뿉 蹂대떎 �슚怨쇱쟻�쑝濡� ���泥섑븷 �닔 �엳�뒗 肄붾뱶瑜� 異붽���빐以� 寃껋씠�떎.
# �떒, �셿�쟾�븳 �삤由꾩감�닚 �샊��� �셿�쟾�븳 �궡由쇱감�닚�씠 �븘�땲�씪硫� �슚怨쇨�� �뾾�떎.

# import sys
# input = sys.stdin.readline 

# def QuickS(ListA):																#��듭젙�젹 �븣怨좊━利�
#     if len(ListA)<2: return ListA									#諛붾떏議곌굔 : 由ъ뒪�듃�쓽 �썝�냼媛� �븯�굹 �삉�뒗 �븘�삁 �뾾�떎硫� 洹몃깷 諛섑솚�븳�떎.
#     piv=ListA[len(ListA)//2]											#湲곗���씠 �릺�뒗 �뵾踰쀬쓣 �젙�븳�떎. �뵾踰쀬�� 以묎컙踰덉㎏ �썝�냼瑜� �벐�뒗 寃껋씠 �븞�젙�쟻�씠�떎.
#     left,right,middle=[],[],[]										#�뵾踰쀫낫�떎 �옉��� 媛�, �겙 媛�, 媛숈�� 媛믪쓣 �꽔�뼱以� 由ъ뒪�듃瑜� 李⑤�����濡� �깮�꽦�븳�떎. �씠濡� �씤�빐 InPlace �븣怨좊━利섏�� �븘�땲寃� �맂�떎.
#     for i in ListA:																#由ъ뒪�듃 A�쓽 媛믪쓣 �빐�떦�븯�뒗 由ъ뒪�듃�뿉 �꽔�뼱二쇰뒗 �옉�뾽
#         if i<piv : left.append(i)
#         elif i>piv : right.append(i)
#         else: middle.append(i)										
#     return QuickS(left)+middle+QuickS(right)			#諛섑솚�븯�뒗 媛믪�� �뵾踰쀫낫�떎 �옉��� 媛믩뱾�씠 �옱洹��쟻�쑝濡� �젙�젹�맂 由ъ뒪�듃 + �뵾踰쀪낵 媛숈�� 媛믩뱾 + �뵾踰쀫낫�떎 �겙 媛믩뱾�씠 �옱洹��쟻�쑝濡� �젙�젹�맂 由ъ뒪�듃�씠�떎.
# #��듭젙�젹��� �룊洹좎쟻�쑝濡� O(nlogn)�쓽 �떆媛꾩씠 嫄몃━吏�留�, �뵾踰쀬씠 媛��옣 �옉��� �닔 �샊��� 媛��옣 �겙 �닔�씤 �긽�깭�뿉�꽌 由ъ뒪�듃�쓽 媛믩뱾�씠 �삤由꾩감�닚 �샊��� �궡由쇱감�닚�쑝濡� �젙�젹�릺�뼱 �엳�뒗 理쒖븙�쓽 寃쎌슦�뿉�뒗 O(n^2)留뚰겮�쓽 �떆媛꾩씠 嫄몃┛�떎.
	
# #�븘�옒�뒗 留ㅺ컻蹂��닔濡� �뱾�뼱媛��뒗 由ъ뒪�듃媛� �삤由꾩감�닚�씤吏� �궡由쇱감�닚�씤吏� �뙋蹂꾪븯�뒗 �븿�닔�씠�떎.
	
# #洹뱁븳�쓽 �삤由꾩감�닚�씠嫄곕굹 

# def IsAscending(List):
#     for i in range(len(List)-1):
#         if List[i]>List[i+1]: return False
#     return True			#鍮꾧탳�떆媛� = O(n)

# #洹뱁븳�쓽 �궡由쇱감�닚�씠嫄곕굹

# def IsDescending(List):
#     for i in range(len(List)-1):
#         if List[i]<List[i+1]: return False
#     return True    #鍮꾧탳�떆媛� = O(n)
        
    
    
# # def solve(A,n,s):
# #     if n==len(A)+1: return s
# #     A[:n+1]=QuickS(A[:n+1])
# #     median=A[((n+2)//2)-1]
# #     s+=median
# #     solve(A,n+1,s)


# sum,i=0,0													#sum��� 寃곌낵濡� 異쒕젰�맆 珥앺빀�씠�떎.
# A=list(map(int,input().split()))

# #由ъ뒪�듃媛� �젙�젹 �삤由꾩감�닚 �샊��� �궡由� �삤由꾩감�닚�씤 寃쎌슦瑜� 嫄몃윭�궦�떎.

# if IsAscending(A):
#     for i in range(len(A)):
#         median=A[((i+2)//2)-1]	#�삤由꾩감�닚�씪 寃쎌슦 �씠誘� �젙�젹�맂 �긽�깭�씠�떎. i媛� 1�뵫 利앷���븳�떎怨� �뻽�쓣 �븣, �씠 寃쎌슦 median��� 由ъ뒪�듃 A�쓽 ((i+2)//2)-1踰덉㎏ �썝�냼�씠�떎. 
#         sum+=median
# elif IsDescending(A):
#     for i in range(len(A)):			
#         median=A[-((i+2)//2)]		#�궡由쇱감�닚�쓽 寃쎌슦�룄 �씠誘� �젙�젹�맂 �긽�깭�씠�떎. �삤由꾩감�닚�쓽 寃쎌슦��� 諛섎��濡� 吏꾪뻾�릺誘�濡� �씠 寃쎌슦 median�쓽 �씤�뜳�뒪�뒗 (i+2)//2�뿉 �쓬�닔瑜� 遺숈뿬以��떎. 
#         sum+=median							#�쐞 鍮꾧탳臾� 紐⑤몢 cn踰덉쓽 �닔�뻾�떆媛꾩쓣 �븘�슂濡� �븳�떎. 怨좊줈 �씠 寃쎌슦�뿉 �닔�뻾�떆媛꾩�� O(n)留뚰겮�쓽 �떆媛꾩씠 嫄몃┛�떎.
# else:
#     # while(i<len(A)):
#     for i in range(len(A)):
#         A[:i+1]=QuickS(A[:i+1]) 	#�삤由꾩감�닚, �궡由쇱감�닚�씠 �븘�땶 ���遺�遺꾩쓽 寃쎌슦�뿉 �빐�떦�븯�뒗 �긽�깭�씠�떎. �씠 寃쎌슦 由ъ뒪�듃 �궡�뿉�꽌 �젙�젹�릺�뼱�빞 �븯�뒗 遺�遺꾩��, 1�뵫 利앷���븯�뒗 i��� �뜑遺덉뼱
#         median = A[((i+2)//2)-1]	#A[0]遺��꽣 A[i]源뚯���뿬�빞 �븳�떎. 洹몃윭誘�濡� �빐�떦 遺�遺꾩쓣 Quick�젙�젹濡� �젙�젹�떆耳쒖���떎. �씠 寃쎌슦 �삤由꾩감�닚�쑝濡� �젙�젹�맂 寃껋씠誘�濡�, median��� A[((i+2)//2)-1] �씠 �맂�떎.
#         # i+=1
#         sum+=median	#sum�뿉 median�쓣 �빀�빐 �늻�쟻�븳�떎.
    
# 																	#�젙�젹�씠 �셿�쟾�븳 �삤由꾩감�닚, �궡由쇱감�닚�룄 �븘�땶 �씪諛섏쟻�씤 寃쎌슦�뿉�뒗 QuickS �븿�닔瑜� �씠�슜�빐 由ъ뒪�듃�쓽 媛믩뱾�쓣 A[0]遺��꽣 A[i]源뚯�� �젙�젹�떆耳� 二쇱뼱�빞 �븳�떎. 洹몃━怨� �씠 �옉�뾽��� A�쓽 湲몄씠留뚰겮 吏꾪뻾�릺誘�濡� n踰� 吏꾪뻾�맂�떎. �떎瑜� 湲곕낯�뿰�궛�뱾�쓣 �젣�쇅�븯怨좊룄 QuickS �븿�닔瑜� n踰� 諛섎났�븳�떎. �룊洹좎쟻�쑝濡� n*nlogn+cn媛� �릺寃좎��留� 理쒖븙�쓽 寃쎌슦 �닔�뻾�떆媛꾩�� n*(n^2)+cn媛� �맂�떎. 利�, �씠 �븣怨좊━利섏쓽 �룊洹좎쟻�씤 �닔�뻾�떆媛꾩�� O(n^2logn)�씠 �릺寃좎��留�, 理쒖븙�쓽 寃쎌슦 �닔�뻾�떆媛꾩�� O(n^3)�씠 �맂�떎. 
			
# print(sum)	#寃곌낵 異쒕젰











# ================================================Quick, Merge, Heap �젙�젹 鍮꾧탳�빐蹂닿린======================================================#



# """1.Heap �젙�젹"""

# def HeapifyDown(A,k,n):
# 	while 2*k+1<n:
# 		L,R=2*k+1,2*k+2
# 		if L<n and A[L]>A[k]:maxi=L
# 		else: maxi=k
# 		if R<n and A[R]>A[maxi]:maxi=R
# 		if maxi!=k:
# 			A[k],A[maxi]=A[maxi],A[k]
# 			k=maxi
# 		else:break

# def make_heap(A):
#     n=len(A)
#     for k in range(n-1,-1,-1):
#         HeapifyDown(A,k,n)


# def heap_sort(A):
#     make_heap(A)
#     n=len(A)

#     for i in range(len(A)-1,-1,-1):
#         A[0],A[i]=A[i],A[0]
#         n-=1
#         HeapifyDown(A,0,n)
#     return A



# """2.Quick �젙�젹"""
# def quick_sort(A,first, last):
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
#     quick_sort(A,first,right-1)
#     quick_sort(A,right+1,last)
#     return A




# """3.merge sort"""

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

# def merge_sort(A,first,last):
#     if first>=last:return
    
#     merge_sort(A,first,(first+last)//2)
#     merge_sort(A,(first+last)//2+1,last)
#     MergeTwoSortedLists(A,first,last)
#     return A
    
    
# # A=[1,10,2,9,3,8,4,7,5,6]


# A=[-365, -251, 389, 159, -961, -958, 458, 73, 61, 362]

# print(merge_sort(A,0,9))

# B=[-365, -251, 389, 159, -961, -958, 458, 73, 61, 362]
# print(quick_sort(B,0,9))

# A=[-365, -251, 389, 159, -961, -958, 458, 73, 61, 362]
# C=[10,-32910,293,-123910, -132103,91203, 12,23219,-213, -231]
# print(heap_sort(C))








#========================================================================================================#










"""insertion sort for quick"""
#媛��옣 �옉���/�겙 �닔遺��꽣 李⑤�����濡� 李얜뒗 諛⑹떇
def insertion_sort(A,left,right):
    global Qc2, Qs2
    for i in range(left+1,right):
        j=i-1
        while j >= 0 and A[j] >A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
            Qs2+=1
            j-=1
            


"""insertion sort for merge"""
# #媛��옣 �옉���/�겙 �닔遺��꽣 李⑤�����濡� 李얜뒗 諛⑹떇
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

��� �젙�젹��� �엯�젰 �겕湲곌�� �젙留� �겢 寃쎌슦 �슚�쑉�쟻�씠吏�留� 諛곗뿴 �겕湲곌�� �옉�쓣 寃쎌슦 �궫�엯 �젙�젹�씠 �뜑 �슚怨쇱쟻�씠�떎.
鍮꾧탳��� 援먰솚 �슏�닔媛� �뜑 �쟻湲� �븣臾�.

"""

"""Quick �젙�젹 mix"""	
def quick_sort2(A,first, last):  #first = 0, last = len(n)-1�씠 �맆 寃껋씠�떎.
    global Qc2, Qs2
    if first>=last: #first=0�씠誘�濡� �씠 寃쎌슦�뒗 鍮� 由ъ뒪�듃�씤 寃쎌슦�씠�떎.
        return
    left,right=first+1,last     #鍮� 由ъ뒪�듃媛� �븘�땲�씪硫� first�뿉 1�쓣 異붽���븳�떎. 洹� 媛믪쓣 left�씪�뒗 蹂��닔�뿉 ����옣�븳�떎. 異붽���쟻�쑝濡� right�씪�뒗 蹂��닔�뿉 留덉��留� �씤�뜳�뒪瑜� ����옣�븳�떎.
    ## if first<last:            #�븘�슂 �뾾�뒗 鍮꾧탳
    
    if last-first+1 < 10:                 #鍮꾧탳 踰붿쐞媛� 25 誘몃쭔�쑝濡� 以꾩뼱�뱾�뿀�쓣 �븣 : insertion �젙�젹 �쟻�슜
        Qc2+=1
        insertion_sort(A,first,last+1)   
    else:    
        
        p=A[first]  #�뵾踰� 媛믪�� 由ъ뒪�듃�쓽 泥ル쾲吏몄뿉 �엳�뒗 �닔�씠�떎.

        
        while left<=right:
            while left <= last and A[left]<p:   #left媛� 由ъ뒪�듃 �겕湲곕낫�떎 �옉怨� A[left]媛� �뵾踰� A[first]蹂대떎 �옉�떎硫� 
                left+=1                         #left�뿉 1�쓣 �뜑�븳�떎.(鍮꾧탳 1�쉶)
                Qc2+=1
            while right>first and A[right]>p:   #right�씠 first蹂대떎 �겕怨� A[right]�씠 A[first]蹂대떎 �겕�떎硫�
                right-=1                        #right �뿉�꽌 1�쓣 類��떎.(鍮꾧탳 1�쉶)
                Qc2+=1
            if left <=right:                    #留뚯빟 left蹂대떎 right�씠 �겕�떎? �꽌濡� 援먰솚(援먰솚 1�쉶)
                A[left],A[right]=A[right],A[left]
                left+=1; right-=1;              #�뿭�떆 left�뿉 1�쓣 �뜑�빐二쇨퀬 right�뿉 1�쓣 類댁쨲
                Qs2+=1

            
        A[first],A[right]=A[right],A[first]
        Qs2+=1
        quick_sort2(A,first,right-1)
        quick_sort2(A,right+1,last)
    # return A


"""Merge �젙�젹 Mix"""
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
## �뿬湲곗뿉 �꽭 媛�吏� �젙�젹�븿�닔瑜� �쐞�븳 肄붾뱶瑜�...
##

"""Heap �젙�젹"""
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

	
"""Quick �젙�젹"""	
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

	

"""Merge �젙�젹"""
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
    Ms+=2*(last-first) #�솢 �씠�윺源�? �씠�쑀瑜� 紐⑤Ⅴ硫� �궗�슜�븷 �닔 �뾾�쓬
    #�씠�쑀:

def merge_sort(A,first,last):
    if first>=last:
    
        return
    
    merge_sort(A,first,(first+last)//2)
    merge_sort(A,(first+last)//2+1,last)
    MergeTwoSortedLists(A,first,last)
    # return A
		
# �븘�옒 肄붾뱶�뒗 諛붽씀吏� 留� 寃�!
# 吏곸젒 �떎�뻾�빐蹂대㈃, �뼱�뼡 媛믪씠 異쒕젰�릺�뒗吏� �븣 �닔 �엳�쓬
#

def check_sorted(A):
	for i in range(n-1):
		if A[i] > A[i+1]: return False
	return True

#
# Qc�뒗 quick sort�뿉�꽌 由ъ뒪�듃�쓽 �몢 �닔瑜� 鍮꾧탳�븳 �슏�닔 ����옣
# Qs�뒗 quick sort�뿉�꽌 �몢 �닔瑜� 援먰솚(swap)�븳 �슏�닔 ����옣
# Mc, Ms�뒗 merge sort�뿉�꽌 鍮꾧탳, 援먰솚(�삉�뒗 �씠�룞) �슏�닔 ����옣
# Hc, Hs�뒗 heap sort�뿉�꽌 鍮꾧탳, 援먰솚(�삉�뒗 �씠�룞) �슏�닔 ����옣
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


