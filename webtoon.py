from bs4 import BeautifulSoup
import urllib.request 
import os
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36')]
urllib.request.install_opener(opener)
u="https://comic.naver.com/webtoon/detail.nhn?titleId=703846&no=111&weekday=tue"
html = urllib.request.urlopen(u)
result = BeautifulSoup(html.read(), "html.parser")
name=result.findAll("h2")
title=name[1].text[0:4]
print(title)
os.chdir("/Users/user/Desktop/")
os.mkdir(title) 


big = "https://comic.naver.com/webtoon/list.nhn?titleId=703846&weekday=tue"
html = urllib.request.urlopen(big)
result = BeautifulSoup(html.read(), "html.parser")

array=[]
list=result.select('td > a')
for s in list:
    if ('https' in s['href']): 
        continue
    array.append(s['href']) # 전체 리스트 화면에서 각 화의 링크를 리스트에 담기


for i in range(len(array)):
    if i%2==0 :
        url="https://comic.naver.com"+array[i]
        html2 = urllib.request.urlopen(url)
        result2 = BeautifulSoup(html2.read(), "html.parser")
        search=result2.findAll("img", {"alt" : "comic content"})
        name=result2.findAll("meta", {"property" : "og:description"})
        for s in name:
            print(s['content'])
            little=s['content']
            os.chdir("/Users/user/Desktop/"+title)
            os.mkdir(s['content']) 
        i=1
        for s in search:
            picture = s['src']
            outpath='C:/Users/user/Desktop/'+title+'/'+little+'/'
            outfile=str(i)+'.jpg'
            urllib.request.urlretrieve(picture, outpath+outfile)
            i += 1
       