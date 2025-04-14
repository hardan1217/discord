import random

def get_password(longitud):
    
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    password = ""
    for i in range(longitud):
        password += random.choice(characters)

    return password