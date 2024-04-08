with open("text2.txt", "r") as old:
    r = old.readlines()


print(r)
pos1 = int(input("pos1 = "))
pos2 = int(input("pos2 = "))
if 0 <= pos1 < len(r)+1 and 0 <= pos2 < len(r)+1:
    r[pos1], r[pos2] = r[pos2], r[pos1]
else:
    print("Такой строки нет")
print(r)

with open("text2.txt", "w") as new:
    new.writelines(r)