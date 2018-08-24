import requests
from urllib.parse import urlencode

headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 Safari/605.1.15',
    'Host':'image.so.com',
    'X-Requested-With':'XMLHttpRequest'
}
base_url='http://image.so.com/j?'




def parse_one_page(page):
    params = {
        'q': '地球',
        'src': 'srp',
        'pn': 60,
        'ch': '',
        'sn':page*60+50,
        'ran':0,
        'ras':0,
        'cn':0,
        'gn':0,
        'kn':50,
}

    url = base_url+urlencode(params)
    print(url)
    r = requests.get(url,headers=headers)
    print(r.content)

parse_one_page(1)



