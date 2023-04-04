#0404
'''
str = "파이썬은 파이썬은 파이썬은 파이썬은"
newstr = str.replace("파이썬은", "자바는")
print("str :" ,str)
print("newstr : ",newstr)
print(str.find("썬"))
print(str.find("파"))
print(str.find("파이썬"))
print(str.index("파이썬"))
print(str.index("파"))
print(str.index("썬")) #만약 없는 값을 찾을때 find를 쓰면 -1값을 리턴 index를 쓰면 에러
print(str.split("썬"))
print(str.split())
print(2,"+",3,"=",5)
a,b=5,10
print('{}+{}={}'.format(2,3,5))
print('{0:d}+{1:f}={2:f}'.format(a,b,a+b))
print('{0:d}+{0:f}={2:f},{3}'.format(a,b,a+b,str))
print('{0}+{1}={2}'.format(a,b,a+b))

print("str.count('파이썬')",str.count("파이썬"))
print(' ☆★  '.join(str))

value = False
print(type(value))
print(int(value))
'''