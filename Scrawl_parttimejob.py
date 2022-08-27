import requests
from bs4 import BeautifulSoup
import re

# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)
# print(soup.a.attrs)
# print(soup.a["href"])

# print(soup.a["href"].ne)

url = "https://www.albamon.com/list/gi/mon_icon_list.asp?itype=10&ps=20&ob=6&lvtype=1&rpcd=,1000,7000,2000,8000,D000,&partExc=2&rWDate=3&Empmnt_Type="
res = requests.get(url)
res.encoding = None
res.raise_for_status()
# soup = BeautifulSoup(res.content.decode('euc-kr', 'replace'), 'html.parser')
soup = BeautifulSoup(res.text, "lxml")
# show_result = []
# show_url = []
# with open("test.html", "w", encoding="utf8") as f:
#     f.write(res.text)


# def clean_text(text):
#     cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',
#                           '', text)
#     return cleaned_text

# c_text = clean_text(soup)
p1 = re.compile("원고")
q1 = re.compile("블로그")

items = soup.find_all("div", attrs={"class":"subWrap"})
print(len(items))
for item in items:
    title = item.find("p", attrs={"class":"cName"}).a.get_text()
    addr = item.find("p", attrs={"class":"cTit"}).a["href"]
    content = item.find("p", attrs={"class":"cTit"}).get_text()

    if p1.search(title) :
        continue

    elif q1.search(content) :
        continue

    print(title + "\n", "https://www.albamon.com/" + addr + "\n", content + "\n")

#     m = p.findall(str(i))
#     if m:
#         continue
#     # show_url.append("https://www.albamon.com/" + i.a["href"])
#     show_result.append(i.a.get_text())

# p = re.compile("꿀부업")

# for i in show_result:
#     m = p.findall(str(i))
#     if m:
#         show_result.remove(i)

# p = re.compile("원고작성")

# for i in show_result:
#     m = p.findall(str(i))
#     if m:
#         show_result.remove(i)

# p = re.compile("주부")

# for i in show_result:
#     m = p.findall(str(i))
#     if m:
#         show_result.remove(i)

# p = re.compile("기자")

# for i in show_result:
#     m = p.findall(str(i))
#     if m:
#         show_result.remove(i)

# p = re.compile("중국어")

# for i in show_result:
#     m = p.findall(str(i))
#     if m:
#         show_result.remove(i)

# for i in show_result:
#     print(i, "\n")

# link = menus[0].a.get_text()
# print("https://www.albamon.com/" + link)
# print("a", soup.find(attrs={"href":"/recruit"}))

# url = "https://comic.naver.com/webtoon/list?titleId=796218&weekday=sun"
# res = requests.get(url)
# res.raise_for_status()

# soup = BeautifulSoup(res.text, "lxml")
# cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[0].a.get_text()
# print(title)


