## To get all the publisher links in a page
response.css(".authorList a::attr(href)").getall()

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
