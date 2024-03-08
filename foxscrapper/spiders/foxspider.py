import scrapy


class FoxspiderSpider(scrapy.Spider):
    name = "foxspider"
    allowed_domains = ["foxbusiness.com"]
    start_urls = ["https://www.foxbusiness.com/category/fox-news-health?page=1"]

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
        yield {
            'title': response.xpath('.//h1[@class="headline"]//text()').get(),
            'subtitle': response.xpath('.//h2[@class="sub-headline"]//text()').get(),
            'text': text,
            'time': response.xpath('.//time//text()').get(),
        }
    #    category not on page

