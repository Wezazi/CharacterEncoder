text = input("Enter the text you want to encode e.g. Cyberpunk2077: \n")
print("\nIF YOU WANT TO USE utf-16 OR utf-32, MAKE SURE TO EXPLICITLY SPECIFY le OR be (e.g. utf-16be, utf-16le, utf-32be, utf-32le). THIS IS REQUIRED TO AVOID BYTE ORDER MARK\n")
userEncoding = input("\nEnter the character encoding you want to use e.g. utf-8, utf-16be, utf-16le, utf-32be, utf-32le, etc: \n")

encoding = text.encode(userEncoding)

binary = "".join(format(byte, "08b") for byte in encoding) # why did i use 08b instead of b? because b won't return the full byte, it returns the binary representation of the value which excludes all padding. 08b: b=represent in binary, 8=make each byte 8 characters long, 0=pad with zeroes if the byte is shorter than 8 characters.  8 won't do anything without 0 and vice versa, so you need to include both of them.
binarySpace = " ".join(format(byte, "08b") for byte in encoding)


hex = encoding.hex().upper()
hexSpace = encoding.hex(" ").upper()


print(f"\n{userEncoding} encoded {text} in binary:\n{binary}")
print(f"\n{userEncoding} encoded {text} in binary with a space after every byte:\n{binarySpace}")
print(f"\n{userEncoding} encoded {text} in hex:\n{hex}")
print(f"\n{userEncoding} encoded {text} in hex with a space after every two digits:\n{hexSpace}\n") #every two hex digits corresponds to one binary byte