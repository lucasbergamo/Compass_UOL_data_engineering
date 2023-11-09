import hashlib

def gen_sha1_hex(input_string):
    sha1_hash = hashlib.sha1(input_string.encode())
    return sha1_hash.hexdigest()

def main():
    while True:
        print_string = input("Digite uma string: ")
        sha1_hash_hex = gen_sha1_hex(print_string)
        print(f"O hash SHA-1 da string: '{print_string}' é:, {sha1_hash_hex}")

if __name__ == "__main__":
    main()