# SeedDB-Crawler

I created this crawler to crawl SeedDB.com in an eductaional research setting only and to learn how to use Scrapy. Feel free to contact me at adriennefranke@gmail.com

For this spider to work you will need...
In a virtualenv, install Scrapy, install requests, and install lxml

To get the spider to crawl:
cd into project folder in terminal, activate virtualenv, type "scrapy crawl SeedDB" in terminal

To crawl the spider and export items to csv:
cd into project folder in terminal, activate virtualenv, type "scrapy crawl SeedDB -o items.csv" 

The items.csv will show up in your project folder
