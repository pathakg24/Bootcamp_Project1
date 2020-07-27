from scrapy import Spider, Request
from cricleague.items import CricleagueItem


class CricleagueSpider(Spider):
    name = 'cricleague_spider'
    allowed_urls = ['https://www.espncricinfo.com/']
    start_urls = ['https://stats.espncricinfo.com/ci/engine/records/averages/batting.html?id=12741;type=tournament']


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
            no = row.xpath('./td[4]//text()').extract_first()
            runs = row.xpath('./td[5]//text()').extract_first()
            hs = row.xpath('./td[6]//text()').extract_first()
            ave = row.xpath('./td[7]//text()').extract_first()
            bf = row.xpath('./td[8]//text()').extract_first()
            sr = row.xpath('./td[9]//text()').extract_first()
            hundreds = row.xpath('./td[10]//text()').extract_first()
            fiftys = row.xpath('./td[11]//text()').extract_first()
            zeros = row.xpath('./td[12]//text()').extract_first()
            fours = row.xpath('./td[13]//text()').extract_first()
            sixs = row.xpath('./td[14]//text()').extract_first()
            


            item = CricleagueItem()
            item['player'] = player
            item['mat'] = mat
            item['inns'] = inns
            item['no'] = no
            item['runs'] = runs
            item['hs'] = hs
            item['ave'] = ave
            item['bf'] = bf
            item['sr'] = sr
            item['hundreds'] = hundreds
            item['fiftys'] = fiftys
            item['zeros'] = zeros
            item['fours'] = fours
            item['sixs'] = sixs
            yield item