from typing import Iterable
from scraper.scraper.items import ScraperItemProperty
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
import scrapy
from scrapy import Request

class PropertySpider(scrapy.Spider):
    
    name = "properties"
    allowed_domains = ["realestatedatabase.net"]
    start_urls = [
        "https://realestatedatabase.net/FindAHouse/houses-for-rent-in-kampala-uganda.aspx?Title=Houses+for+rent+in+kampala"
    ]
    
    
    def start_requests(self) -> Iterable[Request]:
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.response_parser)
            
    def response_parser(self, response):
        for selector in response.css(''):
            item = ScraperItemProperty()
            obj1 = selector.css().extract_first()
            value = selector.css().extract_first()
            item[''] = obj1
            item[''] = value
            yield item

        next_page_link = response.css('li.next a::attr(href)').extract_first()
        if next_page_link:
            yield response.follow(next_page_link, callback=self.response_parser)
