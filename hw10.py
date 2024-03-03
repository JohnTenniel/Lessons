dic = {'emp1': {'name': 'John', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000},
       'emp3': {'name': 'Brad', 'salary': 6500}}

print(dic['emp3'])
print(dic['emp3']['salary'])
print()
dic['emp3']['salary'] = 8500
for k, v in dic.items():
    print(k)
    for x, y in dic[k].items():
        print(x, ':', y)
    print()
