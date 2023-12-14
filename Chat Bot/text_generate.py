# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = 'https://www.xn----7sbab7amcgekn3b5j.xn--p1ai/administratsiya-mo/postanovleniya-i-rasporyazheniya-glavy-mr/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('div', class_='item')

with open("data.txt", 'w') as file:
    for data in quotes:
        link = data.find('a')  # Находим первую ссылку внутри каждого элемента с классом 'item'
        if link:
            href = link.get('href')  # Получаем атрибут href
        number = data.find('div', class_='number').text
        title = data.find('div', class_='title')
        print(number, title)
        file.write(f"{number}%{title.text}%{href}\n")








