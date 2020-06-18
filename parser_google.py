import requests
from bs4 import BeautifulSoup

user_agent = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }

search = input("Что желаете найти? ") #Запрашиваем у юзера, что он хочет найти
url = requests.get('https://www.google.com/search?q=' + search, headers=user_agent) #Делаем запрос
soup = BeautifulSoup(url.text, features="lxml") #Получаем запрос
r = soup.find_all("div", class_="r") #Выводи весь тег div class="r"

for s in r:
    link = s.find('a').get('href') #Ищем ссылки по тегу <a href="example.com"
    title = s.find("h3", {'class': 'LC20lb DKV0Md'}) #Ищем описание ссылки по тегу <h3 class="LC20lb DKV0Md" 
    title = title.get_text() #Вытаскиваем описание
    print(link + " " + title) #Выводем найденную ссылку и ее описание

########################## Кому надо допишут сами #################################
