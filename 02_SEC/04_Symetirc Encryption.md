# Subject
Symetric encryption

## Key terminology
Encryption:  
Encryption is a way of scrambling data so that only authorized parties can understand the information.  
In technical terms, it is the process of converting human-readable plaintext to incomprehensible text, also known as ciphertext.  
In simpler terms, encryption takes readable data and alters it so that it appears random.

Data at rest/ data in motion:  
- Data at rest refers to all data stored on devices that are not transferred from device to device or network to network.  
It includes data stored locally on computer hard drives, archived in databases, file systems, and storage infrastructure.  

- Data in use is data that is currently being updated, processed, erased, accessed, or read by a system and is stored within IT infrastructures such as RAM, databases, or CPUs.  
This type of data is not being passively stored but is very much active.  

- Data in motion, or data in transit, on the other hand, is data moving from one location to another, whether it’s between computers, virtual machines, from an endpoint to cloud storage, or through a private or public network. Once it arrives at its destination, data in motion becomes data at rest.  

Caesar cipher:  
It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter with a fixed number of positions down the alphabet. 

symmetrical encryption:
An encryption methodology that uses a single key to encrypt (encode) and decrypt (decode) data.  
The secret key can be a word, a number, or a string of letters, and it's applied to a message.  
The message is changed following the rules in the key. Sender and receiver know the key, and can thus code and decode any message that would use that specific key.  

Algorithm  
Also known as a cipher, algorithms are the rules or instructions for the encryption process. The key length, functionality, and features of the encryption system in use determine the effectiveness of the encryption.  

Key  
An encryption key is a randomized string of bits used to encrypt and decrypt data. Each key is unique, and longer keys are harder to break. Typical key lengths are 128 and 256 bits for private keys and 2048 for public keys.


## Exercise  
- Find two more historic ciphers besides the Caesar cipher.
- Find two digital ciphers that are being used today.
- Send a symmetrically encrypted message to one of your peers via the public Slack channel.  
They should be able to decrypt the message using a key you share with them.  
Try to think of a way to share this encryption key without revealing it to everyone. 
You are not allowed to use any private messages or other communication channels besides Slack. Analyse the shortcomings of this method.


### Sources
https://www.cloudflare.com/learning/ssl/what-is-encryption/  

https://www.endpointprotector.com/blog/protecting-data-at-rest-vs-data-in-motion/#:~:text=Data%20in%20motion%2C%20or%20data,motion%20becomes%20data%20at%20rest.  

https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/  

https://study.com/academy/lesson/symmetric-encryption-definition-example.html  

https://www.educba.com/types-of-cipher/  

https://www.arcserve.com/blog/5-common-encryption-algorithms-and-unbreakables-future  

https://www.thesslstore.com/blog/symmetric-encryption-101-definition-how-it-works-when-its-used/

### Overcome challenges
- To  find two more historic ciphers besides the Caesar cipher, I searched the internet (https://www.educba.com/types-of-cipher/). 
I found these ciphers:  
1) monoalphabetic cipher,  
each alphabet in plain text can be replaced by any other alphabet except the original alphabet.  

2) homophonic substitution cipher,  
the alphabet is replaced by fixed alphabet or set of alphabet  

3) polygram substitution cipher,  
rather than replacing each alphabet with another, the alphabets’ Block is replaced with another block of alphabets.  

4) polyalphabetic substitution cipher,  
Polyalphabetic Cipher is also known as Vigenere Cipher,  
In Polyalphabetic Substitution, Cipher is a method of encrypting alphabetic texts. It uses multiple substitution alphabets for encryption.  
Vigener square or Vigenere table is used to encrypt the text. The table contains 26 alphabets written in different rows; each alphabet is cyclically shifted to the left according to the previous alphabet, equivalent to the 26 possible Caesar Ciphers. The cipher uses a different alphabet from one of the rows at various points in the encryption process.  

5) playfair cipher,  
6) hill cipher,  
7) caeser cipher,  
Read each alphabet of plain text.
Replace each alphabet with 3 places down.
Repeat the process for all alphabet in plain text.  

- To Find two digital ciphers that are being used today. I searched the internet (https://www.arcserve.com/blog/5-common-encryption-algorithms-and-unbreakables-future).  
1) Triple DES  
Triple DES uses three individual keys with 56 bits each. The total key length adds up to 168 bits, but experts would argue that 112-bits in key strength is more accurate. Despite slowly being phased out, Triple DES has, for the most part, been replaced by the Advanced Encryption Standard (AES).  
2) AES  
Although it is highly efficient in 128-bit form, AES also uses keys of 192 and 256 bits for heavy-duty encryption purposes.  

- Send a symmetrically encrypted message to one of your peers via the public Slack channel.  
They should be able to decrypt the message using a key you share with them.  
Try to think of a way to share this encryption key without revealing it to everyone. 
You are not allowed to use any private messages or other communication channels besides Slack. Analyse the shortcomings of this method.  

The results and answers of this question see exercise 5.