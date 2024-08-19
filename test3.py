import base64
import datetime
import json
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA1

def get_signed_url(url, key_pair_id, private_key_string, expire_date):
    def rsa_sign(plain_text, private_key):
        key = RSA.importKey(private_key)
        signer = PKCS1_v1_5.new(key)
        digest = SHA1.new(plain_text)
        return signer.sign(digest)

    def url_safe_base64_encode(data):
        return base64.urlsafe_b64encode(data).decode('utf-8')

    expire_date_epoch = int((expire_date - datetime.datetime(1970, 1, 1)).total_seconds())
    policy = {
        "Statement": [
            {
                "Resource": url,
                "Condition": {
                    "DateLessThan": {"AWS:EpochTime": 1725303717}
                }
            }
        ]
    }
    policy_json = json.dumps(policy).replace(" ", "").encode('utf-8')
    print(policy_json)
    policy_b64 = url_safe_base64_encode(policy_json)
    signature = rsa_sign(policy_json, private_key_string)
    signature_b64 = url_safe_base64_encode(signature)

    signed_url = f"{url}?Policy={policy_b64}&Signature={signature_b64}&Key-Pair-Id={key_pair_id}"
    return signed_url

# 使用示例
url = "https://ts2.hjbd81.top/hjstore/video/20231127/1e64e31314bf3ef03b61eb4bf034d3bc/6697367dKrdzVFa_i24.ts"
key_pair_id = "K4NBQA24QVP0Y"
private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAlcSnBoCfspbJ61SjCnGr7cbBsuBvNarCwQuNVnR/t8Q0t0Cd
II4BiNplxW4tBgCcZGgA8mOuj/ePKRe2SsTrUDE0yt17rCcKmmvfge+2zCjGOj7Z
N+EM+fNgrpLCnrQNeJuoMdu2ZCVy0hWk4+2E3+Q9P7kBbIMM6AqcIygnatqY03ZM
uiHLhlZ4RDWyPFSuQZ8bBHteppnuOzRyQG+HgWVqExjeNoXEAmI0xekDXAWmatCc
qKNPSZFflMoK06QWRVaLrA3+laxS0VYr9HdzGI4EybdQqzlxtUxEFbwSDeKI0c+A
Tov1AFaqIdDFtxF2CFcGSHCYEEdTjufgEvLfYQIDAQABAoIBAFAckPt5cfMllXy8
GTpM85qM5q+4PcSHQwXgGApW5rp1yXz8ow/25fs+V5H0DUFYsk9DEr6Vc5qu4XUp
qej0zKpop8ScFLtRZuqTKUtn3m/2n5IobCjnyPkqply7RD+AMHSDTsTcsgN/xJt7
2GfTdXANtnWPkKNqtkyo4DwuDmepDmGjLOlA8QNtxTVkMVDKjNtX5FNKT6cOhrF7
z3zEy4+WdJlVrw+QJ1sSLVoxhR9+Q3T6pGNnPf6MCz8w36vuwFj5BVgGLIrKBtIt
NtoiokOusBYWB1YdTQa1suYuzCjV8cyisaho3JYbwzg9BlzcWfqbsoi51l6BUNYi
NdkucAECgYEA+4YtPhPCQcs6UTWWLbFE7c2hFfEFtOKB1zXepFAEjziILkZ4nMGn
sw/qp7uQttUTd6dr5hRNq+ripnfDxy5FNJOW+mJpSOqJU4gkjzThBl16VC9UGApX
dRRm8ecSlqLVBylpHDvQpbOT6K0Ys4yRqYNlUznmk4SjCDfUqr2c1PECgYEAmG7s
pWbTuG+Ftt229DUYph7lmjN783uqZF6zYzM4UQ1giHLu8hUuDVwjmN4v4HD0f3ol
yLRDomSRcPCnKdjoyCqcaRYmIwZ1ecN/XOYxYg1Tkx/GrBicj1ovy7pGgAk9rzUL
Yj1NU0es9HyLrm2L5oYwHR3fM7BGH+//m7hi8XECgYBUXFt+T6g+4wfrRvrY1nUV
AXv+3PkaA0KjSQkkuUXeN4rNYot/oCA8GaGNooZWHD9MSZYR9Etc1wov5Ul/29AQ
Y1QnJKzFbQykPKxub8Dtnpqx87HT4lwVA8PHbMY6SeEDZus/Mfy4JvP7/Vqklggg
/9YTRP9GCR2ZWwh0P+aDMQKBgGNEgXnpb+GBRuvikT2Rwl6UamO0OXlDxKAeh+YH
OhqWgpH5fyBJqLbslQX9U+JuzNqjei2tLwp3QbvyDHqVFmscTMWmtelDUIeeR7gA
9JHtKcr6+4+ha3tzeQLMaRMCcZhDDAnK8CtW1wxUe0Z5co0KQBUGGg/4MIKl8ajA
ODcRAoGBAKISlrd9TXXtIQhIsYgGluCUCRy9GUKJEUfsvSZY8KbW5yVghxaDBZxY
YOEgeIB+YKALRJ7vp3SS372MhnrRzYbHXtaKz2HGTwZITnhm+NDyRZGMIetYd98C
WXisi3eHgdALpTd024csIK9PQ9HWt2FCYdv7QOTisnPFisrn9wN5
-----END RSA PRIVATE KEY-----
"""
expire_date = datetime.datetime(2024, 8, 1, 12, 0)

signed_url = get_signed_url(url, key_pair_id, private_key_string, expire_date)
print(signed_url)