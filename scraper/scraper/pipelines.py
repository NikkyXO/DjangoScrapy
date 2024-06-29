# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from properties.models import Book
from asgiref.sync import sync_to_async
from scraper.scraper.items import ScraperItemBook



class ScraperPipelineBook:
    
    @sync_to_async
    def process_item(self, item, spider):
        print("Processing save   : ", item)
        if not Book.objects.filter(title=item['title']).exists():
            item.save()

        return item


class ScraperPipelineProperty:
    def process_item(self, item, spider):
        print("Processing save  2 : ", item)
        # item.save()
        return item