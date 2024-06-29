from django.core.management.base import BaseCommand
from scraper.scraper.spiders.property_spider import PropertySpider
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from scraper.scraper import settings as my_settings



class Command(BaseCommand):
    help = 'Release spider'

    def handle(self, *args, **options):
        crawler_settings = Settings()
        crawler_settings.setmodule(my_settings)

        process = CrawlerProcess(settings=crawler_settings)

        process.crawl(PropertySpider)
        process.start()