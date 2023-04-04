##0404
#제어문
#if문
''' if 조건 : 실행문 
elif : 실행문 2 
else :

### hour를 입력받아 새벽 아침 점심 저녁 출력
hour = 9
if hour < 6 : print("새벽")
elif hour<12 : print("아침")
elif hour<16 : print("점심")
else : print("저녁")

### score를 입력받아 장학금 액수 출력
score_str=input("점수는?")
score = int(score_str)
if score<200 : print("50만원")
elif 200<=score<400 : print("100만원")
else : print("1000만원")

 ### if절로 오늘의 점심메뉴 정하기
ans=input("점심을 먹을까요?(Y/N)")
if ans=='Y' : 
    ans=input("서브웨이로 갈까요?(Y/N)")
    if ans=='Y' : 
        print("8호관 1층으로 가서 먹으시오.")
    elif ans=='N' :
        ans=input("학식을 먹을까요?(Y/N)")
        if ans=='Y' :
            print("8호관 3층으로 가서 먹으시오")
        elif ans=='N' :
            print("오늘은 안먹는다")
        else : print("다시 입력하시오...")
    else : print("다시 입력하시오...")
elif ans=='N' :
    print("오늘은 안먹는다")
else : print("다시 입력하시오...")

### 반복문
### for
### for ( int i = 0 ; i < 5 ; i++ ){
###       print ( " ... " )
### }

for i in 1,3,4,5,6,9 :
    print(i)

print("range1")
for i in range(0,101,10) :
    print(i)
print("range2")
for i in range(10) :
    print(i)
print("sum")
sum=0
for i in range(15) :
    sum += i
    print(i, "번째 sum : ",sum)
else:
    print("for문의 조건이 더이상 만족하지 않습니다. ")
    print("i가 range(11)에서 벗어남.")
    print("for문이 break나 continue로 종료된게 아니라 정상적으로 종료될 때 종료됨")

print("sum : ", sum)

### while 조건 : 수행문

i = 10
while i > 5 :
    print(i , "는 5보다 크다.")
    i = i-1

### n=1 부터 5까지 찍어보는 프로그래밍
i = 1
while i <= 5 :
    print(i)
    print(i, end='  **   ')
    i = i + 1

MAXNUM = 4
MAXHEIGHT = 130

more = True
cnt = 0
while more :
    height = float(input("키는?"))
    if height < MAXHEIGHT :
        cnt += 1
        print('들어가시오. ')
    else : print('커서 못 들어갑니다. ')
    if cnt == MAXNUM:
        more = False
else : print('모두 찼습니다. 다음번에 이용하세요.')

while True :
    str = input("단어를 넣으시오.")
    if str=="exit":
        print("exit합니다 종료합니다.")
        break
    else :
        if str=="apple":
            print("apple이 입력되었습니다.") 
            print("countinue를 실행합니다.")
            continue
        print("입력한 단어 : ",str)

    print("저는 아직 while안에 있습니다.")

print("while이 종료되었습니다.")

'''




while True :
    str = input("단어를 넣으시오.")
    if str=="exit":
        print("exit합니다 종료합니다.")
        break
    else :
        if str=="apple":
            print("apple이 입력되었습니다.") 
            continue
        print("입력한 단어 : ",str,str,str)