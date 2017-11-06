import time
import requests
from concurrent.futures import ThreadPollExecutor


Number = range(12)
url = 'http://httpbin.org/get?a={}'


def fetch(a):
    r = requests.get(url.format(a))
    return r.json()['args']['a']


start = time.time()
with ThreadPollExecutor(max_workers=3) as executor:
    for num, result in zip(Number, executor.map(fetch, Number)):
        print('fetch({}) = {}'.format(num, result) )

print('user time :{}'.format(time.time()-start))