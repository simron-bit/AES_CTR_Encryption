#Encryption under AES-GCM
from Crypto.Cipher import AES

#1. Plaintext, nonce, key and counter defined
plaintext='HELLO'
nonce = b'\x15\xa9\xf3\x2d\x6b\x00\xcc\x7f\xaa\x98\x71\x2e' #Nonce of 12 bytes
key = b'ThisIsASecretKey'
counter =[
    b'\x00\x00\x00\x01',#Counter of 4 bytes
    b'\x00\x00\x00\x02',
    b'\x00\x00\x00\x03',
    b'\x00\x00\x00\x04',
    b'\x00\x00\x00\x05'
]

a=[]
x=len(plaintext)
i=0

#1. The ASCII value of each letter in the plaintext is generated and stored in a string
for char in plaintext:
    a.append(ord(char))
    i=i+1

#2. Generation of keystream
b=[]
keystream=[]
j=0
for j in range(x):
    block=nonce+counter[j] #A block of 16 bytes(12 bytes nonce and 4 bytes counter)
    cipher=AES.new(key,AES.MODE_ECB) #A cipher object is created 
    keystream.append(cipher.encrypt(block)) #The cipher object helps encrypt the 16 bytes block one by one to form the keystream

#3. Generation of ciphertext
ciphertext=[]
for plain_t, keystream_block in zip(a, keystream):
    xor_ed = bytes([plain_t ^ keystream_block[0]])#Corresponding blocks from array 'a' and 'keystream' is paired and then XOR'ed to get the ciphertext
    ciphertext.append(xor_ed)

print(ciphertext)


