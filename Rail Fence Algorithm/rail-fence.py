# Program in python to implement Rail-Fence Encryption Algorithm with variable depth (given by user)
# Note: The program removes all the whitespaces from the plain_text
# Note: The program adds a whitespace after each rail in the final cipher_text

plain_text = str(input("Enter Plain-Text: "))
depth = int(input("Enter depth: "))

# Removing all the whitespaces from the plain_text
plain_text = plain_text.replace(" ", "")

cipher_rail = []
for i in range(0, depth):
    cipher_rail.append([])

c = 0
up, down = False, True
for char in plain_text:
    cipher_rail[c].append(char)
    if c == depth-1:
        up, down = True, False
    if c == 0:
        up, down = False, True
    if down == True:
        c += 1
    if up == True:
        c -= 1

cipher_text = ""
for rail in cipher_rail:
    for char in rail:
        cipher_text += char
    cipher_text += " "

print("Cipher-Text:", cipher_text)