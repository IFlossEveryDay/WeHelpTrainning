# 請撰寫一隻 Python 程式，從以上網頁爬取每一篇文章的標題，並且能持續往上一頁爬取，
# 總共爬取十頁。本題開放使用 BeautifulSoup 這個第三方套件。
# 程式在取得標題後，以一行一標題的格式，輸出到 movie.txt 中，將生成的 movie.txt 檔案包含在你的作業資料夾中，
# 並符合以下規範：
# 1. 僅輸出開頭為[好雷]、[普雷]、[負雷] 的文章標題。
# 2. 輸出時，先輸出[好雷] 開頭的所有標題，然後依序輸出[普雷] 和[負雷] 開頭的所有標題。

import bs4
import urllib.request as req
allTitles = {}
niceMovie = ""
normalMovie = ""
badMovie = ""


def getData(url):

    request = req.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (MacintoshIntel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

        root = bs4.BeautifulSoup(data, "html.parser")
        titles = root.find_all("div", class_="title")

        for title in titles:
            if title.a != None:
                allTitles = {title.a.string}
                for nice in allTitles:
                    if "[好雷]" in nice:
                        if "Re:" not in nice:
                            global niceMovie
                            niceMovie += nice + "\n"
                            # print(niceMovie)
                            # movies.write(niceMovie + "\n")
                            # print(niceMovie + normalMovie + badMovie)
                for normal in allTitles:
                    if "[普雷]" in normal:
                        if "Re:" not in normal:
                            global normalMovie
                            normalMovie += normal + "\n"
                            # print(normalMovie)
                            # movies.write(normalMovie + "\n")
                for bad in allTitles:
                    if "[負雷]" in bad:
                        if "Re:" not in bad:
                            global badMovie
                            badMovie += bad + "\n"
                            # movies.write(badMovie + "\n")
                            # print(badMovie)

    # movies.write(niceMovie + "\n" +
    #              normalMovie + "\n" +
    #              badMovie)

    nextLink = root.find("a", string="‹ 上頁")
    return nextLink["href"]


pageURL = "https://www.ptt.cc/bbs/movie/index.html"


count = 0
while count < 10:
    pageURL = "https://www.ptt.cc" + getData(pageURL)
    count += 1


with open("movies.txt", "a", encoding="utf-8") as movies:
    movies.write(niceMovie + "\n" +
                 normalMovie + "\n" +
                 badMovie)

# print(niceMovie + "\n" + normalMovie + "\n" + badMovie)

# for title in titles:
#            if title.a != None:
#                 allTitles = {title.a.string}
#                 for nice in allTitles:
#                     if "[好雷]" in nice:
#                         if "Re:" not in nice:
#                             niceMovie = nice
#                             print(niceMovie)
#             # movies.write(niceMovie + "\n")
#             for normal in allTitles:
#                 if "[普雷]" in normal:
#                     if "Re:" not in normal:
#                         normalMovie = normal
#                         print(normalMovie)
#                         # movies.write(normalMovie + "\n")
#             for bad in allTitles:
#                 if "[負雷]" in bad:
#                     if "Re:" not in bad:
#                         badMovie = bad
#                         # movies.write(badMovie + "\n")
#                     # print(niceMovie)
#     # movies.write(niceMovie + "\n" +
#     #              normalMovie + "\n" +
#     #              badMovie)
