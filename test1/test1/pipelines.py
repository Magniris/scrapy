# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class Test1Pipeline(object):
    def process_item(self, item, spider):
        return item

class CsvWriterPipeline(object):

    def __init__(self):
        self.csvwriter = csv.writer(open('items.csv', 'wb'))

    def process_item(self, items, dmoz_spider):
    	descs = str(items['desc'][1]).strip()
    	self.csvwriter.writerow([items['title'][0], items['link'][0], descs])
        print "TEST: " + descs
        return items
