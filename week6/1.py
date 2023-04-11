#0411
#리스트, 튜플, 딕셔너리, 집합

#리스트
#['김', '이','박','최']
#안에 들어가는 값은 int,float,string  다 가능하다

#튜플 <- 수정이 불허하다
#['김','이','박','최']

# 딕셔너리 { key : value, k1:v1, k2:v2, .... }
# address = {'홍길동' : '서울' , '김길동':'부천' , 'james' : '미국'}
#  print(address['홍길동'])

'''

a="1"
print(type(a)) #string
print(int(a) + 5) # 6 / print(a + 5) => error


#list
lst = [10,20,30,40,50]
print(type(lst))
print(lst[0]," ",lst[1]," ", lst[len(lst)-1])

#빈 리스트를 생성하고 하나씩 원소를 추가
list1=[]
list1.append("python")
list1.append("python")
list1.append("python")
list1.append("python")
list1.append("java")
list1.append("c++")
print(list1)
list2=['java','python','c++']
print(list1[0])
for i in range(len(list1)):
    print(list1[i])

for i in list1:
    print(i)

print(list1)
print("count : " , list1.count("python"))
print("index : ", list1.index("java"))

list1[0]="AI"
list1[2]="iot"
print(list1)

list2 = list1[0:3:1]
print(list2)
list2 = list1[1:5:1]
print(list2)
list2=list1[1:len(list1):2]
print(list2)
list2 = list1[2:6:3]
print(list2)
list2 = list1[::-1]
print(list2)

list3=list2
print(list3)
list3[1]=list2
print(list3)
list3[1:2]=list2
print(list3)

'''
'''
#list insert
food = []
food.append("짜장면")
food.append("샌드위치")
print(food)
food.insert(0,"파스타")
print(food)
food.insert(2,"햄버거")
print(food)

food.remove("짜장면")
print(food)
print(food.pop())
print(food)
print(food.pop(0))
print(food)

dessert=['사탕','초콜릿']

food.extend(dessert)
print(food)

food.reverse()
print(food)
food.sort()
print(food)

exli = ["dancer","apple","candy","flum","banan","example"]
print(exli)
print(sorted(exli))

exli.sort()
print(exli)

'''

#리스트 컴프리헨션 <= 코드를 최대한 짧게 쓰기
# 리스트 컴프리핸션 // 리스트 변수명 = [i for i in range()]
# 0~10 까지의 리스트를 만들어라
l3=[0,1,2,3,4,5,6,7,8,9,10]
print(l3)

l3=[]
for i in range(11) :
    l3.append(i)
print(l3)

l3=[i for i in range(11)]
print(l3)

l3=[i**2 for i in range(11)]
print(l3)

l3= [i**2 for i in range(11) if i%2==0]
print(l3)

# 메모리
# L1= L2 // 얕은 복사
# copy() // deep copy << 독립적으로 다른 곳에 복사
#shallow copy
print("l3: " ,l3)
array=l3
print("array : " ,array)
l3.pop()
print("l3: " ,l3)
print("array : " ,array)
print(l3 is array)

#deep copy
array2 = l3[:]
print("l3: " ,l3)
print("array2 : " ,array2)
l3.pop()
print(l3 is array2)
print("l3: " ,l3)
print("array2 : " ,array2)
array2.append(13)
print("l3: " ,l3)
print("array : " ,array)
print("array2 : " ,array2)
l3.append(12)
print("l3: " ,l3)
print("array : " ,array)
print("array2 : " ,array2)