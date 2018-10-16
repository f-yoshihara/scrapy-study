import scrapy

class TutorialItem(scrapy.Item):
    text   = scrapy.Field()
    author = scrapy.Field()
    date   = scrapy.Field()