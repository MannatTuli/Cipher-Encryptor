import base64
import string

cryptName = input('Enter the cipher you want to use (base64, ciphernew): ')
 
if cryptName == 'base64': 
	sample_string = input('Enter the string in base64 to encrypt: ')
	sample_string_bytes = sample_string.encode("ascii")
  
	base64_bytes = base64.b64encode(sample_string_bytes)
	base64_string = base64_bytes.decode("ascii")
  
	print(f"Encoded string: {base64_string}")

elif cryptName == 'ciphernew':
    key = 13
    key = int(key)
    message = input("Enter the text you want to encrypt (cipherNew is a simple cipher made by me which changes some letters to characters as well): ")
    
    for letter in message:
            print(chr(ord(letter) + key))


else:
	print('Please enter a cipher from the given ones...')