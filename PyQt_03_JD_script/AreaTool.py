# -*- coding=utf-8 -*-
from jdlogger import logger

'''
测试 https://c0.3.cn/stock?skuId=100003406321&area=19_1607_4773_0&venderId=1000000946&buyNum=1&choseSuitSkuIds=&cat=9192,9197,12588&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=jd_7c3992aa27d1a&pduid=1580535906442142991701&ch=1&callback=jQuery4291064
请看教程寻找自己的url
'''
url = 'https://c0.3.cn/stock?skuId=100009613538&area=2_2825_51940_0&venderId=1000002350&buyNum=1&choseSuitSkuIds=&cat=652,12345,12807&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=songpeng22&pduid=15834232508191055034127&ch=1&callback=jQuery249470'
skuId = url.split('skuId=')[1].split('&')[0]
area = url.split('area=')[1].split('&')[0]
logger.info('你的area是[ %s ]，链接的商品id是[ %s ]', area, skuId)
