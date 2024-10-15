## To get all the publisher links in a page
response.css(".authorList a::attr(href)").getall()
publisher_links_per_page = response.xpath('//a[h2]/@href').getall()

next_page = response.xpath('//a[contains(text(), "next")]/@href').get()
book_links = response.xpath('//a[contains(text(), "Details")]/@href').getall()
books_page = response.xpath('//a[i[contains(@class, "chevron-right")]]/@href').get()

## product page

-> book title = response.css("h1::text").get().strip()
-> author name = response.css(".details-book-info__content-author a::text").get().strip()
-> categories = response.css(".details-book-info__content-category .ml-2::text").get().strip()
-> n_ratings = int(response.css(".details-book-info__content-rating .ml-2::text").get().strip().split()[0]) # only gets the number
-> n_review = response.css(".ml-2 a::text").get().strip()
-> price = int(response.css(".sell-price::text").get().strip().split()[1].replace(",", ""))
-> publisher = response.css(".item a::text").get().strip()
-> isbn = int(response.css(".item~ .item+ .item .circle+ p::text").get().strip())
-> summaray = response.css("#js--summary-description::text").get()
-> rating = float(response.css(".summary-title::text").get())
-> prod_img_link = response.css(".look-inside::attr(src)").get()

## going to the next page

-> next_page = response.css("a:nth-child(13)::attr(href)").get()

## going to the next page (while visiting publishers)
-> response.css("a:nth-child(7)::attr(href)").get()
## getting all the book links from a page (while visiting a publisher)
-> response.css(".book-list-wrapper a::attr(href)").getall()

book_title = response.xpath('//h1/text()').get().stip()
author_name = response.xpath('//p[span[contains(text(), "by")]]/a/text()').get()
publishers = response.xpath('//div[p[contains(text(), "Publication")]]/a/text()').get()
edition =  response.xpath('//div[p[contains(text(), "Edition")]]/p/text()').getall()[1]
isbn = response.xpath('//div[p[contains(text(), "ISBN")]]/p/text()').getall()[1].strip()
category = category_text = response.xpath('//div[span[contains(text(), "Category")]]/a/text()').get()
summary_text = response.xpath('//div[contains(@id, "summary")]/text()').getall() # list of strings
availability = response.xpath('//span[contains(@id, "not-available")]/text()').get()
obj = response.xpath('//script[@type="application/ld+json"]/text()').getall()[0]
obj = response.xpath('//script[contains(@type, "ld+json")]/text()').getall()[0] # better
js_obj = json.loads(obj)
image = js_obj['image]
price = js_obj['prce]


if js_obj["aggregateRating"]:
    rating = js_obj["aggregateRating"]['ratingValue']
    rating_count = js_obj['ratingCount']
    review_count = js_obj['reviewCount']
publishers_eng = js_obj['brand]
category_eng = js_obj['category']
if js_obj["offers"]:
    offer_price = js_obj['offers']['price']