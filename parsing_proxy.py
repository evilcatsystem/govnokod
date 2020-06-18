from bs4 import BeautifulSoup
import requests

url = requests.get('https://us-proxy.org/')

soup = BeautifulSoup(url.text, features="lxml")

result = soup.find('textarea', class_='form-control')

print(result.text)
