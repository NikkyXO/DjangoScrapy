import csv
from typing import Iterable

from scraper.scraper.items import ScraperItemBook
import scrapy
from scrapy import Request
from scrapy import signals



class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def start_requests(self) -> Iterable[Request]:
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.response_parser)

    def response_parser(self, response):
        for selector in response.css('article.product_pod'):
            item = ScraperItemBook()
            title = selector.css('h3 > a::attr(title)').extract_first()
            price = selector.css('.price_color::text').extract_first()
            item['title'] = title
            item['price'] = price
            yield item

        next_page_link = response.css('li.next a::attr(href)').extract_first()
        if next_page_link:
            yield response.follow(next_page_link, callback=self.response_parser)


# def book_spider_result():
#     books_results = []

#     def crawler_results(item):
#         item.save()
#         # print("item:  ", item)
#         books_results.append(item)

#     dispatcher.connect(crawler_results, signal=signals.item_scraped)
#     crawler_process = CrawlerProcess()
#     crawler_process.crawl(BooksSpider)
#     crawler_process.start()
#     return books_results


# if __name__ == '__main__':
#     books_data = book_spider_result()
#     print(books_data)
#     if books_data:
#         keys = books_data[0].keys()
#         with open('books_data.csv', 'w', newline='') as output_file:
#             writer = csv.DictWriter(output_file, keys)
#             writer.writeheader()
#             writer.writerows(books_data)
#     else:
#         print("No data scraped.")
