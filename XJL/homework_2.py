from bs4 import BeautifulSoup
from urllib import request

# def save(self, item, spider):
#     file_name = '1.txt'
#     try:
#         with open(self.folder_name + file_name,'a') as fp:
#             fp.write(item)

filename = "C:\\Users\\XJL\\Desktop\\1.txt"


# def save(file_name, contents):
#     fp = open(file_name, 'w', encoding='utf-8')
#     fp.write(contents)
#     fp.close()
# yield


def shiCi(url, file_name):
    # 下载
    # 构建请求
    req = request.Request(url)
    # 根据请求获取请求结果
    result = request.urlopen(req).read()
    soup = BeautifulSoup(result, 'html5lib')
    print(soup.title.string)
    muluList = soup.select(".book-mulu")
    fp = open(file_name, 'a', encoding='utf-8')
    for mulu in muluList:
        # save(filename, soup.title.string)
        fp.write(mulu.get_text())
        print(mulu.get_text())
    fp.close()


questionUrl = "http://www.shicimingju.com/book"

req = request.Request(questionUrl)

result = request.urlopen(req).read()

soup = BeautifulSoup(result, 'html5lib')

bookList = soup.find_all('div', {'class': 'bookmark-list'})[0].find_all('a')

i = 1

for book in bookList:
    if i <= 10:
        zhUrl = "http://www.shicimingju.com" + book.attrs['href']
        shiCi(zhUrl, filename)
        i += 1
    else:
        break
