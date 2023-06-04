import hashlib
starting_str = 'bgvyzdsv'
num = 0

while True:
    num += 1
    hashed_object = hashlib.md5(f'{starting_str}{num}'.encode())
    hash_to_str = hashed_object.hexdigest()
    if hash_to_str.startswith('000000'):
        print(num)
        break

