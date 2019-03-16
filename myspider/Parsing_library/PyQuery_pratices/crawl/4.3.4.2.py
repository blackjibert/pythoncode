from pyquery import PyQuery as pq

doc = pq(url='https://www.toutiao.com/')
print(doc('title').text())

# 和上面的是一样的
# import requests
#
# doc = pq(requests.get('https://www.toutiao.com/').text)
# print(doc('title'))
