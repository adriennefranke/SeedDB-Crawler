import scrapy
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from webscrape2.items import SeedDB2Item
# from webscrape2.items import CrunchBaseItem
from lxml import html
import requests



class SeedDBSpider(CrawlSpider):
    name = "SeedDB"
    allowed_domains = ['seed-db.com', 'crunchbase.com']
    start_urls = [
        "http://www.seed-db.com",
    ]
    
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//a[@class="btn btn-lg btn-success"][1]'), follow=True, callback='parse_accelerator'),
        Rule(LinkExtractor(allow=r'http://www\.seed-db\.com/accelerators/view\?acceleratorid=\d+'), follow=True, callback='parse_accelerator_page'),
        
        )

    def parse_accelerator(self, response):
        for sel in response.xpath('//table/tbody/tr'):
            l = ItemLoader(item=SeedDB2Item(), selector=sel)
            l.add_xpath('accelerator', 'td/a/strong/text()')
            l.add_xpath('accelerator_website', 'td/a/@href')
            l.add_xpath('num_cohorts', 'td[3]/span/text()')
            l.add_xpath('num_exits', 'td[4]/span/text()')
            l.add_xpath('num_funding', 'td[5]/span/text()')
            l.add_xpath('num_avg_funding', 'td[6]/span/text()')
            yield l.load_item()

    # i think we need to do a request and response thing here in order for it to crawl those webpages
    def parse_accelerator_page(self, response):
        for sel in response.xpath('//tbody/tr'):
            l = ItemLoader(item=SeedDB2Item(), selector=sel)
            l.add_xpath('crunchbase_link', 'td[2]/a/@href')
            l.add_xpath('cohort_status', 'td/button/text()')
            l.add_xpath('cohort_name', 'td[2]/a/strong/text()')
            l.add_xpath('cohort_date', 'td[4]/span/text()')
            l.add_xpath('cohort_exit', 'td[5]/span/text()' )
            l.add_xpath('cohort_funding', 'td[7]/span/text()')
            l.add_xpath('birthed_from', '')
            # print l.load_item()
            yield l.load_item()


    #need to edit third rule in order for this to work
    # def parse_crunchbase_page(self, response):
        #for sel in response.xpath('//div[@id="info-card-overview-content"]/div/dl/div[2]'):
    #         l = ItemLoader(item=CrunchBaseItem(), selector=sel)
    #         l.add_xpath('startup_headquarters', 'dd[1]/a/text()')
    #         l.add_xpath('startup_categories', 'dd[4]/a/text()')
    #         l.add_xpath('startup_desc', 'dd[2]/text()')
    #         yield l.load_item()





