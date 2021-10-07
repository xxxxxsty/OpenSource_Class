def findMax(a,b,c):
    if a>b:
        big=a
    else:
        big=b
    if c>big:
        big=c
    return big
a= int (input("첫 번째 숫자 입력: "))
b= int (input("두 번째 숫자 입력: "))
c= int (input("세 번째 숫자 입력: "))
biggest = findmax(a,b,c)
print(a,b,c,"중 가장 큰 수는",big,"입니다.")
