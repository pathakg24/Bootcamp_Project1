from scrapy import Spider, Request
from bowling.items import BowlingItem


class BowlingSpider(Spider):
    name = 'bowling_spider'
    allowed_urls = ['https://www.espncricinfo.com/']
    start_urls = ['https://stats.espncricinfo.com/ci/engine/records/averages/bowling.html?id=12741;type=tournament']


    def parse(self, response):

        rows = response.xpath('//table[@class="engineTable"]/tbody/tr')

        patterns = ['./td[@class="left"]/a/text()']

        for row in rows:

            for pattern in patterns:
                player = row.xpath(pattern).extract_first()
                if player:
                    break

            if not player:
                continue


            mat = row.xpath('./td[@class="padAst"]/text()').extract_first()
            inns = row.xpath('./td[3]//text()').extract_first()
            overs = row.xpath('./td[4]//text()').extract_first()
            mdns = row.xpath('./td[5]//text()').extract_first()
            runs = row.xpath('./td[6]//text()').extract_first()
            wkts = row.xpath('./td[7]//text()').extract_first()
            bbi = row.xpath('./td[8]//text()').extract_first()
            bowl_ave = row.xpath('./td[9]//text()').extract_first()
            econ = row.xpath('./td[10]//text()').extract_first()
            bowl_sr = row.xpath('./td[11]//text()').extract_first()
            fours = row.xpath('./td[12]//text()').extract_first()
            fives = row.xpath('./td[13]//text()').extract_first()
            ct = row.xpath('./td[14]//text()').extract_first()
            st = row.xpath('./td[15]//text()').extract_first()


            item = BowlingItem()
            item['player'] = player
            item['mat'] = mat
            item['inns'] = inns
            item['overs'] = overs
            item['mdns'] = mdns
            item['runs'] = runs
            item['wkts'] = wkts
            item['bbi'] = bbi
            item['bowl_ave'] = bowl_ave
            item['econ'] = econ
            item['bowl_sr'] = bowl_sr
            item['fours'] = fours
            item['fives'] = fives
            item['ct'] = ct
            item['st'] = st
            yield item