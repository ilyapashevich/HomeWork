"""
Я пытался еще таким способом, но у меня не получилось справится с расшифровкой!
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Выберите действие:")
    print("1. Зашифровать текст")
    print("2. Расшифровать текст")
    choice = input("Введите 1 или 2: ")

    if choice == '1':
        text = input("Введите текст для шифрования: ")
        shift = 3
        encrypted_text = encrypt(text, shift)
        print(f"Зашифрованный текст: {encrypted_text}")
    elif choice == '2':
        text = input("Введите текст для дешифрования: ")
    else:   
         decrypted_text = decrypt(encrypted_text, shift)
         print(f"Расшифрованный текст: {decrypted_text}")

if __name__ == "__main__":
    main()"""

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift


    for char in text:
        if char.isalpha():  # Проверяем, является ли символ буквой
            alphabet = 'abcdefghijklmnopqrstuvwxyz' if char.islower() else 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            new_index = (alphabet.index(char) + shift) % len(alphabet)
            result += alphabet[new_index]
        else:
            result += char  # Не изменяем символы, которые не являются буквами

    return result

text = input("Введите текст: ")
shift = 3
mode = input("Выберите режим (encrypt/decrypt): ").strip().lower()

output = caesar_cipher(text, shift, mode)
print(f"Результат: {output}")