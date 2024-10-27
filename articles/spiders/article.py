import scrapy
from typing import Iterable
from scrapy_splash import SplashRequest 

from articles.items import ArticlesItem

lua_script = """
    function main(splash, args)  
      splash:go(args.url)
    
      -- custom rendering script logic...
      
      return splash:html()
    end
    """

"""
Using Splash to bypass 401 error but can't get content due to geo capcha delivery. Leave it for later
"""

class ArticleSpider(scrapy.Spider):
    name = "article"
    allowed_domains = ["www.nytimes.com"]
    start_urls = ["https://www.nytimes.com/2020/09/02/opinion/remote-learning-coronavirus.html?action=click&module=Opinion&pgtype=Homepage"]

    def start_requests(self) -> Iterable[SplashRequest]:
        for url in self.start_urls:
            yield SplashRequest(
                url, callback=self.parse, endpoint="execute", args={"lua_source": lua_script, 'wait': 1}, 
            )


    def parse(self, response):
        
        article = ArticlesItem()
        titleHtml = response.css("article#id > header > h1")
        title = titleHtml.css("::text").get()
        print(response.body)
        article['title'] = title
        return article
