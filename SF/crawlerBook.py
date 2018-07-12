from bs4 import BeautifulSoup
from urllib import request

# 书籍选择
def bookMarkList(url):
    req = request.Request(url)
    result = request.urlopen(req).read()
    soup = BeautifulSoup(result, "html5lib")

    book_mark_list = soup.find('div',{'class': 'bookmark-list'}).find("ul").find_all("li")
    url_list = ["http://www.shicimingju.com"+liPath.find("h2").find("a").attrs['href'] for liPath in book_mark_list]
    # for li in book_mark_list:
    #     h2 = li.find("h2")
    #     url = "http://www.shicimingju.com"+h2.find("a").attrs['href']
    #     print(h2.get_text()+"*********"+url)
    return url_list
# bookMarkList("http://www.shicimingju.com/book/")

# 书籍目录
def bookMulu(url):
    req = request.Request(url)
    result = request.urlopen(req).read()
    soup = BeautifulSoup(result, "html5lib")

    bookHeader = soup.find('div',{'class': 'book-header'})
    print(bookHeader.find("h1").get_text())

    book_mu_lu = soup.find('div',{'class': 'book-mulu'}).find("ul").find_all("li")
    url_list = ["http://www.shicimingju.com"+liPath.find("a").attrs['href'] for liPath in book_mu_lu]
    # for li in book_mu_lu:
    #     url = "http://www.shicimingju.com"+li.find("a").attrs['href']
    #     print(li.get_text()+"*********"+url)
    return url_list
# bookMulu("http://www.shicimingju.com/book/sanguoyanyi.html")

# 章节内容
def chapterContent(url):
    req = request.Request(url)
    result = request.urlopen(req).read()
    soup = BeautifulSoup(result, "html5lib")

    chaptercontent = soup.find('div',{'class': 'www-main-container www-shadow-card '})
    print(chaptercontent.find("h1").get_text())

    chapter_content = chaptercontent.find('div',{'class': 'chapter_content'}).find_all("p")
    string_content = [pPath.get_text() for pPath in chapter_content]
    # for p in chapter_content:
    #     # temp.append(p.get_text())
    #     print(p.get_text())
    return string_content
# chapterContent("http://www.shicimingju.com/book/sanguoyanyi/1.html")

# 获得书籍选择页面
for urlMark in bookMarkList("http://www.shicimingju.com/book/"):
    # 获得书籍目录页面
    for urlMulu in bookMulu(urlMark):
        # 获得章节内容页面
        for content in chapterContent(urlMulu):
            print(content)
