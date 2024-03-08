# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import datetime
import re


class FoxscrapperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        # Format date field
        # if 'date' in adapter:
        #     date_str = adapter['date'].strip().rstrip('\n')
        #     try:
        #         # Parse the date string using the format you provided
        #         adapter['date'] = datetime.strptime(date_str, '\n          %B %d, %Y %I:%M%p EST\n        ').strftime('%Y-%m-%d %H:%M:%S')
        #     except ValueError:
        #         adapter['date'] = None  # Or keep the original string
       
        return item

        
 
