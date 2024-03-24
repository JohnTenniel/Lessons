str1 = 'Я изучаю Nuton. Мне нравится Nuton. Nuton очень интересный язык программирования.'
old = input('Укажите что хотите поменять: ')
new = input('Введете новый символ: ')
arr = [new if i == old else i for i in str1]
str2 = ''.join(arr)
print(str2)
