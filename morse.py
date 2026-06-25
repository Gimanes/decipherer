import main

translations = {
    "a": ".-/",
    "b": "-.../",
    "c": "-.-./",
    "d": "-../",
    "e": "./",
    "f": "..-./",
    "g": "--./",
    "h": "..../",
    "i": "../",
    "j": ".---/",
    "k": "-.-/",
    "l": ".-../",
    "m": "--/",
    "n": "-./",
    "o": "---/",
    "p": ".--./",
    "q": "--.-/",
    "r": ".-./",
    "s": ".../",
    "t": "-/",
    "u": "..-/",
    "v": "...-/",
    "w": ".--/",
    "x": "-..-/",
    "y": "-.--/",
    "z": "--../",
    "1": ".----/",
    "2": "..---/",
    "3": "...--/",
    "4": "....-/",
    "5": "...../",
    "6": "-..../",
    "7": "--.../",
    "8": "---../",
    "9": "----./",
    "0": "-----/",
    ".": ".-.-.-/",
    ",": "--..--/",
    "?": "..--../",
    "/": "-..-./",
    "@": ".--.-./",
    " ": " "
}

def encode(text):
    translation = ""
    for char in text:
        if char in translations:
            translation += translations[char]
        else:
            translation += char
    if main.log_on:
        with open("log.txt", "a") as f:
            f.write(f"Action: Morse Encode - Text: {text}\n")
            f.write(f"Action: Morse Encode - Result: {translation}\n")
    else:
        pass
    print(translation)

def decode(text):
    reverse_translation = {v: k for k, v in translations.items()}
    decoded_text = ""
    i = 0
    while i < len(text):
        found = False
        for code in reverse_translation:
            if text[i:i+len(code)] == code:
                decoded_text += reverse_translation[code]
                i += len(code)
                found = True
                break
        if not found:
            decoded_text += text[i]
            i += 1
    if main.log_on:
        with open("log.txt", "a") as f:
            f.write(f"Action: Morse Decode - Text: {text}\n")
            f.write(f"Action: Morse Decode - Result: {decoded_text}\n")
    else:
        pass
    print(decoded_text)