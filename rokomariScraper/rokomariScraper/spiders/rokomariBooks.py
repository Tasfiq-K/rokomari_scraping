import scrapy


class RokomaribooksSpider(scrapy.Spider):
    name = "rokomariBooks"
    allowed_domains = ["www.rokomari.com"]
    start_urls = ["https://www.rokomari.com/book/publishers?ref=sm_p2"]

    def parse(self, response):
        links = response.css(".authorList a::attr(href)").getall()

        if links:
            for link in links:
                yield response.follow(link, callback=self.parse_publishers)

        next_page = response.css("a:nth-child(13)::attr(href)").get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_publishers(self, response):
        book_links = response.css(".book-list-wrapper a::attr(href)").getall()

        if book_links:
            for book_link in book_links:
                yield response.follow(book_link, callback=self.parse_books)

        next_page = response.css("a:nth-child(7)::attr(href)").get()

        if next_page:
            yield response.follow(next_page, callback=self.parse_publishers)

    def parse_books(self, response):
        pass
