# 0502
# 함수 : input을 주면 output이 결과로 나오는 것.

'''
input - 숫자 - num1
output = 숫자 - output_num
이런 기능을 하는 function - multi
'''

# 함수 정의
def multi(num1) :
    output_num = num1 * 3
    return output_num

# 정의한 함수 호출
print(multi(10))

# hello, input - 사람이름 두개입력
# ouput - 안녕 1번사람, 안녕 2 번사람

def hello(n1="홍", n2="김") :   # 기본 값을 주어 에러를 피한다
    print("안녕", n1)
    print("안녕", n2)

hello("홍길동","고길동")

# 두개의 숫자를 입력받아, 두개의 합을 함수내에서 출력

def sum(n3, n4) :
    print(n3+n4)

sum(1,2)

# 지역 변수, 전역 변수
num = 100 # 전역 변수 global variable
print("**** num: ", num) # 100

def addone() :
    num = 10
    print("addone()" , num+1) # num = 11
    print("addone() num : ", num) # num = 10

addone()
print("***num :", num) #100

# 인자의 갯수가 여러개인 경우 ex ) print

def hello2(*names) :
    for i in names :
        print("hello" , i)

hello2("고길동", "홍길동" , "전우치")

def sum2(*numb) :
    sum = 0
    for i in numb :
        sum = sum + i
    return sum

print(sum2(1,2,3))
lst = [1,2,3,4,5,6,7,8,9]
print(sum2(*lst))

# dictionary = {key: value1, key2: value2}

coffee = {"아메리카노":3000 ,"라떼":4500, "티":2700}

def printmenu(**keyvalue) :
    for key in keyvalue :
        print(key, keyvalue[key])

printmenu(**coffee)
printmenu(아메리카노=3000, 티=2700, 핫초코=4500)

def funex(*num, **menu) : # num의 합 menu를 동시 출력
    result = 0
    for n in num :
        result = result + n
    print(result)

    for key in menu :
        print(key , menu[key])

funex(1,2,3,4,5,6,7,아메=3000,핫초코=3000)
funex(*lst,**coffee)
funex(1,2,3,4,5,6,7,8,9,**coffee)

#lambda fucntion // 실행문이 하나일때 만드는 이름없는 function
# lambda parameter_name(input) : parameter(output) 로 실행하는 문법

def addone(x):
    return x+1

print(addone(100))

print((lambda x : x+1)(100))

print((lambda num1,num2: num1+num2)(100,200))

# map, filter // list가 존재할때 // map(함수,input리스트) or map(lambda,input리스트)

lst1 =[1,2,3,4,5,6]
lst2 =[2,3,4,5,6,7]

print(list(map(lambda x : x+1 , lst1)))

print(list(map(lambda num1,num2 : num1+num2, lst1,lst2)))