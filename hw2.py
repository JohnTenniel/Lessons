num = int(input('Введите пятизначное число: '))

mn = 1
sr = 0
score = 0
while num > 0:
    temp = num % 10
    mn *= temp
    sr += temp
    num //= 10
    score += 1
sr = sr / score
print('Произведение цифр:', mn)
print('Среднее арифметическое:', sr)