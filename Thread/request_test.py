import requests
import time


url = 'http://127.0.0.1:8011/api/index/new/v4?device_id=44838D82-CA60-4438-8A02-9095BED2F67B&start_num=1&version=7.2.5'

start_time = time.time()

for i in range(30):
    r = requests.get(url)
    print(r)

print(time.time() - start_time)