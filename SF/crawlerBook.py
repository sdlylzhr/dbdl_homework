from bs4 import BeautifulSoup
from urllib import request
import os

# 全局变量
global bookName
global bookChapter
global savePath
savePath = "C:\\Users\\SF\\Desktop\\Book"

# 书籍选择
def bookMarkList(url):
    req = request.Request(url)
    result = request.urlopen(req).read()
    soup = BeautifulSoup(result, "html5lib")

    book_mark_list = soup.find('div',{'class': 'bookmark-list'}).find("ul").find_all("li")
    url_list = ["http://www.shicimingju.com"+liPath.find("h2").find("a").attrs['href'] for liPath in book_mark_list]
    return url_list
# bookMarkList("http://www.shicimingju.com/book/")

# 书籍目录
def bookMulu(url):
    req = request.Request(url)
    result = request.urlopen(req).read()
    soup = BeautifulSoup(result, "html5lib")
    # 书名
    bookHeader = soup.find('div',{'class': 'book-header'})
    global bookName
    bookName = bookHeader.find("h1").get_text()
    print(bookName)

    book_mu_lu = soup.find('div',{'class': 'book-mulu'}).find("ul").find_all("li")
    url_list = ["http://www.shicimingju.com"+liPath.find("a").attrs['href'] for liPath in book_mu_lu]
    return url_list
# bookMulu("http://www.shicimingju.com/book/sanguoyanyi.html")

# 章节内容
def chapterContent(url):
    req = request.Request(url)
    result = request.urlopen(req).read()
    soup = BeautifulSoup(result, "html5lib")
    # 章节名
    chaptercontent = soup.find('div',{'class': 'www-main-container www-shadow-card '})
    global bookChapter
    bookChapter = chaptercontent.find("h1").get_text()
    print("   "+bookChapter)

    # chapter_content = chaptercontent.find('div',{'class': 'chapter_content'}).find_all("p")
    # string_content = [pPath.get_text() for pPath in chapter_content]
    chapter_content = chaptercontent.find('div',{'class': 'chapter_content'})
    string_content = chapter_content.get_text()
    return string_content
# chapterContent("http://www.shicimingju.com/book/sanguoyanyi/1.html")

# 存储文件
def writeText(content):
    global bookName
    global bookChapter
    global savePath
    path = "%s\\%s" % (savePath, bookName)
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
    f = open("%s\\%s.txt" % (path, bookChapter), 'a', encoding="UTF-8")
    f.write(content)
    f.close()

# 书籍下载
count = 10
i = 0
for urlMark in bookMarkList("http://www.shicimingju.com/book"):
    i += 1
    if i == count:
        break
    # 获得书籍目录页面
    for urlMulu in bookMulu(urlMark):
        # 获得章节内容页面
        writeText(chapterContent(urlMulu))
        # print(chapterContent(urlMulu))
        # for content in chapterContent(urlMulu):
        #     writeText(content)
        #     print(content)
