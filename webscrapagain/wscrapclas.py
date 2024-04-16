import requests

from bs4 import BeautifulSoup

#res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')

#soup = BeautifulSoup(res.text,'lxml')

#print(soup)

#print(soup.select('.vector-toc-text'))
#print(soup.select('.vector-toc-text')[0])
#for i in soup.select('.vector-toc-text'):
   # print(i.text)

#res = requests.get('http://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
#soup = BeautifulSoup(res.text,'lxml')
#print(soup)
#print(soup.select('img')[0])
#print(soup.select('.sidebar'))
#chess = soup.select('.sidebar')[0]
#print(chess['class'])
#print(chess('img')[0]['src'])

image_link = requests.get("http://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Chess_Programming.svg/150px-Chess_Programming.svg.png")

