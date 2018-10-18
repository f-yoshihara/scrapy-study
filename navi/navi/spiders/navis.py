import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from navi.items import NaviItem
import re
from bs4 import BeautifulSoup

def strip_html_tags(raw_html):
    tagcleanr = re.compile('<.*?>')
    tagcleantext = re.sub(tagcleanr, '', raw_html)
    spacecleantext = tagcleantext.replace(' ', '')
    return spacecleantext

class NavisSpider(scrapy.Spider):
    name = 'navis'
    allowed_domains = ['gakusai-navi.jp']
    start_urls = ['http://gakusai-navi.jp/highschool/experience/index/']

    rules = (
        Rule(LinkExtractor(), callback='parse')
    )

    def parse(self, response):
        self.logger.info('parse: %s', response.url)
        # for navi in response.css('tbody'):
        #     item = NaviItem()
        #     item['name']     = navi.xpath('//td[1]/text()').extract_first()
        #     item['overview'] = navi.xpath('//td[2]/text()').extract_first()
        #     item['url']      = navi.css('td a::attr(href)').extract_first()
        #     item['date']     = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
        

# start----------------------------------------------------------------------------------------------------------------------------

    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = 'quotes-%s.json' % page
    #     with open(filename, 'wb') as f:
    #         json.dump(response.body, f)
    #     self.log('Saved file %s' % filename)

    # def parse_item_entiresite(self, response):
    #     self.logger.info('parse_item: %s', response.url)
    #     filename = response.url.split("/")[-2] + '.html'
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)

    # def parse_item(self, response):
    #     # only process this type of page: http://unofficialism.info/posts/xxx/
    #     self.logger.info('parse_item: %s', response.url)
    #     r = re.compile("http://unofficialism.info/posts/([0-9a-zA-Z-_]+)/$")
    #     o = r.findall(response.url)       
    #     if len (o) > 0:
    #         ## value from title in body
    #         ## <h1 class="twelve columns page_heading">de:code 2017 DI08 – Azure Searchセッションフォローアップ</h1>
    #         title = response.css('h1.twelve.columns.page_heading::text').extract_first()
    #         self.logger.info('parsed title=%s', title)
    #         content_html = response.css('div.twelve.columns').extract_first()

    #         ## manual strip by strip_html_tags 
    #         #self.logger.info('parsed content=%s', strip_html_tags(content_html))

    #         ## strip by BeautifulSoup
    #         bs = BeautifulSoup(content_html, "html.parser")
    #         content = bs.text
    #         #self.logger.info('parsed content=%s', content)
            
    #         date = response.css('span.date::text').extract_first()
    #         self.logger.info('parsed date=%s', date)

    #         item = UnofficialismspiderItem()
    #         item['title'] = title
    #         item['url'] = response.url
    #         item['content'] = content
    #         item['date'] = date
    #         yield item

# end----------------------------------------------------------------------------------------------------------------------------