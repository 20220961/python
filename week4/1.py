#0328 python class

'''
print("hello")
print(3)
print(10.5)

print(type("hello"))
print(type(3))
print(type(19.5))

i,j,k = 3,5,"hello"
print(i,j,k)
print(type(i),type(j),type(k))

a,b=100,5
a+=b
print(a)
a,b=100,5
a-=b
print(a)
a,b=100,5
a*=b
print(a)
a,b=100,5
a/=b
print(a)
a,b=100,5
a%=b
print(a)
a,b=100,5
a//=b
print(a)
a,b=100,5
a**=b
print(a)

name = input("당신의 이름은 무었인가요")
print("저의 이름은 ",name)

y2class = input("2학년 몇반 소속인가요")
print("저는 ", y2class, "(반) 학생입니다")
print(type(y2class))

age=input("나이는? ")
print("저는 ", age, "살 입니다.")
print(type(age))

print("우리 아버지는 저보다 30살 많으신",int(age)+30,"세 이십니다")
int()
float()
str()
a=10
str_a=str(a)
print("type(a)",type(a))
print("type(str_a) : ", type(str_a))

planet = input('원하는 행성은?')
strRadius = input(planet + '반지름은?')
radius = int(strRadius)

length = 2*3.14*radius
print(planet,'반지름 :', radius)
print(planet,'둘레길이 : ',length)


print([len('python')-1])
var = "python"
ch1 = var[0]
print(var[0],var[1],var[2],var[3])
print(var[0],var[-6])
print("length of var : " , len(var))
print("PYTHON"[0],"PYTHON"[2])
print(var[1:5],var[2:4],var[0:3],var[0:6])
print('python'[0:len('python')])
print(var[:3],var[:4],var[1:],var[3:])

###시험에 안나오는 부분
print(var[-5:-1],var[-4:-1],var[-6:-3],var[-6:-1],var[-len('var'):-1])

str = 'Monty Python'
print(len(str))
print(str[0:5],str[:6],str[6:12])
print(str[-12:-7],str[-6:],str[-6:0])
print(str[::-1],str[0:6:2])

###(str[::x] x가 양수일 때는 x칸 만큼 간격을 조정 음수일때는 x칸 만큼 역순로 간격을 조정)

print("abcdef" + "\b" + "c")
print("hello\n world")
print("aaa\vbbb\vccc")
print("aaaa\'bbbb\'cccc")

str_var="하하하하하"
### type(str_var) =>  str
print(str_var.replace("하","호"))

str_var2 = "안녕하세요.파이썬. 파이썬 수업입니다."
str_var3=(str_var2.replace("파이썬","자바"))
print("str_var2",str_var2)
print("str_var3",str_var3)

'''

# 실수를 입력 받음.
# 102.345
# 1+0+2+3+4+5
#sum을 출력하라

num_str=input("실수를 입력해주세요")
sum=num_str.replace(".","")
print(int(sum[0])+int(sum[1])+int(sum[2])+int(sum[3])+int(sum[4])+int(sum[5]))