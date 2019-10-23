pal = input("input a string: ")
ispal = False

pal = pal.lower()
pal = pal.replace("?", "")
pal = pal.replace(" ", "")
pal = pal.replace(",", "")
pal = pal.replace("'", "")
pal = pal.replace(".", "")
pal = pal.replace("!", "")

for x in range(0, len(pal)-1):
    if(x==(len(pal)-1)-x):
        break
    if((pal[x]==pal[(len(pal)-1)-x])):
        ispal = True
    else:
        ispal = False
        break

if(ispal):
    print("its a palindrome!")
else:
    print("its not a palindrome. :(")
