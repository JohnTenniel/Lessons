# i = 0
# while i < 5:
#     j = 0
#     if i % 2 == 0:
#         while j < 16:
#             print("+", end="")
#             j+=1
#     else:
#         while j < 16:
#             print("-", end="")
#             j+=1
#     print()
#     i+=1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 5:
#     j = 0
#     while j < 5:
#         if i == j:
#             print("*", end="")
#         else:
#             print(" ", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1

# n = int(input())
# for i in range(1, n + 1):
#     if n % i== 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")


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


