# Task 2
MORSE_CODE_DICT = \
    {  # Russian letters
        'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 'Ё': '.',
        'Ж': '...-', 'З': '--..', 'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--',
        'Н': '-.', 'О': '---', 'П': '.--.', 'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-',
        'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.', 'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--',
        'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..', 'Ю': '..--', 'Я': '.-.-',
        # English letters
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
        'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        # Numbers
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        # Special symbols
        ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': ' '}

user_text_input = input("Enter message: ")
user_text_input_splitted = user_text_input.split()
user_text_encrypted = []
user_text_decrypted = []
if user_text_input.isalpha():
    # Encryptor
    for letter in user_text_input.upper():
        user_text_encrypted.append(MORSE_CODE_DICT[letter])
    print("Encrypted message: ", " ".join(user_text_encrypted))
else:
    # Decryptor
    for letter in user_text_input:
        result_letter = list(zip())
        user_text_decrypted.append(result_letter)
    print("Decrypted message: ", user_text_decrypted)
