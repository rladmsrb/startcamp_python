import requests
# print(response.status_code)
# print(response.text)
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
response = requests.get(url)

data = BeautifulSoup(response.text, 'html.parser')
kospi = data.select_one('#KOSPI_now')
# print(kospi)
print(f'현재 코스피 지수는 {kospi.text}입니다.')
