import string

def caeser_cypher(plain_text, key, alphabets):

    def shift_alphabet(alphabet):
        return alphabet[key:] + alphabet[:key]

    shifted_alphabets = tuple(map(shift_alphabet, alphabets))

    join_alphabet = ''.join(alphabets)
    join_shifted_alphabet = ''.join(shifted_alphabets)

    align = str.maketrans(join_alphabet, join_shifted_alphabet)
    return plain_text.translate(align)

plain_input = input("Enter the text to be Encrypted or Decrypted: ")
key_input = input("Enter the key shift. NB include \"-\" for decryption: ")

cryption = caeser_cypher(plain_input, int(key_input), [string.ascii_lowercase, string.ascii_uppercase, string.punctuation])

if(key_input[0] == "-"):
    print(f"Your Decripted text is: {cryption}")
elif(key_input == key_input):
    print(f"Your Encrypted text is: {cryption}")
else:
    print("Invalid input")







