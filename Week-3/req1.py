# #請撰寫一隻 Python 程式，能從以上網址取得資料，並且將景點資料用一行一筆資料，每個欄位用逗號隔開的格式，
# 輸出到 data.csv 的檔案中，請將生成的 data.csv 檔案包含在你的作業資料夾中。
# 請根據 xpostDate 欄位，僅輸出 2015 年以後(包含 2015 年) 的資料。
# 提醒：區域資料請參考原始資料的地址欄位，必須是三個字，並且為以下區域的其中一個：
# 中正區、萬華區、中山區、大同區、大安區、松山區、信義區、士林區、文山區、北投區、內湖區、南港區。
from datetime import datetime, date
import json
import urllib.request as request


src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as responese:
    data = json.load(responese)

attractions_List = data["result"]["results"]
with open("data.csv", "w", encoding="utf-8") as file:
    # json.dump(data, file, ensure_ascii=False)
    for attractions in attractions_List:
        date = datetime.strptime(attractions["xpostDate"], "%Y/%m/%d")
        # print(date)
        dist = (attractions["address"])
        # print(type(dist))
        # print(dist[5:8])
        url = attractions["file"]
        url_sep = url.split("https")
        # print("https" + url_sep[1])

        if (date > datetime(2014, 12, 31)):
            file.write(
                attractions["stitle"] + ", " +
                dist[5:8] + ", " +
                attractions["longitude"] + ", " +
                attractions["latitude"] + ", " +
                "https" + url_sep[1] + ", " +
                "\n")


# with open("data.json", "w", encoding="utf-8") as file:
#     # json.dump(data, file, ensure_ascii=False)
#     for attractions in attractions_List:
#         date = datetime.strptime(attractions["xpostDate"], "%Y/%m/%d")
#         # print(date)
#         dist = (attractions["address"])
#         # print(type(dist))
#         # print(dist[5:8])
#         url = attractions["file"]
#         url_sep = url.split("https")
#         # print("https" + url_sep[1])

#         if (date >= datetime(2015, 1, 1)):
#             file.write(json.dumps(
#                 attractions["stitle"] + ", " +
#                 dist[5:8] + ", " +
#                 attractions["longitude"] + ", " +
#                 attractions["latitude"] + ", " +
#                 "https" + url_sep[1] + ", " +
#                 "\n", ensure_ascii=False))
