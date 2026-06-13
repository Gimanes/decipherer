import imageio
import numpy as np
import imageio.v2 as imageio

translations = {
    "en": {
        "a": "41", "b": "42", "c": "43", "d": "121", "e": "15",
        "f": "123", "g": "131", "h": "132", "i": "16", "j": "24",
        "k": "212", "l": "213", "m": "51", "n": "52", "o": "53",
        "p": "231", "q": "232", "r": "26", "s": "34", "t": "312",
        "u": "313", "v": "321", "w": "35", "x": "323", "y": "61",
        "z": "62", " ": "0", "2": "182", "5": "282", "1": "181",
        "3": "183", "4": "281", "6": "283", "7": "381", 
        "8": "382", "9": "383", "0": "48", ".": "47", "?": "57",
        "!": "68", ",": "127", "-": "217", ";": "237", ":": "317"
    }
}

matrix_key = {
    '1': [3],
    '2': [1],
    '3': [2],
    '4': [2, 3],
    '5': [2, 1],
    '6': [2, 1, 3],
    '7': [0],
    '8': [0, 3],
    '9': [0, 1],
    '0': [0, 2]
}

text = ""

def encode(text, language):
    translation = ""
    for char in text:
        if char in translations[language]:
            translation += translations[language][char]
        else:
            translation += char
    with open("log.txt", "a") as f:
        f.write(f"Action: Encode - Text: {text}\n")
        f.write(f"Action: Encode - Result: {translation}\n")
    return translation
translated_text = encode(text, "en")
print(translated_text)


def decode(text, language):
    reverse_translation = {v: k for k, v in translations[language].items()}
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
    with open("log.txt", "a") as f:
        f.write(f"Action: Decode - Text: {text}\n")
        f.write(f"Action: Decode - Result: {decoded_text}\n")
    return decoded_text

def imageEncode(text, language, sstv_on):
    translation = encode(text, language)
    
    img = np.zeros((64, 64), dtype=np.uint8)
    
    for i, char in enumerate(translation):
        if char in matrix_key:
            col = i % 64
            block_row = (i // 64) * 4 

            if block_row + 3 < 64: 
                for r in matrix_key[char]:
                    img[block_row + r][col] = 255
            else:
                print("bih text fuck of")
                break

    rotated_img = np.rot90(img, -1)
    if sstv_on:
        target_width = 320
        target_height = 240
        height, width = img.shape
        upscaled_to_sstv_img = np.zeros((target_height, target_width), dtype=np.uint8)
        y_ratio = height / target_height
        x_ratio = width / target_width
        for y in range(target_height):
            for x in range(target_width):
                src_y = int(y * y_ratio)
                src_x = int(x * x_ratio)
                upscaled_to_sstv_img[y, x] = img[src_y, src_x]
        imageio.imwrite("encoded_image.png", upscaled_to_sstv_img)
    else:
        imageio.imwrite("encoded_image.png", rotated_img)

    with open("log.txt", "a") as f:
        f.write(f"Action: Image encode - Text: {text}\n")
        f.write(f"Action: Image encode - Result: {translated_text}\n")

choice = input("Do you want to encode, decode, or image encode? (e/d/i): ")
if choice == "e":
    text = input("Enter text to encode: ")
    print(encode(text, "en"))
elif choice == "d":
    text = input("Enter text to decode: ")
    print(decode(text, "en"))
elif choice == "i":
    text = input("Enter text to image encode: ")
    sstv = input("Do you want to use special mode for SSTV? (y/n): ")
    if sstv.lower() == "y":
        imageEncode(text, "en", True)
    else:
        imageEncode(text, "en", False)
    print("Done")
else: 
    print("Invalid choice. Please enter 'e' for encode or 'd' for decode.")
