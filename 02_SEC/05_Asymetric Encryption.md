# Subject


## Key terminology


## Exercise
1) Generate a key pair.  

2) Send an asymmetrically encrypted message to one of your peers via the public Slack channel. They should be able to decrypt the message using a key you share with them. The recipient should be able to read the message, but it should remain a secret to everyone else.
You are not allowed to use any private messages or other communication channels besides Slack. Analyse the difference between this method and symmetric encryption.

### Sources
https://generate-random.org/encryption-key-generator?count=1&bytes=32&cipher=des-cbc&string=&password=  

https://www.tools4noobs.com/online_tools/encrypt/  

https://www.devglan.com/online-tools/rsa-encryption-decryption

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