#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Hamdi
import urllib
import urllib2

from lxml import etree


class Spider:

    def run(self):
        url =  'https://careers.tencent.com/search.html'
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "cookie": "ga = GA1.2.557595732.1563001651",
        }
        request = urllib2.Request(url, headers=headers)
        html = urllib2.urlopen(request)

        content = etree.HTML(html)

        job_titles = content.xpath('//h4[@class="recruit-title"]')
        print job_titles



if __name__ == '__main__':
    spider = Spider()
    spider.run()
