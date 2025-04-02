#prime num
p=int(input("Enter the prime number:"))


#primitive root
g=int(input("Enter the primitive root:"))


#select private key for alice :xa
Xa=int(input("Enter the private key for Xa:"))
if Xa<p:
    #calculate the public key for Xa
    Ya=(pow(g,Xa,p))
    print(f"The public key for Xa is:{Ya}")
else:
    print("Invalid private key entered!!!.Private key should be less than prime number.")
    exit()



#select private key for bob :Xb
Xb=int(input("Enter the private key for Xb:"))
if Xb<p:
        #calculate the public key for Xb
    Yb=(pow(g,Xb,p))
    print(f"The public key for Xb is:{Yb}")
else:
    print("Invalid private key entered!!!.Private key should be less than prime number.")
    exit()

#calculate the shared secret key for alice Ka:
Ka=(pow(Yb,Xa,p))
print(f"The shared secret key for Xa is:{Ka}")

#calculate the shared secret key for bob Kb:
Kb=(pow(Ya,Xb,p))
print(f"The shared secret key for Xb is:{Kb}")
