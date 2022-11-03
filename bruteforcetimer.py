import hashlib
import string
import random
import time
import bcrypt
from itertools import chain, product

def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))


a = ''.join(random.choices(string.ascii_lowercase, k = 4))

a_hash_md5 = hashlib.md5(a.encode()).hexdigest()
a_hash_sha512 = hashlib.sha512(a.encode()).hexdigest()
salt = bcrypt.gensalt(rounds = 4)
a_hash_bcrypt = bcrypt.hashpw(a.encode(), salt)
print(a_hash_bcrypt)


start_time = time.time()
for attempt in bruteforce(string.ascii_lowercase, 4):
    attempt_hash = hashlib.md5(attempt.encode()).hexdigest()
    if attempt_hash == a_hash_md5:
        print(attempt)
        break
print("md5: %s Sekunden" % (time.time() - start_time))

start_time = time.time()
for attempt in bruteforce(string.ascii_lowercase, 4):
    attempt_hash = hashlib.sha512(attempt.encode()).hexdigest()
    if attempt_hash == a_hash_sha512:
        print(attempt)
        break
print("sha512: %s Sekunden" % (time.time() - start_time))

start_time = time.time()
for attempt in bruteforce(string.ascii_lowercase, 4):
    if bcrypt.checkpw(attempt.encode(), a_hash_bcrypt):
        print(attempt)
        break
print("bcrypt: %s Sekunden" % (time.time() - start_time))

print("ende")
