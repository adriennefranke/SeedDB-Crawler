# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst

def process_item(value):
    value = value[0]
    return value.strip()

class SeedDB2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    accelerator = scrapy.Field(
        output_processor=TakeFirst()
        )
    accelerator_website = scrapy.Field(
        output_processor=TakeFirst()
        )
    num_cohorts = scrapy.Field(
        output_processor=process_item
        )
    num_exits= scrapy.Field(
        output_processor=process_item
        )
    num_funding = scrapy.Field(
        output_processor=process_item
        )
    num_avg_funding = scrapy.Field(
        output_processor=process_item
        )
    crunchbase_link = scrapy.Field(
        output_processor=process_item
        )
    cohort_status = scrapy.Field(
        output_processor=process_item
        )
    cohort_name = scrapy.Field(
        output_processor=process_item
        )
    cohort_date = scrapy.Field(
        output_processor=process_item
        )
    cohort_exit = scrapy.Field(
        output_processor=process_item
        )
    cohort_funding = scrapy.Field(
        output_processor=process_item
        )
    birthed_from = scrapy.Field(
        output_processor=process_item
        )

    # AcceleratorExits = scrapy.Field()
    # Startup = scrapy.Field()
    # StartupCrunchBaseLink = scrapy.Field()
    # StartupLocation = scrapy.Field()
    # StartupCategories = scrapy.Field()
# class CrunchBaseItem(scrapy.Item):
#     crunchbase_link = scrapy.Field(
#         output_processor = process_item
#         )
    # startup_headquarters = scrapy.Field()
    # startup_categories = scrapy.Field()
    # startup_desc = scrapy.Field()


    pass
