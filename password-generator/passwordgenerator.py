import random
import string

def generate_password(length):
    charset = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(charset, k=length))
    return password

pass_length = int(input("How long would you like the password to be?: "))

password = generate_password(pass_length)
print(password)