# Task 2

MORSE_CODE_DICT_RUS = {  # Russian letters
    "А": ".-",
    "Б": "-...",
    "В": ".--",
    "Г": "--.",
    "Д": "-..",
    "Е": ".",
    # "Ё": ".",
    "Ж": "...-",
    "З": "--..",
    "И": "..",
    "Й": ".---",
    "К": "-.-",
    "Л": ".-..",
    "М": "--",
    "Н": "-.",
    "О": "---",
    "П": ".--.",
    "Р": ".-.",
    "С": "...",
    "Т": "-",
    "У": "..-",
    "Ф": "..-.",
    "Х": "....",
    "Ц": "-.-.",
    "Ч": "---.",
    "Ш": "----",
    "Щ": "--.-",
    "Ъ": "--.--",
    "Ы": "-.--",
    "Ь": "-..-",
    "Э": "..-..",
    "Ю": "..--",
    "Я": ".-.-",
    # Numbers
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    # Special symbols
    ",": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    "!": "−−..−−",
    " ": "/",
    "": "",
}
MORSE_CODE_DICT_ENG = {  # English letters
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    # Numbers
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    # Special symbols
    ",": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    "!": "−−..−−",
    " ": "/",
    "": "",
}


MORSE_CODE_REVERSED_ENG = {value: key for key, value in MORSE_CODE_DICT_ENG.items()}
MORSE_CODE_REVERSED_RUS = {value: key for key, value in MORSE_CODE_DICT_RUS.items()}

language = input("Enter language(RUS/ENG): ")
language = language.upper()
text = input("Enter message: ")
text = text.upper()
action = input("Enter action(encode/decode): ")
action = action.upper()
translated = ""


def translate(text: str, timed_string="", translated="", action: str = "") -> str:
    if action == "ENCODE":
        print(encode(text=text, translated=translated))

    elif action == "DECODE":
        print(decode(text=text, timed_string=timed_string, translated=translated))
    else:
        print("!_Wrong action_!\n" "Action must be 'ENCODE' or 'DECODE'")


def encode(text: str, translated="") -> str:
    if language == "RUS":
        translated = ""
        for letter in text:
            if letter != " ":
                translated += MORSE_CODE_DICT_RUS[letter] + " "
            else:
                translated += "/ "
        print(translated)
    elif language == "ENG":
        translated = ""
        for letter in text.upper():
            if letter != " ":
                translated += MORSE_CODE_DICT_ENG[letter] + " "
            else:
                translated += "/ "
        print(translated)


def decode(text: str, timed_string="", translated="") -> str:
    if language == "RUS":
        translated = ""
        for symbol in text:
            if symbol != " ":
                timed_string += symbol
            else:
                if symbol == "/":
                    timed_string += " "
                translated += MORSE_CODE_REVERSED_RUS[timed_string]
                timed_string = ""
        if timed_string != "":
            translated += MORSE_CODE_REVERSED_RUS[timed_string]
        print(translated)
    elif language == "ENG":
        translated = ""
        for symbol in text:
            if symbol != " ":
                timed_string += symbol
            else:
                if symbol == "/":
                    timed_string += " "
                translated += MORSE_CODE_REVERSED_ENG[timed_string]
                timed_string = ""
        if timed_string != "":
            translated += MORSE_CODE_REVERSED_ENG[timed_string]
        print(translated)
        return translated


translate(text, timed_string="", translated="", action=action)
