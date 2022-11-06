import hashlib
value = b"passward"

vvalue = "111111"
value_md5=hashlib.md5(value)
value_hex=value_md5.hexdigest()
value_bin=value_md5.digest()

en = hashlib.md5(vvalue.encode()).hexdigest()
print(value)
print(value_md5)
print(value_hex)
print(value_bin)
print(en)

# wargame.kr md5() passward
for i in range(0, 10000000):
    if b"'='" in hashlib.md5(str(i).encode()).digest():
        print("Found: {}".format(i))

# wargame.kr md5() compare
# md5('240610708') == md5('QNKCDZO')