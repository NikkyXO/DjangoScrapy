# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from properties.models import Book, Property

class ScraperItemBook(DjangoItem):
    # define the fields for your item here like:
    django_model = Book
 
 
class ScraperItemProperty(DjangoItem):
    django_model = Property
