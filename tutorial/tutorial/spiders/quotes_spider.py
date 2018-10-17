import scrapy
import datetime
from tutorial.items import TutorialItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
            'http://quotes.toscrape.com/page/1/'
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            item = TutorialItem()
            item['text']   = quote.css('span.text::text').extract_first()
            item['author'] = quote.xpath('span/small/text()').extract_first()
            item['date']   = datetime.datetime.utcnow() + datetime.timedelta(hours=9)

        yield item

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback = self.parse)