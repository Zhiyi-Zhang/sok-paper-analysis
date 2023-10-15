import scrapy
from urllib.parse import urlencode
import logging
from scraper_api import ScraperAPIClient

myheaders =  {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
        'Accept': 'application/json,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
        }
API_KEY = '5e60f000e3f5da8e370eb80de6290150'

class Scholarv1Spider(scrapy.Spider):
    name = 'scholarv1'
    allowed_domains = ['scholar.google.com', 'scraperapi.com']
    start_urls = ['http://scholar.google.com/']
    last_url = ''
    MAX_RETRIES = 3

    def __init__(self, category='', **kwargs):
        super().__init__(**kwargs)  # python3

    def get_url(self, url):
        API_KEY = '5e60f000e3f5da8e370eb80de6290150'
        client = ScraperAPIClient(API_KEY)
        proxy_url = client.scrapyGet(url)
        return proxy_url

    def parse(self, response):
        #self.pubyear = '&as_ylo=' + str(self.start_year) + '&as_yhi=' + str(self.end_year) + '&'
        #self.logger.info('Pubyear is %s', self.pubyear)
        meta = response.meta
        retries = response.meta['retry_count']
        position = response.meta['position']
        for res in response.xpath('//*[@data-rp]'):
            link = res.xpath('.//h3/a/@href').extract_first()
            temp = res.xpath('.//h3/a//text()').extract()
            if not temp:
                title = "".join(res.xpath('.//h3/span[@id]//text()').extract())
            else:
                title = "".join(temp)
            snippet = "".join(res.xpath('.//*[@class="gs_rs"]//text()').extract())
            cited = res.xpath('.//a[starts-with(text(),"Cited")]/text()').extract_first()
            temp = res.xpath('.//a[starts-with(text(),"Related")]/@href').extract_first()
            related = "http://scholar.google.com" + temp if temp else ""
            num_versions = res.xpath('.//a[contains(text(),"version")]/text()').extract_first()
            published_data = "".join(res.xpath('.//div[@class="gs_a"]//text()').extract())
            position += 1
            item = {'title': title, 'link': link, 'cited': cited, 'relatedLink': related, 'position': position,
                   'numOfVersions': num_versions, 'publishedData': published_data, 'snippet': snippet}
            yield item
        next_page = response.xpath('//td[@align="left"]/a/@href').extract_first()
        self.logger.info('Parse function called on%s', next_page)
        if next_page is not None:
            retries = 0
            url = "http://scholar.google.com" + next_page
            self.last_url = url
            yield scrapy.Request(self.get_url(url), dont_filter=True,  errback=self.handle_failure, 
                    callback=self.parse, headers=myheaders, meta={'position': position, 'retry_count': retries})
        else:
            self.logger.info('Retry!!! #' +str(retries))
            if retries < self.MAX_RETRIES:
                retries += 1
                yield scrapy.Request(self.get_url(self.last_url), dont_filter=True,  errback=self.handle_failure, 
                        callback=self.parse, headers=myheaders, meta={'position': position, 'retry_count': retries})


    def handle_failure(self, failure):
        self.log(failure, level=logging.ERROR)
        # try with a new proxy
        self.log('restart from the failed url {}'.format(failure.request.url))
        yield scrapy.Request(url=failure.request.url, callback=self.parse, errback=self.handle_failure)


    def start_requests(self):
        queries = ['\"Denial+of+Service\"']
        for query in queries:
            url = 'http://scholar.google.com/scholar?' + urlencode({'hl': 'en', 'q': query, 'as_sdt': '1', 'as_ylo': str(self.start_year), 'as_yhi': str(self.end_year)})
            yield scrapy.Request(self.get_url(url), dont_filter=True,  errback=self.handle_failure, callback=self.parse, meta={'position': 0, 'retry_count': 0}, headers=myheaders)
