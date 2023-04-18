#0418
#튜플, 딕셔너리, 집합
lst = [] #리스트 // 수정, 변경, 일부 원소 삭제가능
# tuple = () 수정이 불가능한 항목 <<-- 튜플 사용
t1 = (1,2,3,4)
print(t1)
t2 = tuple()
print(t2)
t3 = 1,2,3,4,2,2,2,3,2,2
print(type(t3))
i = 1
print(type(i))
print(t3.index(4))
print(t3.count(2))
t4=1,2,3,4,5
t5=100,200,300,400,500
print(t4,t5)
print(t4)
print(t5)
# sorted() < 원본은 안바뀜 // lst.sort() < 원본이 바뀜
print(sorted(t3))
#dictionary
#key:value
#1001:"홍길동",1002:"김길동"
d1={1001:"홍길동",1002:"김길동",1003:"박길동",1004:"고길동"}
print(type(d1))
print(d1[1001])
d2=dict()
d2={}
d2['강좌명']='파이썬'
print(d2)
print(d2['강좌명'])
print(len(d2))
#dictionary key:value 1:1월, 2:월... 12:12월 for문을 돌려서 각각의 value값을 찍어라
month={1:'1월',2:'2월',3:'3월',4:'4월',5:'5월',6:'6월',7:'7월',8:'8월',9:'9월',10:'10월',11:'11월',12:'12월'}
for i in range(1,13) :
    print(month[i])
for k in month.keys() :
    print(month[k])
for j in month.values() :
    print(j)
for n in month.items() :
    print(n)
    print(n[1])
for v,z in month.items() :
    print(v)
    print(z)
for i in month : # momth.keys()
    print(i)
    print(month[i])
year={100:'2세기',200:'3세기',300:'4세기',400:'5세기',500:'6세기',600:'7세기',700:'8세기',800:'9세기',900:'10세기',1000:'11세기',}
for i in range(100,1001,100) :
    print(year[i])
#dictionary method
print("month.keys() : ", month.keys())
print("month.values() : ", month.values())
print("month.items() : ", month.items())

year.pop(100) # index에 있는 item을 제거 pop()안에는 key값을 준다.
print(year)
year.popitem() # 제일 마지막 아이템을 제거
print(year)
year.update({900:'9백년대'})
print(year)
year.update({2000:'21세기'})
print(year)

#dictionary-tuple-list 변환
#tuple - 변경불가.수정x (아메리카노, 핫초코, 딸기라떼)
#tuple -> list 유자차 추가 => tuple 변경
#list -> tuple 수강신청 전 수강생 변경 -> tuple
#tuple, list => dictionary (1,2,3,4), (홍,김,박,이)
seql=['a','b','c','d']
seqt=tuple(seql)
print(seqt)
print(type(seqt))

seql2 = list(seqt)
print(seql2)
print(type(seql2))

seqd = dict(enumerate(seql))
print(seqd)
print(type(seqd))

#zip
#list, tuple가 여러개. -> 하나의 튜플의 조합으로 된 리스트로.
lI = ['1조','2조','3조']
YA = ['홍','김','이']
YB = ['최','한','배']

z= zip(lI,YA,YB)
print(type(z))
print(list(z))
print(tuple(zip(lI,YA,YB)))

li1 = ['한식','양식','중식','인스턴트']
li2 = ['전주식당','닥터로빈','홍콩반점','롯데리아']
li3 = ['제육','파스타','짬뽕','더블베이컨세트']
#zip에 묶인 list나 tuple 중 제일 짧은 것을 기준으로 짤리게됨
print(list(zip(li1,li2,li3)))
for i in range(4) :
    print(li1[i] , li2[i] , li3[i])
lia = list(zip(li1,li2,li3))
for i in lia :
    print(i[0],i[1],i[2])

print(list(zip(li2,li3)))
print(dict(zip(li2,li3)))
print(dict(zip(li1,zip(li2,li3))))