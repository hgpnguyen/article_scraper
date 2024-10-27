import scrapy
import datetime
import re
from bs4 import BeautifulSoup
from articles.items import ArticlesItem



class VnexpressSpider(scrapy.Spider):
    name = "vnexpress"
    allowed_domains = ["vnexpress.net"]
    #start_urls = ["https://vnexpress.net/tia-laser-he-lo-thanh-pho-bi-lang-quen-tren-con-duong-to-lua-4808928.html"]

    def __init__(self, start_url=None, *args, **kwargs):
        super(VnexpressSpider, self).__init__(*args, **kwargs)
        self.start_urls = [start_url]


    def parse(self, response):
        title = response.css("h1.title-detail::text").get().strip()

        content = BeautifulSoup(response.css("p.description").get(), 'html.parser').get_text().strip()
        contentElements = response.css("p.Normal")
        for para in contentElements[:-1]:
            content += '\n' + BeautifulSoup(para.get(), 'html.parser').get_text().strip()

        byline = BeautifulSoup(contentElements[-1].get(), 'html.parser').get_text().strip()

        dateStrOri = response.css("span.date::text").get().strip() #26/10/2024, 20:00 (GMT+7)
        dateList = dateStrOri.split(',')
        pattern = r'(\d+/\d+/\d+, \d+:\d+) \(GMT\+(\d+)\)'
        match = re.search(pattern, dateStrOri)
        if match:
            dateTime, gmt = match.group(1), match.group(2)
            if len(gmt) < 4:
                gmt = '+' + gmt.zfill(2) + '00'
            dateObj = datetime.datetime.strptime(dateTime + gmt, '%d/%m/%Y, %H:%M%z')
        else:
            gmtSplit = dateList[2].split('+')
            gmt = gmtSplit[1][:-1]
            if len(gmt) < 4:
                dateList[2] = gmtSplit[0] + "+" + gmt.zfill(2) + "00)"
            dateStr = (dateList[1] + dateList[2]).strip()
            dateObj = datetime.datetime.strptime(dateStr, '%d/%m/%Y %H:%M (GMT%z)')

        return ArticlesItem(title=title, content=content, byline=byline, updated_date=dateObj)