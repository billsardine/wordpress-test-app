import time
import requests

print('Generating load to wp lb and web servers')

i = 1
cycles = 1

while i == 1 :
    response = requests.get('http://wp-web-lb')
    web1response = requests.get('http://wp1-web/cgi-bin/db-dump-tool.py')
    web2response = requests.get('http://wp2-web/cgi-bin/db-dump-tool.py')
    print('Cycle Number ',cycles)
    cycles = cycles + 1
    time.sleep(10)
