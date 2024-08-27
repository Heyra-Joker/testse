# -*- encoding: utf-8 -*-


import base64
import hashlib

a = "yP2FmKwolWvY68B_tcjoRw=="

a = a.replace("-","+").replace("_", "/")
b = base64.b64decode(a.encode('utf-8'))
print(hashlib.md5(b).hexdigest())
