#큰 수의 법칙
n,m,k = map(int, input().split())
data = list(map(int, input().split()))
data.sort() #가장 큰 수, 그 다음수 찾기
big_number = data[n-1]
second_big_num = data[n-2]


result=0
while 1:
    for i in range(k):
        if m==0:
            break
        relsult = result + big_number
        m=m-1
    if m==0:
        break
    result = result + second_big_num
    m=m-1



print(result)