number = 8  # if 조건문
if number < 5:
    print('숫자가 5보다 작습니다.')
elif 5 < number < 10:
    print('5보다 크고 10보다 작습니다.')

money = int(input())
if money >= 7:
    print('비행기')
elif 5 <= money < 7:
    print('기차')
elif 3 <= money < 5:
    print('버스')
else:
    print('도보')


for i in range(10):  # for 반복문
    print("hello world")

for i in 'abcde':
    print(i)


countries = ['kor','usa','china']  # if/for문 활용
for country in countries:
    if country == 'kor':
        print('한글로 분석해주세요.')
    elif country == 'usa':
        print('영어로 분석해주세요.')
    else:
        print('중국어로 분석해주세요.')


a = 0  # while 반복문
while a < 5:
    a += 1  # a = a+1
    print(a)


# 1부터 5까지 더하기
# (1) for
result = 0
for i in range(1,6):
    result = result + i
print(result)

# (2) while
a = 0
result = 0
while a < 5:
    a = a + 1
    result = result + a
print(result)


# # 제어문 (countinue, break)
for i in range(10):
    if 3 <= i <= 5:
        # continue  # 반복문의 코드 처음으로 돌아감
        break  # 반복문을 멈춤
    print(i)  # 0,1,2,6,7...


