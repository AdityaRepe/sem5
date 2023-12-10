import math

p=input("Enter the Plain Text:")
private_key=list(map(int,input("Enter the Private_key ").split()))

m=sum(private_key)+5
n=2

def gcd(n,m):
    while math.gcd(n,m)!=1:
        n += 1
    return n
n=gcd(2,m)

def public_key(private_key,n,m):
    return[(X * n) % m for X in private_key]

pub_key=public_key(private_key,n,m)

def encryption(pub_key):
    cipher1=0
    cipher2=0
    for i in range(0,4):
        cipher1+=int((ord(p[i])-ord('0'))*pub_key[i])
    for i in range(4,8):
        cipher2+=int((ord(p[i])-ord('0')) * pub_key[i-4])
    return cipher1,cipher2
c1,c2=encryption(pub_key)

print("Plain Text:",p)
print("Private Key:",private_key)
print("Public Key:",pub_key)
print("Cipher1:",c1)
print("Cipher2:",c2)