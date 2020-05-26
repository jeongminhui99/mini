from bs4 import BeautifulSoup
import urllib.request

html = urllib.request.urlopen("http://www.swu.ac.kr/www/swuniversity.html")
result = BeautifulSoup(html.read(), "html.parser")
search=result.findAll({"a"})
print("*** 서울여자대학교 학과 및 홈페이지 정보 ***\n")
print("학과                   홈페이지\n")
for s in search:
    if(s.text == "자율전공학부" or s.text == "공동기기실" or s.text == "일반대학원" or s.text == "전문대학원" or s.text == "특수대학원" or s.text == "기초교육원" or s.text == "바롬인성교육원"):
        continue
    url="http://www.swu.ac.kr"+s['href']
    html2 = urllib.request.urlopen(url)
    result2 = BeautifulSoup(html2.read(), "html.parser")
    search2 = result2.find("a", {"class", "btn btn_xl btn_blue_gray"})
    if(search2 == None):
        print(s.text, "          홈페이지가 존재하지 않음")
    elif('bacha' in search2['href']) :
        print(s.text, "          홈페이지가 존재하지 않음")
    else :
        print(s.text, "          ", search2['href'])
 




# for s in search:
#     if(s.text == "일반대학원" or s.text == "전문대학원" or s.text == "특수대학원" or s.text == "기초교육원"):
#         continue
#     print(s.text)



