#program to find mathematical numbers for strings
a = input()
for i in a:
    j = ord(i)
    if j >= 95:
        print(j - 96,end='')
    elif j >= 65:
	    print(j - 64,end='')