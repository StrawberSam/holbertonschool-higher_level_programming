#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    caractere = ""

    for char in text:
        caractere += char

        if char in '.?:':
            print(caractere.strip(), end="\n\n")
            print()
            caractere = ""

    if caractere:
        print(caractere.strip())
