# Subject


## Key terminology  
The two main kinds of encryption are symmetric encryption and asymmetric encryption. Asymmetric encryption is also known as public key encryption.
In symmetric encryption, there is only one key, and all communicating parties use the same (secret) key for both encryption and decryption.  
In asymmetric, or public key, encryption, there are two keys: one key is used for encryption, and a different key is used for decryption.  
The decryption key is kept private (hence the "private key" name), while the encryption key is shared publicly,  
for anyone to use (hence the "public key" name). Asymmetric encryption is a foundational technology for TLS (often called SSL).  

What is an encryption algorithm?
An encryption algorithm is the method used to transform data into ciphertext. An algorithm will use the encryption key in order to alter the data in a predictable way, so that even though the encrypted data will appear random, it can be turned back into plaintext by using the decryption key.  

Commonly used symmetric encryption algorithms include:  
AES
3-DES
SNOW  

Commonly used asymmetric encryption algorithms include:
RSA
Elliptic curve cryptography

## Exercise
1) Generate a key pair.  

2) Send an asymmetrically encrypted message to one of your peers via the public Slack channel. They should be able to decrypt the message using a key you share with them. The recipient should be able to read the message, but it should remain a secret to everyone else.
You are not allowed to use any private messages or other communication channels besides Slack. Analyse the difference between this method and symmetric encryption.

### Sources
https://generate-random.org/encryption-key-generator?count=1&bytes=32&cipher=des-cbc&string=&password=  

https://www.tools4noobs.com/online_tools/encrypt/  

https://www.devglan.com/online-tools/rsa-encryption-decryption  

https://www.cloudflare.com/learning/ssl/what-is-encryption/  

https://cryptotools.net/dhe

### Overcome challenges  
I used the online key generator for a symmetric encryption of exercise 4 (https://generate-random.org/encryption-key-generator?count=1&bytes=32&cipher=des-cbc&string=&password=)  

To generate a key pair for asymmetric encryption, I used a online tool to generate RSA key pair. (https://www.devglan.com/online-tools/rsa-encryption-decryption).  

Also to send a message (the symmetric key of exercise 4), we used the same website. I used the other persons public key, which I recieved via slack. This is the asymmetric part of exercise 5. 
I used the other persons public key to encrypt the message (the symmetric key of exercise 4), I have now the encrypted text as output.  

I can now send this encrypted text (the symmetric key of exercise 4) with slack, the other person can decrypt the text with the same website  
using his/her private key to decrypt the text (the symmetric key of exercise 4).  

Now both persons have the symmetric key. The key is exchanged securely with the asymmetric key exchange.  

You can now send messages with symmetric encryption because both persons have the key. To encrypt and decrypt we use the same key.  
We use the online tool (https://www.tools4noobs.com/online_tools/encrypt/). Now we have done also the symmetric part of exercise 4.  



### Results