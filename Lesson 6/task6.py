def vigenere_cipher(text, key, mode='encrypt'):
    result = []
    key = key.lower()
    key_length = len(key)
    key_as_int = [ord(i) - ord('a') for i in key]
    text_as_int = [ord(i) - ord('a') for i in text.lower() if i.isalpha()]
    
    for i, char in enumerate(text_as_int):
        if mode == 'encrypt':
            value = (char + key_as_int[i % key_length]) % 26
        elif mode == 'decrypt':
            value = (char - key_as_int[i % key_length]) % 26
        else:
            raise ValueError("Mode must be 'encrypt' or 'decrypt'")
        result.append(chr(value + ord('a')))
    
    return ''.join(result)

mode = input("Введите режим (encrypt/decrypt): ").strip().lower()
text = input("Введите текст: ").strip()
key = input("Введите ключ: ").strip()

try:
    output = vigenere_cipher(text, key, mode)
    print(f"Результат: {output}")
except ValueError as e:
    print(f"Ошибка: {e}")