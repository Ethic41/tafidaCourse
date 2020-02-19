# this function is our entry point
# we will collect user_input and
# call the function to generate password
# candidate
import hashlib
from string import ascii_lowercase

charset = ascii_lowercase


def main():
    user_hash = input("###[Welcome to SHA-Cracker v1.0]###\nPlease Enter the Hash[SHA-1 only]:\n")
    generate(6, charset, user_hash)


def generate(target_length: int, charset: str, user_hash, count=1, output=""):
    for char in charset:
        if count == target_length:
            # yield output+char
            pass_candidate = output+char
            if crack(user_hash, pass_candidate):
                print(f"====[Password Cracked Successfully, plaintext for {user_hash} is '{pass_candidate}']====")
                exit()
        
        if count != target_length:
            generate(target_length, charset, user_hash, count+1, output=f"{output}{char}")


def crack(user_hash, pass_candidate):
    if hashlib.sha1(pass_candidate.encode("utf8")).hexdigest() == user_hash:
        return True
    return False

main()