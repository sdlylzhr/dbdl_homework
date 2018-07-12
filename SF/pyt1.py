from bs4 import BeautifulSoup
from urllib import request
# 获取格式化的文本
soup = BeautifulSoup(open("neepu.html", encoding="UTF-8"), "html5lib")
# 查看内容
# print(soup.prettify())
# print(soup.title.string)
# 获取特定标签内容
print(soup.title.get_text())
print(soup.div.attrs['id'])
divList = soup.find_all("div")  # True
print(divList)
print("----------------------------------------------------------------------------------------------------")
# 根据属性筛选内容
idEls = soup.find_all("div", id="div1")  # //div
print(idEls)
clsList = soup.find_all(class_="kkk")
print(clsList)
atList = soup.find_all(attrs={"class":"kkk"})
divList = soup.select("#div1")
print(divList)

# url = "https://www.zhihu.com/question/284717296/answer/439318239"
# # 构建一个请求
# req = request.Request(url)
# # 获取请求的结果
# result = request.urlopen(req).read()
# # 使用BS解析HTML字符串
# soup = BeautifulSoup(result, "html5lib")
# # 打印文本
# # print(soup.title.string)
# anList = soup.select(".RichContent-inner")
# for an in anList:
#     print(an.get_text())

# 定义为函数
def zhihuAn(url):
    req = request.Request(url)
    result = request.urlopen(req).read()
    soup = BeautifulSoup(result, "html5lib")
    anList = soup.select(".RichContent-inner")
    for an in anList:
        print(an.get_text())
zhihuAn("https://www.zhihu.com/question/284717296/answer/439318239")

# 批量操作
questionUrl = "https://www.zhihu.com/explore/recommendations"
req = request.Request(questionUrl)
result = request.urlopen(req).read()
soup = BeautifulSoup(result, "html5lib")
anList = soup.select(".question_link")
for qu in anList:
    zhihuUrl = "https://www.zhihu.com"+qu.attrs['href']
    print(zhihuUrl)
    zhihuAn(zhihuUrl)