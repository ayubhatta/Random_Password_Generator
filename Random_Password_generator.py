import secrets 
import string

def create_pw(pw_length):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(pw_length))
    return password

print(create_pw(8))   # prints a random password with 8 characters
print(create_pw(10))    # prints a random password with 10 characters
# print(create_pw(12))
# print(create_pw(14))
