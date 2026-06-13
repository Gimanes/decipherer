import main

import numpy as np

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caesar_cipher(text: str, shift):
    # shift the alphabet by the specified amount
    if shift == 10:
        print("10 shift is broken so expect letter 'e' to be replaced with 'o'")
    shift_alphabet = alphabet[shift:] + alphabet[:shift] # alphabet shift here

    # this part will encode the text using the shifted alphabet

    print(shift_alphabet)

    for char in text:
        result = text.replace(char, alphabet[shift_alphabet.index(char)]) if char in shift_alphabet else char

    print(result)
    if main.log_on:
        with open("log.txt", "a") as f:
            f.write(f"Action: Caesar - Text: {text}")
            f.write(f"Action: Caesar - Shift: {shift}")
            f.write(f"Action: Caesar - Result: {result}")
    else:
        pass
