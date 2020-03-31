# binary-to-ascii
It will convert Binary text to ascii text.


The Code ::::::::::::


#conversion of binary to ascii
word= input("Enter the binary text you want to convert: ")
bword= [word[i:i+8] for i in range(0, len(word), 8)]
output= ""
for bword in bword:
    a = int(bword, 2)
    ch = chr(a)
    output += ch
print(output)


Note: In the code, if your input is in format  01101000 01100101 01101100 ........ (space after every 8th digit)
then just replace [word[i:i+8] for i in range(0, len(word), 8)] with word.split()
