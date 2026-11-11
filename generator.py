import random

# مولد كلمات مرور مصغر
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = "".join(random.choice(chars) for _ in range(8))

print("--- Password Generator ---")
print(f"Generated Password: {password}")