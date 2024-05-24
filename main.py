import random
import string

print("Password Generator:")
i=1
ch=string.ascii_letters+string.digits+string.punctuation
while i:
    l=float(input("Enter length of password:"))
    k=int(l)
    if l<=0:
        print("Invalid length")
    elif l!=k:
        print("Please enter a valid integer")
    else:
        pw=''.join(random.choice(ch) for _ in range(k))
        print("Generated Password:",pw)
    chk=input("DO you want to generate another password(Yes/No):")
    if chk.lower()!='yes':
        i=0


