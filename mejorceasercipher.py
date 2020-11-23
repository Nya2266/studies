def mejor_ceasar():
    text = input("Text to cipher")
    step = int(input("GIVE ME THAT STEPA TO CIPHER"))
    cipher = ""
    for i in text:
        if not i.isalpha():
            continue
        code = ord(i) + step
        cipher += chr(code)
        print(i)
        print(code)
    print("original text:", text)
    print("Ciphered text:", cipher)

mejor_ceasar()

print(chr(110))
