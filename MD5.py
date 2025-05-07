import hashlib 

data="poonam"

resultMD5=hashlib.md5(data.encode())
print("Results for MD5",resultMD5)
print(result.hexdigest())