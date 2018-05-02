# coding=utf-8
from urllib.request import urlopen
from urllib.error import HTTPError
import bs4
import io
import sys

def getUrlConten(url):
    try:
        urlContent = urlopen(url)
    except HTTPError as ex:
        print(ex.msg)
        return None
    else:
        html = bs4.BeautifulSoup(urlContent.read(), "html.parser")
        if html is not None:
            return html
        else:
            return None


def Main():
    url = "http://www.huaban.com"
    html = getUrlConten(url)
    if html is not None:
        print(html.body)
        print(html.tag.subTag.anotherSubTag)
        a_lable = html.findAll("a", text="平面")
        hrefs = []
        for tag in a_lable:
            attrs = tag.attrs.items()
            for key, value in attrs:
                if key == "href":
                    hrefs.append(url + value)
                print("key:%s value:%s" % (key, value))
        print("抓取到链接:%d" % hrefs.count())
    else:
        print("未获取到页面信息")


def getExpressionPackage():
    url = "http://huaban.com/boards/32549252/"
    html = getUrlConten(url)
    if html is not None:
        picContens = html.findAll("div", {"id": "waterfall"})
        picList = picContens[0].children
        for pic in picList:
            print(pic.get_text())


# Main()
getExpressionPackage()