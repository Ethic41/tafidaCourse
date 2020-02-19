import hashlib

def main():
  user_input = input("Welcome to my function, enter ur name:\n")
  greet_user(user_input)
  
def greet_user(username):
  hash_username = hashlib.sha1(username.encode("utf8")).hexdigest()
  print(f"hello {username}")
  print(f"the hash of ur username is {hash_username}")

main()