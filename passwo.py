import random
import string

letters = string.ascii_letters
numbers = string.digits


all_chars = list(letters + numbers)

random.shuffle(all_chars)


password = ''.join(all_chars[:10])

print("Generated Password:", password)