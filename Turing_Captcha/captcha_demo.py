import random

def generate_captcha():
    return ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789", k=5))

captcha = generate_captcha()
print("CAPTCHA:", captcha)

user_input = input("Enter CAPTCHA: ")

if user_input == captcha:
    print("Verified: You are human!")
else:
    print("Incorrect CAPTCHA.")