# 1.py
print("hello world")
print("파이썬"+"만세")
''' 이것은
여러줄로
이루어진
주석입니다.'''
print("박병식!!" *3)
print(type("🍜"))
print("🍜🍝" *3)
print(1,2,3-5,3.14,2.718828)
print('Hi','Python')
print('23000원은','5000원 ?개','1000원 ?개')
print('5000원',23000//5000,'개')
print('1000원',(23000%5000)//1000,'개')
print(eval('3+15/2'))
print(eval('4*3%5'))
print(eval('3*-2**3'))
print(eval('"java"*3'))
print(eval('1+62-3*52'))
print(1+62-3*52)
print(eval('256*553-152'))
print(256*553-152)
print(1028%16+1028//16)
print(eval('1028%16+1028//16'))
a=78000//50000
print("5만원권",a,"장냅니다.")
aex=78000%50000
print(aex,"원남음")
b=aex//10000
print("만원권",b,"장냅니다.")
bex=aex%10000
print(bex,"원남음")
c=bex//5000
print("5천원권",c,"장냅니다")
cex=bex%5000
print(cex,"원남음")
print(cex,"원 남았으므로 5천원권 한장을 더 냅니다")
c=c+1
charge=5000-cex
print("5만원권은",a,"만원권은",b,"5천원권은",c,"거스름돈은",charge)
