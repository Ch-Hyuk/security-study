import requests


requests.packages.urllib3.disable_warnings()
URL = 'http://ctf.j0n9hyun.xyz:2025/?page='
cnt = 1223
while(1):
    r = requests.get(URL+str(cnt))
    print(cnt)
    if "HackCTF" in r.text:
        print("FLAG: "+cnt)
        break
    cnt += 1