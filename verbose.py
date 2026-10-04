import regex

#for debugging: text = "Iphone192184 👨🏿‍👩🏿‍👧🏿‍👦🏿"

text = input("Enter the text you want to encode e.g. Cyberpunk2077: \n")

for grapheme in regex.findall(r"\X", text):
    print(f"Grapheme: {grapheme}")

    for codepoint in grapheme:
        print(f"    Code point: {codepoint} U+{ord(codepoint):04X}")
    print()


print("\nIF YOU WANT TO USE utf-16 OR utf-32, MAKE SURE TO EXPLICITLY SPECIFY le OR be (e.g. utf-16be, utf-16le, utf-32be, utf-32le). THIS IS REQUIRED TO AVOID BYTE ORDER MARK\n")
userEncoding = input("\nEnter the character encoding you want to use e.g. utf-8, utf-16be, utf-16le, utf-32be, utf-32le, etc: \n")

encoding = text.encode(userEncoding)

binary = "".join(format(byte, "08b") for byte in encoding)
binarySpace = " ".join(format(byte, "08b") for byte in encoding)


hex = encoding.hex().upper()
hexSpace = encoding.hex(" ").upper()


print(f"\n{userEncoding} encoded {text} in binary:\n{binary}")
print(f"\n{userEncoding} encoded {text} in binary with a space after every byte:\n{binarySpace}")
print(f"\n{userEncoding} encoded {text} in hex:\n{hex}")
print(f"\n{userEncoding} encoded {text} in hex with a space after every two digits:\n{hexSpace}\n")