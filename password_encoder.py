''' Lab 6 Password Encoder
Partners: Andrew Sklyarov (encoder), Sonia Alwani (decoder)'''

def encode_password(decoded_password):
    encoded_password = ''

    for digit in decoded_password:
        digit = str( (int(digit) + 3) % 10 ) # the modulus 10 makes the digits wrap around (ex. 3 being added to 9 returns 2 instead of 12)
        encoded_password += digit

    return encoded_password

def decode_password(encoded_password):
    #TODO: Complete the decoder
    pass

# Main code
decoded_password = ''
encoded_password = ''
print("Welcome to the password encoder program!")

while True:
    print("Please select an option: ")
    print("0. Exit")
    print("1. Encode a password")
    print("2. Decode your encoded password")
    option = int(input("Your selection: "))
    print()

    if option == 0:
        print("Goodbye!")
        break
    elif option == 1:
        decoded_password = input("Please enter the password you want to encode (digits only): ")
        encoded_password = encode_password(decoded_password)
        print("Your encoded password is:", encoded_password)
        print()
    elif option == 2:
        decoded_password = decode_password(encoded_password)
        print("Your decoded password is:", decoded_password)

