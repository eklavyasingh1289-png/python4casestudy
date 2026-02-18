#reverse and uppercase
def revandup(n):
    a = n[::-1]
    for i in a:
        c=i.upper()
        print(c,end='')
revandup(input())