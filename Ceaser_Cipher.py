def caesar_cipher(text, shift)
    encrypted_text = 
    for char in text
        if char.isalpha()  # Checking if the character is an alphabet
            if char.isupper()  # For uppercase letters
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            else  # For lowercase letters
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else  # Non-alphabet characters remain unchanged
            encrypted_text += char
    return encrypted_text
    
def caesar_decrypt(text, shift)
    decrypted_text = ''
    for char in text
        if char.isalpha()
            shifted = ord(char) - shift
            if char.islower()
                if shifted  ord('a')
                    shifted += 26
            elif char.isupper()
                if shifted  ord('A')
                    shifted += 26
            decrypted_text += chr(shifted)
        else
            decrypted_text += char
    return decrypted_text

# main
plaintext = ABDULGHANI
shift_amount = 3
encrypted_text = caesar_cipher(plaintext, shift_amount)
print(Original text, plaintext)
print(Encrypted text, encrypted_text)

decrypted_text = caesar_decrypt(encrypted_text, shift_amount)
print(Decrypted, decrypted_text)
