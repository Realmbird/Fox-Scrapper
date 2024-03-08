import scrapy
from foxscrapper.items import FoxscrapperItem

class FoxspiderSpider(scrapy.Spider):
    name = "foxspider"
    allowed_domains = ["foxbusiness.com"]
    start_urls = ["https://www.foxbusiness.com/category/fox-news-health?page=1"]
    page = 1
    def parse(self, response):
        articles = response.xpath('//article[@class="article article-ct"]')
        
        for article in articles:
            link = article.xpath('.//a//@href').get()

            # item = {
            #     'title': article.xpath('.//a//@aria-label').get(),
            #     'text': article.xpath('.//p//text()').get(),
            #     'time': article.xpath('.//time//text()').get(),
            #     'category': article.xpath('.//span//text()').get(),
            # }
            if link is not None:
                yield response.follow(link, callback=self.parse_article)
        
        # next_page = response.xpath('//li[class="pagi-item pagi-next"]').get()
        
        # Pagination
        self.page += 1
        next_page_url = f'https://www.foxbusiness.com/category/fox-news-health?page={self.page}'
        yield response.follow(next_page_url, callback=self.parse)
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)
        
        #   yield {
        #         'title': article.xpath('.//a//@aria-label').get(),
        #         'text': article.xpath('.//p//text()').get(),
        #         'time': article.xpath('.//time//text()').get(),
        #         'category': article.xpath('.//span//text()').get(),
        #         'link': link,

        #     }  

    def parse_article(self, response):
        
        # response.xpath('//*[@class="article-body"]//p//text()').getall()
        texts = response.xpath('.//div[@class="article-content"]//p//text()').getall()
        text = ''.join(texts)
        product_item = FoxscrapperItem()
        product_item['time'] = response.xpath('.//time//text()').get().strip()
        product_item['title'] = response.xpath('.//h1[@class="headline"]//text()').get()
        product_item['subtitle'] = response.xpath('.//h2[@class="sub-headline"]//text()').get()
        product_item['text'] = text
        
        #    category not on page
        yield product_item

