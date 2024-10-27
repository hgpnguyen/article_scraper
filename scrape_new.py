import sys
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from articles.items import ArticlesItem
from articles.spiders.cnn import CnnSpider
from articles.spiders.vnexpress import VnexpressSpider
from urllib.parse import urlparse
from scrapy.utils.project import get_project_settings

from scrapy.signalmanager import dispatcher

def main():
    results = []
    def crawler_results(signal, sender, item, response, spider):
        results.append(item)

    dispatcher.connect(crawler_results, signal=signals.item_scraped)

    args = sys.argv
    url = args[1]
    domain = urlparse(url).netloc
    spiderDict = {
        'edition.cnn.com': CnnSpider,
        'vnexpress.net': VnexpressSpider
    }
    process = CrawlerProcess(get_project_settings())
    if domain in spiderDict:
        process.crawl(spiderDict[domain], start_url=url)
        process.start()
    else:
        print("There is no spider to crawl this website")
    return results

if __name__ == "__main__":
    print(main())