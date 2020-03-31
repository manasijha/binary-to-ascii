#conversion of binary to ascii
word= input("Enter the binary text you want to convert: ")
bword= [word[i:i+8] for i in range(0, len(word), 8)]
output= ""
for bword in bword:
    a = int(bword, 2)
    ch = chr(a)
    output += ch
print(output)
