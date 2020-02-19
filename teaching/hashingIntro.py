# hello tafida
# SHA-1
# SHA-256
# SHA-512
import hashlib

password = "ab"
password_hash = hashlib.sha1(password.encode("utf8")).hexdigest()
print(password_hash)
