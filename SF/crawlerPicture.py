from bs4 import BeautifulSoup
from urllib import request
import random

# 壁纸清单
def ioliu(url):
    # 伪装请求报头
    header = {
        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        # 'Accept-Encoding': 'gzip, deflate, sdch',
        # 'Accept-Language': 'zh-CN,zh;q=0.8',
        # 'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }
    timeout = random.choice(range(80, 180))

    req = request.Request(url, headers = header)
    result = request.urlopen(req).read()
    soup = BeautifulSoup(result, "html5lib")

    imgs = soup.select(".download")
    imgList = ["https://bing.ioliu.cn"+img.attrs['href'] for img in imgs]
    # print(imgList)
    imgName = 0
    for imgPath in imgList:
        print(imgPath)
        try:
            f = open("C:\\Users\\SF\\Desktop\\picture\\%d.jpg"%imgName,"wb")
            imgName += 1;
            f.write(request.urlopen(imgPath).read())
            f.close()
        except Exception as e:
            print(e)

ioliu("https://bing.ioliu.cn")
