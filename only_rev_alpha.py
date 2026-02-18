#Reverse only the alphabet part of a string containing alphabets and numbers.
a = input()
a = list(a)
n = len(a)
b = []
for i in a:
    if(i.isalpha()):
        b.append(i)
c = b[::-1]
i=0
j=0
while(i<n):
    if(a[i].isalpha()):
        a[i]=c[j]
        j+=1
    i+=1

for i in a:
    print(i,end='')