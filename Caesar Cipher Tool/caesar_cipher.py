import string

def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts a text using Caesar Cipher.
    """
    result = []
    # Invert the shift for decryption
    if mode == 'decrypt':
        shift = -shift
        
    for char in text:
        if char.isalpha():
            # Handle uppercase and lowercase letters differently to preserve case
            start = ord('a') if char.islower() else ord('A')
            # Calculate the new character using modulo for wrapping around the alphabet
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result.append(new_char)
        else:
            # Leave punctuation, numbers, and spaces unchanged
            result.append(char)
            
    return ''.join(result)

def brute_force(text):
    """
    Attempts to decrypt the text using all possible 25 shifts.
    """
    print("\n--- Brute Force Decryption Results ---")
    for shift in range(1, 26):
        decrypted_text = caesar_cipher(text, shift, mode='decrypt')
        print(f"Shift {shift:02}: {decrypted_text}")
    print("--------------------------------------")

def main():
    print("=== Caesar Cipher Tool ===")
    
    while True:
        print("\nSelect an option:")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Brute-force attack (decrypt without key)")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            text = input("\nEnter the text to encrypt: ")
            try:
                shift = int(input("Enter the shift key (integer): "))
                encrypted = caesar_cipher(text, shift, 'encrypt')
                print(f"-> Encrypted text: {encrypted}")
            except ValueError:
                print("Error: Shift value must be an integer.")
                
        elif choice == '2':
            text = input("\nEnter the text to decrypt: ")
            try:
                shift = int(input("Enter the shift key (integer): "))
                decrypted = caesar_cipher(text, shift, 'decrypt')
                print(f"-> Decrypted text: {decrypted}")
            except ValueError:
                print("Error: Shift value must be an integer.")
                
        elif choice == '3':
            text = input("\nEnter the text to brute-force: ")
            brute_force(text)
            print("Review the outputs above to find the readable message.")
            
        elif choice == '4':
            print("\nExiting the Caesar Cipher Tool. Goodbye!")
            break
            
        else:
            print("\nInvalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
