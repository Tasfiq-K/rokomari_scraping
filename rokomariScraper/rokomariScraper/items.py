# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RokomariscraperItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    categories = scrapy.Field()
    edition = scrapy.Field()
    availability = scrapy.Field()
    publisher_name_english = scrapy.Field()
    category_english = scrapy.Field()
    n_ratings = scrapy.Field()
    n_reviews = scrapy.Field()
    price = scrapy.Field()
    offer_price = scrapy.Field()
    publisher = scrapy.Field()
    isbn = scrapy.Field()
    summary = scrapy.Field()
    rating = scrapy.Field()
    prod_img_link = scrapy.Field()
    book_url = scrapy.Field()
