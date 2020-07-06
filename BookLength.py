import bs4, requests

def getBookLength(bookUrl):
        res = requests.get(bookUrl)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        elems = soup.select('#details > div:nth-child(1) > span:nth-child(3)')

        return elems[0].text.strip()


page = getBookLength('https://www.goodreads.com/book/show/19063.The_Book_Thief')

print('Length of the Book is ' + page)
