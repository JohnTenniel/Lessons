n = int(input("Количество элементов списка:"))
L = list()
for i in range(n):
    L.append(int(input("->")))
print(L)
k = int(input("Введите индекс K: "))
L.remove(L[k])
print(L)
