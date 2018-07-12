from bs4 import BeautifulSoup
from urllib import request

def ioliu(url):
    req = request.Request(url)
    result = request.urlopen(req).read()
    soup = BeautifulSoup(result, "html5lib")
