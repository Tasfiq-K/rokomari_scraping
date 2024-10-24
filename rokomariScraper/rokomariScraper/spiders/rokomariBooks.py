import json

import scrapy

from ..items import RokomariscraperItem


class RokomaribooksSpider(scrapy.Spider):
    name = "rokomariBooks"
    allowed_domains = ["www.rokomari.com"]
    start_urls = ["https://www.rokomari.com/book/publishers?ref=sm_p2"]

    def parse(self, response):
        publisher_links_per_page = response.xpath("//a[h2]/@href").getall()

        if publisher_links_per_page:
            for link in publisher_links_per_page:
                yield response.follow(link, callback=self.parse_publishers)

        # if there are other pages for current publisher
        publisher_next_page = response.xpath(
            '//a[contains(text(), "next")]/@href'
        ).get()

        if publisher_next_page:
            yield response.follow(publisher_next_page, callback=self.parse)

    def parse_publishers(self, response):
        # for the current publisher parse the book links
        book_links_per_page = response.xpath(
            '//a[contains(text(), "Details")]/@href'
        ).getall()

        if book_links_per_page:
            for book_link in book_links_per_page:
                yield response.follow(book_link, callback=self.parse_books)

        # if there are multiple pages for the current publisher that has books
        # grab the next page element
        books_next_page = response.xpath(
            '//a[i[contains(@class, "chevron-right")]]/@href'
        ).get()

        # if the next page exists, follow it
        if books_next_page:
            yield response.follow(books_next_page, callback=self.parse_publishers)

    def parse_books(self, response):
        items = RokomariscraperItem()

        book_url = response.url if response.url else "No Valid Url"

        title = (
            response.xpath("//h1/text()").get().strip()
            if response.xpath("//h1/text()").get()
            else "No Title"
        )
        author = (
            response.xpath('//p[span[contains(text(), "by")]]/a/text()').get().strip()
            if response.xpath('//p[span[contains(text(), "by")]]/a/text()')
            else "No Author"
        )
        categories = (
            response.xpath('//div[span[contains(text(), "Category")]]/a/text()')
            .get()
            .strip()
            if response.xpath('//div[span[contains(text(), "Category")]]/a/text()')
            else "No Categories"
        )

        publisher = (
            response.xpath('//div[p[contains(text(), "Publication")]]/a/text()')
            .get()
            .strip()
            if response.xpath('//div[p[contains(text(), "Publication")]]/a/text()')
            else "No Publisher"
        )

        isbn = (
            response.xpath('//div[p[contains(text(), "ISBN")]]/p/text()')
            .getall()[1]
            .strip()
            if response.xpath('//div[p[contains(text(), "ISBN")]]/p/text()')
            else "No ISBN"
        )

        edition = (
            response.xpath('//div[p[contains(text(), "Edition")]]/p/text()')
            .getall()[1]
            .strip()
            if response.xpath('//div[p[contains(text(), "Edition")]]/p/text()')
            else "No Edition"
        )

        availability = (
            response.xpath('//div[contains(@id, "details-btn-area")]//span/text()')
            .get()
            .strip()
            if response.xpath('//div[contains(@id, "details-btn-area")]//span/text()')
            else "Not Available"
        )

        summaray = (
            "।".join(
                response.xpath('//div[contains(@id, "summary")]/text()').getall()
            ).strip()
            if response.xpath('//div[contains(@id, "summary")]/text()')
            else "No summary"
        )

        language = (
            response.xpath(
                '//div[contains(@id, "additional-specification")]//tr[td[contains(text(), "Language")]]/td[2]/text()'
            )
            .get()
            .strip()
            if response.xpath(
                '//div[contains(@id, "additional-specification")]//tr[td[contains(text(), "Language")]]/td[2]/text()'
            )
            else "No Language"
        )

        js_obj = response.xpath('//script[contains(@type, "ld+json")]/text()').getall()[0]  # better

        if js_obj:
            json_data = json.loads(js_obj)
            prod_img_link = (
                json_data["image"] if json_data["image"] else "No image link"
            )

            price = float(json_data["price"])

            if json_data["aggregateRating"]:
                rating = float(json_data["aggregateRating"]["ratingValue"])

                n_ratings = int(json_data["aggregateRating"]["ratingCount"])
                n_reviews = int(json_data["aggregateRating"]["reviewCount"])
                publisher_name_english = json_data["brand"]
                category_english = json_data["category"]

            # offer information
            if json_data["offers"]:
                offer_price = (
                    float(json_data["offers"]["price"])
                    if json_data["offers"]["price"]
                    else 0.0
                )
        items["book_url"] = book_url
        items["isbn"] = isbn
        items["title"] = title
        items["author"] = author
        items["publisher"] = publisher
        items["publisher_name_english"] = publisher_name_english
        items["categories"] = categories
        items["category_english"] = category_english
        items["edition"] = edition
        items["availability"] = availability
        items["summary"] = summaray
        items['language'] = language
        items["rating"] = rating
        items["n_ratings"] = n_ratings
        items["n_reviews"] = n_reviews
        items["prod_img_link"] = prod_img_link
        items["price"] = price
        items["offer_price"] = offer_price

        yield items
