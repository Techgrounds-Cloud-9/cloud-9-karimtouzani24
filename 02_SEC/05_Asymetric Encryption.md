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

Now both persons have the symmetric key. The key is exchanged securely with the asymmetric key exchange (RSA).  

You can now send messages with symmetric encryption because both persons have the key. To encrypt and decrypt we use the same key.  
We use the online tool (https://www.tools4noobs.com/online_tools/encrypt/). Now we have done also the symmetric part of exercise 4.  

We used RSA for the asymmetric key exchange, but Diffie-Hellman method is another way to share a secret key. I used the online tool,  
https://cryptotools.net/dhe, to generate the secret key, see results.



### Results  
![generate random symmetric key](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/SEC/symmetric%20key%20gen.png)  
Generate a random symmetric key.  


![generate RSA key pair, public and private key, for asymmetric key exchange](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/SEC/RSA%20key%20pair.png)  
Generate RSA key pair, public and private key, for asymmetric key exchange  


![encrypt the key using the other persons public key](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/SEC/encrypt%20to%20manish%20asym..png)  
Encrypt the key using the other persons public key.  

![other person can decrypt the key with his/her private key](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/SEC/decrypt%20manisha%20asym.png)  
Other person can decrypt the key with his/her private key.  


![Now the symmetric key is shared securely with the asymmetric key exchange, RSA. We can encrypt text with the symmetric key](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/SEC/encrypt%20tool.png)  
Now the symmetric key is shared securely with the asymmetric key exchange, RSA. We can encrypt text with the symmetric key.  


![The other person can decrypt the text with the shared symmetric key](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/SEC/decrypt%20tool.png)  
The other person can decrypt the text with the shared symmetric key.  


![Instead of RSA you can also use the Diffie-Hellman key exchange, by using the other persons public key to generate a shared key](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/SEC/diffie%20hellman1.png)  
Instead of RSA you can also use the Diffie-Hellman key exchange, by using the other persons public key to generate a shared key.  

![After sharing our public keys, the online tool generates the shared key to both of us, this image shows that the keys we have are the same.](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/SEC/diffie%20hellman2.png)  
After sharing our public keys, the online tool generates the shared key to both of us, this image shows that the keys we have are the same.
