Replace `import random` with `import secrets` and subsequently use `secrets.choice` instead of `random.choice`.
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# User input
length = int(input("Enter password length: "))

password = generate_password(length)

print("Generated Password:", password)
