import requests
from pyquery import PyQuery as pq

url = 'http://www.baidu.com/s'
params = {
  'ie': 'UTF-8',
  'wd': '李开锋'
}
doc=pq(requests.get(url, params = params).text)
results = doc('h3.t a').items()
for page in results :
  print('标题：' + page.text())
  print('链接：' + page.attr('href'))
  
