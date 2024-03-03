n = int(input("Введите число от 1 до 99:"))
if n > 99 or n < 1:
    print("просили же от 1 до 99!! давай по новой!")
else:
    if n % 10 == 0 or 5 <= n % 10 <= 9 or 11 <= n <= 14:
        print(n, " Копеек")
    elif n % 10 == 1:
        print(n, " Копейка")
    else:
        print(n, " Копейки")
