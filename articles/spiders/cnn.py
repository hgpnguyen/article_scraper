import scrapy
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
        item = ArticlesItem(title=title, content=content)
        return item
