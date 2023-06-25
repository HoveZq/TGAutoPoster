import requests
from bs4 import BeautifulSoup

async def get_links(db):
    #Получение всех блоков с ссылкой
    response = requests.get('https://forklog.com/news').text
    link_blocks = BeautifulSoup(response, 'lxml').find('div', class_='category_page_grid').find_all('div', class_='cell')
    #Создание массива с ссылками; проверка наличия ссылки в базе данных, отсев
    links = [link.find('a').get('href') for link in link_blocks if not await db.get_link_id(link.find('a').get('href')) and not 'otchet' in link.find('a').get('href') and not 'itogi-nedeli' in link.find('a').get('href')]
    return links

async def get_text(link):
	result = ''
	response = requests.get(link).text
	txts = BeautifulSoup(response, 'lxml').find('div', class_='post_content').find_all('p', recursive=False)
	for txt in txts:
		if 'forklog' in txt.text.lower():
			break
		result += f' {txt.text}'
	return result