# from bs4 import BeautifulSoup
#
# f = open('index.html').read()
# soup = BeautifulSoup(f, "html.parser")
# # row = soup.find("div", class_="row") #возвращает первый найденный
# # row = soup.find_all("div", class_="row")  # возвращает все найденные списком также тут можно ставить [1] ил не ставить
# # [1] это как с принтов ниже а юбез нее покажет все
# # print(row[1]) #для all можно выводить их как части списка
# # row = soup.find_all("div", class_="row")[1].find("div", class_="name").text #2 финд ищет в первом а text выводит
# # то что между тегами найдено вторым финд
# # свойство текс не работает на чистый файнд алл, только если выбрана его часть доп поиском или []
# # row = soup.find_all("div", {"data-set": "salary"})[0].text
# # row = soup.find_all("div", {"data-set": "salary"})
# # row = soup.find_all("div", {"class": "row"})
# # row = soup.find("div", {"class": "row"})
# # row = soup.find("div", string="Alena").parent
# # row = soup.find("div", string="Alena").parent.parent
# # row = soup.find("div", string="Alena").find_parent(class_="row")
# # row = soup.find("div", id="whois3")
# # row = soup.find("div", id="whois3").find_next_sibling()#покажет следующий соседний элемент ан одном уровне вроженности
# row = soup.find("div", id="whois3").find_previous_sibling()  # предыдущий элемент
# print(row)
import re

# from bs4 import BeautifulSoup
#
#
# def get_copywriter(tag):
#     whois = tag.find('div', class_='whois').text
#     if "Copywriter" in whois:
#         return tag
#     return None
#
#
# f = open('index.html').read()
# soup = BeautifulSoup(f, "html.parser")
#
# copywriter = []
# row = soup.find_all("div", class_="row")
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
#
# print(copywriter)
# from bs4 import BeautifulSoup
# import re
#
#
# def get_salary(s):
#     pattern = r"\d+"
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
#
# f = open('index.html').read()
# soup = BeautifulSoup(f, "html.parser")
# salary = soup.find_all('div', {"data-set": "salary"})
#
# for i in salary:
#     get_salary(i.text)

#Досмотреть пол пары

import requests
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    p1 = soup.find("header", id="masthead").find('p', class_="site-title").text
    return p1


def main():
    url = 'https://ru.wordpress.org'
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()