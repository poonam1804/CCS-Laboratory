import hashlib 

data="poonam"

resultSHA=hashlib.sha256(data.encode())
print("Results for SHA",resultSHA)
print(resultSHA.hexdigest())