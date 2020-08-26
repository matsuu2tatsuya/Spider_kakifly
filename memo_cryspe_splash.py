class CryspeSpider(scrapy.Spider):
    name = 'cryspe_splash'
    allowed_domains = ['cryptospells.jp/trades']
    start_urls = ['https://cryptospells.jp/trades/']

    def start_requests(self):
        script = """
        function main(splash, args)
            local num_scrolls = 25
            local scroll_delay = 0.5
            local scroll_to = splash:jsfunc("window.scrollTo")
            local get_body_height = splash:jsfunc(
                "function() {return document.body.scrollHeight;}"
            )
            assert(splash:go(splash.args.url))
            assert(splash:wait(0.5))
            local area = splash:select('.checkmark')
            area:click()
            assert(splash:wait(0.5))

        for _ = 1, num_scrolls do
                scroll_to(0, get_body_height())
                splash:wait(scroll_delay)
            end
            return {
                html = splash:html(),
                png = splash:png(),
                har = splash:har(),
            }
        end
                """
        yield SplashRequest(url='https://cryptospells.jp/trades/', callback=self.parse, endpoint='execute',
                            args={'lua_source': script})

        # yield SplashRequest(url=url, callback=self.parse, args={"wait": 3})

    def parse(self, response):
        for res in response.xpath('//div[@class="col-4 col-sm-2 col-sm-2--half col-card"]'):
            cryspe_items = Cryptospells_Item()
            base_URL = 'https://cryptospells.jp'

            cryspe_items['name'] = None

            ID_path = res.css('[class="serial-number serial-number-user-img-wrapper"]').xpath('string()').get()
            ID_path2 = re.sub(r'# ', '', ID_path)
            cryspe_items['ID'] = re.sub(r' ', '', ID_path2)

            cryspe_items['price_ETH'] = None
            SPL_path = res.css('[class="price"]').xpath('string()').get()
            SPL_path2 = re.sub(r' SPL', '', SPL_path)
            cryspe_items['price_SPL'] = re.sub(r',', '', SPL_path2)
            cryspe_items['price_JPY'] = None

            cryspe_items['buy_transaction_URL'] = base_URL + res.css('a::attr("href")').re_first(r'/trades/\d+$')
            cryspe_items['sell_transaction_URL_ETH'] = None
            cryspe_items['buy_transaction_URL_JPY'] = None

            cryspe_items['image_URL'] = res.css('img[src$="png"]::attr("src")').get()

            yield cryspe_items

