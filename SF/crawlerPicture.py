from bs4 import BeautifulSoup
from urllib import request
import random
import time

# 全局变量
global numPath
global header
numPath = 0
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
}


# 打开网页
def htmlUrl(url):
    # 伪装请求报头
    global header
    # req = request.Request(url, headers=header)
    # result = request.urlopen(req).read()
    # 添加timeout异常处理
    timeout = random.choice(range(80, 180))
    req = request.Request(url, headers=header)
    while True:
        try:
            result = request.urlopen(req, timeout = timeout).read()
            break
        except Exception as e:
            print(e)
            time.sleep(3)
    return result


# 选择页面
def pageChoice(num):
    url = "https://www.walldevil.com/best-wallpapers/"
    if num != 0:
        url = url + "/page/%d" % num
    # print(url)
    return url
# pageChoice(10)


# 每页图片清单
def pictures(url):
    # header = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    # }
    # req = request.Request(url, headers=header)
    # result = request.urlopen(req).read()
    # 启用统一网页请求控制
    result = htmlUrl(url)
    soup = BeautifulSoup(result, "html5lib")

    imgsArticle = soup.find_all('article',
                                {'class': 'col-xxl-2 col-xl-five col-lg-3 col-md-4 col-sm-6 col-xs-6 col-xxs-12'})
    imgsDiv = [article.find('div', {'class': 'inner'}) for article in imgsArticle]
    imgsUrl = []
    for div in imgsDiv:
        # 筛选出图片属性
        imgsli = [li for li in div.find("ul").find_all("li")]
        if imgsli[1].get_text() == "1920x1080":
            imgsUrl.append(div.find("a").attrs['href'])
    # print(imgsUrl)
    return imgsUrl
# pictures("https://www.walldevil.com/best-wallpapers/")


# 获取单个图片下载地址
def picture(url):
    result = htmlUrl(url)
    soup = BeautifulSoup(result, "html5lib")

    imgFigure = soup.find("figure")
    imgUrl = imgFigure.find("a").attrs['href']
    # print(imgUrl)
    return imgUrl
# picture("https://www.walldevil.com/galaxy-tumblr-quotes-wallpaper-874462")


# 储存图片
def writePicture(url):
    global numPath
    try:
        result = htmlUrl(url)
        f = open("C:\\Users\\SF\\Desktop\\picture\\%d.jpg" % numPath, "wb")
        f.write(result)
        f.close()
        numPath += 1
    except Exception as e:
        print(e)


# 壁纸下载(0~20)
i = 0
while i < 20:
    for picturesUrl in pictures(pageChoice(i)):  # 获取当前页下载列表
        downloadUrl = picture(picturesUrl)  # 获取单个下载项
        print(downloadUrl)
        writePicture(downloadUrl)  # 存储下载文件
    i += 1
