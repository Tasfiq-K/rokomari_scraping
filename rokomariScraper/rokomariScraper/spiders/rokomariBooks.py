import scrapy


class RokomaribooksSpider(scrapy.Spider):
    name = "rokomariBooks"
    allowed_domains = ["www.rokomari.com"]
    start_urls = ["https://www.rokomari.com/book/publishers?ref=sm_p2"]

    def parse(self, response):
        pass

    def parse_publishers(self, response):
        pass

    def parse_info(self, response):
        pass
