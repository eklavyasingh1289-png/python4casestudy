#Check the strength of a password
def pa(password):
    if len(password)<6:
        print("Password too short")
    if not any(i.isupper() for i in password):
        print("No uppercase character")
    if not any(i.islower() for i in password):
        print("No lowercase character")
    if not any(i.isdigit() for i in password):
        print("No number")
    print("Strong")
pa(input())