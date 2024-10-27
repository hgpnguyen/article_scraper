import scrapy
import datetime
import re
from bs4 import BeautifulSoup

from articles.items import ArticlesItem

class CnnSpider(scrapy.Spider):
    name = "cnn"
    allowed_domains = ["edition.cnn.com"]
    #start_urls = ["https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html"]

    def __init__(self, start_url=None, *args, **kwargs):
        super(CnnSpider, self).__init__(*args, **kwargs)
        self.start_urls = [start_url]


    def parse(self, response):
        title = response.css("div.headline__wrapper > h1#maincontent::text").get().strip()
        content = ""
        articleContain = response.css("div.article__content")
        content = BeautifulSoup(articleContain.get(), 'html.parser').get_text().strip()

        byline = response.css("span.byline__name::text").get()

        dateStr = response.css("div.timestamp::text").get().strip()
        pattern = r'(?P<hour>\d+):(?P<minute>\d+) (?P<A_PM>\w\w) \w+, \w+ (?P<month>\w+) (?P<day>\d+), (?P<year>\d+)'
        match = re.search(pattern, dateStr)
        print(match)
        if match:
            hour, minute, a_pm = int(match.group('hour')), int(match.group('minute')), match.group('A_PM')
            month, day, year = match.group('month'), int(match.group('day')), match.group('year')
            month = month[:3]
            formattedDateStr = f'{hour:02}:{minute:02} {a_pm}, {month} {day:02}, {year}'
            dateObj = datetime.datetime.strptime(formattedDateStr, '%I:%M %p, %b %d, %Y')
        else:
            dateObj = dateStr

        item = ArticlesItem(title=title, content=content, byline=byline, updated_date=dateObj)
        return item
