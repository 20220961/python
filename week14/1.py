'''
dic = {'a':10, 'b':20, 'c':30, 'd':40}
keyList = dic.keys()
valueList = dic.values()
print(keyList)
print(valueList)

## 결과
## dict_keys(['a', 'b', 'c', 'd'])
## dict_values([10, 20, 30, 40])

members = {'홍':'1','박':'2', '정': '3'}
members['최']='5'
members.update({'강':'6'})
members['김']='7'
members.update({'최':'8'})
print(members)

## 결과
## {'홍': '1', '박': '2', '정': '3', '최': '8', '강': '6', '김': '7'}

carDict = {'H101':('2017','3000'),'K301':('2022','2000'),'H401':('2020','3200'),'D221':('2020','1500'),'H111':('2022','3000'),'K301':('2022','2700')}
for key in carDict.keys():
    print(key, carDict[key])
for key,value in carDict.items():
    print(key, value)

결과
H101 ('2017', '3000')
K301 ('2022', '2700')
H401 ('2020', '3200')
D221 ('2020', '1500')
H111 ('2022', '3000')

for item in carDict.items():
    print(item)
결과 :
('H101', ('2017', '3000'))
('K301', ('2022', '2700'))
('H401', ('2020', '3200'))
('D221', ('2020', '1500'))
('H111', ('2022', '3000'))

carDict.key()
carDict.values()
carDict.items()

## 생산년도로 구성된 각 요소가 int형인 yearList를 생성하고 출력
yearList = []
for value in carDict.values():
    yearList.append(int(value[0])) # 배기량을 표기하고 싶을 시 value[1]로
print(yearList)
## 결과 : [2017, 2022, 2020, 2020, 2022]

#생산년도를 입력받아, 해당년도에 생선된 자동차가 몇대인지 출력하는 코드작성
ans = input("생산년도를 입력하세요 : ")
print(ans, " 의 등록차는 ", yearList.count(int(ans)),"대 입니다") # input 값은 String 이므로 int로 변환
# 결과 : 2020  의 등록차는  2 대 입니다

# for 문 사용
count = 0
for value in carDict.values():
    if value[0] == ans :
        count = count + 1
print(ans, "의 등록차는 ", count, "대 입니다.")
## 결과 : 2020 의 등록차는  2 대 입니다.

# 스포츠 구기종목
sport = ['축구','야구','농구','배구']
num = [11,9,5,6]
spp = dict(zip(sport,num))
pp = 0

while 1 :
    sp = input("구기 종목의 인원 수를 알고 싶은 스포츠 : ")
    if sp == 'quit' :
        break
    if sp in spp.keys():
        print(spp[sp])
    else :
        print("몰라요")
        continue
    print("ㅇㅇㅇ 님은 ", sp ,"에 대한 정보를 서치하였습니다.")
print("종료")


# lambda 함수 작성 map, filter
# 입력 숫자 하나 받고, 출력으로 숫자 +1 를 하는 함수
def addone(num) :
    return num + 1
print(addone(10)) # 결과 : 11
# lambda 입력값 : return 값
print((lambda num : num + 1)(10)) # 결과 : 11
print((lambda a,b: a+b)(10,30)) # 결과 : 40
def sum1(a,b):
    return a+b
print((lambda a,b: a%b)(100,3)) # 결과 : 1
def cal(a,b):
    return a%b
# map (funtion , 입력값리스트)
print(list(map(lambda num : num+1,[10,20,30,40,50]))) # 결과 : [11, 21, 31, 41, 51]
list1 = [100,200,300,400,500]
list2 = [1,3,5,7,9]
print(list(map(lambda a,b:a+b,list1,list2))) # 결과 : [101, 203, 305, 407, 509]
print(list(map(lambda a,b:a%b,list1,list2))) # 결과 : [0, 2, 0, 1, 5]
# list 말고 tuple로도 만들 수 있음 차이점은 tuple 은 수정 불가
## filter를 사용하여 리스트에 있는 음수 제거
list3 = [1,-2,3,-4,5,-6]
print(list(filter(lambda a:a>0,list3))) # 결과 : [1, 3, 5]

__name__

1.py => run __name__ <= "main"
2.py        __name__ <= "2"
3.py        __name__ <= "3"

__name__ << 활용법 설명 구분
활용법 : if __name__ == __main__ ** 시험 출제 **
else ~~
'''