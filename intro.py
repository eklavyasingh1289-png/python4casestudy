#kind of a revision since I haven't coded python in a while 
print("Hello World")
arr = []
ans = 'y'
while(ans=='y'):
    k = input("Enter an element")
    arr.append(k)
    ans = input("Enter more records? y/n")
for i in arr:
    print(i)
