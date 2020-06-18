import requests
from bs4 import BeautifulSoup
import re

user_agent = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}

link = input("Укажите ссылку, чтобы узнать id: ") #Просим пользователя указать ссылку на инстаграм страницу
url = requests.get(link, headers=user_agent) #делаем запрос
soup = BeautifulSoup(url.text, features="lxml") #Получаем ответ
data = soup.body.find('script', text=re.compile('window\._sharedData')) #Обрабатываем и убираем window._sharedData

id = data.__str__().split('"id":"')[1].split('"')[0] #В полученном результате из переменной date ищем "id":"0123456789"
username = data.__str__().split('"username":"')[1].split('"')[0] #В полученном результате из переменной date ищем "username":"username"
followers = soup.find("meta",  property="og:description") #Обрабатываем запрос по тегу meta и вытаскиваем описание

print(followers['content']) #Выводим описание
print("id пользователя: " + id + " username: " + username) #Выводим id и username

########################## Кому надо дополнит сам ########################################
