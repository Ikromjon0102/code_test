# import secrets
#
# def generate_verification_code():
#     return secrets.token_hex(16)


import random

def generate_verification_code():
    return str(random.randint(100000, 999999))
