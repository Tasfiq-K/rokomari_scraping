import scrapy
from ..items import RokomariscraperItem


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
        title = (
            response.css("h1::text").get().strip()
            if response.css("h1::text")
            else "No Title"
        )
        author = (
            response.css(".details-book-info__content-author a::text").get().strip()
            if response.css(".details-book-info__content-author a::text")
            else "No Author"
        )
        categories = (
            response.css(".details-book-info__content-category .ml-2::text")
            .get()
            .strip()
            if response.css(".details-book-info__content-category .ml-2::text")
            else "No Categories"
        )
        n_ratings = (
            
            response.css(".details-book-info__content-rating .ml-2::text")
            .get()
            .strip()
            .split()[0]
            if response.css(".details-book-info__content-rating .ml-2::text")
            else "No Ratings"
        )
        n_reviews = (
            response.css(".ml-2 a::text").get().strip()
            if response.css(".ml-2 a::text")
            else "No Reviews"
        )
        price = (
            int(
                response.css(".sell-price::text")
                .get()
                .strip()
                .split()[1]
                .replace(",", "")
            )
            if response.css(".sell-price::text")
            else 0
        )
        publisher = (
            response.css(".item a::text").get().strip()
            if response.css(".item a::text")
            else "No Publisher"
        )
        isbn = (
            response.css(".item~ .item+ .item .circle+ p::text").get().strip()
            if response.css(".item~ .item+ .item .circle+ p::text")
            else "No ISBN"
        )
        summaray = (
            response.css("#js--summary-description::text").get()
            if response.css("#js--summary-description::text")
            else "No summary"
        )
        rating = (
            float(response.css(".summary-title::text").get())
            if response.css(".summary-title::text")
            else 0.0
        )
        prod_img_link = (
            response.css(".look-inside::attr(src)").get()
            if response.css(".look-inside::attr(src)")
            else "No image"
        )
