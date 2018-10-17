# scrapy runspider quotes_json_spider.py
import scrapy
import json

class QuotesJsonSpider(scrapy.Spider):
    name = "quotes_json"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.json' % page
        with open(filename, 'wb') as f:
            json.dump(response.body, f)
        self.log('Saved file %s' % filename)

        
# with open('data.json', 'w') as outfile:
    