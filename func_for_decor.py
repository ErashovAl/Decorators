import bs4
import requests
from logger_for_decor import logger

url = 'https://habr.com'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0'}


def resp(url_add=''):

    response = requests.get(url+url_add, headers=headers)
    response.raise_for_status()
    text = response.text
    
    return text


@logger
def search_in_soup(word):
    
    amount = 0

    soup = bs4.BeautifulSoup(resp('/ru/all/'), features='html.parser')
    articles = soup.find_all('article')

    for article in articles:
        
        time_stamp = article.find(class_='tm-article-snippet__datetime-published').find('time').attrs['title']
        headline = article.find(class_='tm-article-snippet__title_h2').find('a').text
        headline_link = article.find(class_='tm-article-snippet__title_h2').find('a').attrs['href']
        
        soup_page = bs4.BeautifulSoup(resp(headline_link), features='html.parser')
        ext_body = soup_page.find(class_='article-formatted-body').text
        
        text_for_search = headline + ext_body

        if word in text_for_search:
            amount += 1
            res = f"<{time_stamp}> - <{headline}> - <{url+headline_link}>"
            print(res,'\n')
    
    return f"количество совпадений: {amount}"

# search_in_soup()