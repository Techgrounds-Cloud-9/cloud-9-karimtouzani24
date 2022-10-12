# Subject
Passwords

## Key terminology
In terms of factors of authentication, passwords fall into the ‘something you know’ category.
To make it harder to guess the password, the folowing strategies can be used:  
	- Not using common passwords
	- Using longer passwords
	- Using special characters like @,*,%, etc.
	- Using a mixture of CAPITAL and small letters
	- Not using easily deducible passwords like birthdates or pet names
	- Using a different password for every login
	- Using a sentence  
  
Password managers are created to make it easier to remember and use your own passwords.  

Passwords are stored securely in linux, in the /etc/shadow file, most stored password are hashed.  

Rainbow table:  
Is a password cracking method that uses a special table (a “rainbow table”) to crack the password hashes in a database. Applications don’t store passwords in plaintext, but instead encrypt passwords using hashes. After the user enters their password to login, it is converted to hashes, and the result is compared with the stored hashes on the server to look for a match. If they match, the user is authenticated and able to login to the application.  

Hashing:  
Hashing is the process of translating a given key into a code. A hash function is used to substitute the information with a newly generated hash code.  
More specifically, hashing is the practice of taking a string or input key, a variable created for storing narrative data, and representing it with a hash value, which is typically determined by an algorithm and constitutes a much shorter string than the original.



## Exercise  
- Find out what hashing is and why it is preferred over symmetric encryption for storing passwords.  

- Find out how a Rainbow Table can be used to crack hashed passwords.  

- Below are two MD5 password hashes. One is a weak password, the other is a string of 16 randomly generated characters. Try to look up both hashes in a Rainbow Table.  

03F6D7D1D9AAE7160C05F71CE485AD31  

03D086C9B98F90D628F2D1BD84CFA6CA  

- Create a new user in Linux with the password 12345. Look up the hash in a Rainbow Table.  

- Despite the bad password, and the fact that Linux uses common hashing algorithms, you won’t get a match in the Rainbow Table. This is because the password is salted.  

- To understand how salting works, find a peer who has the same password in /etc/shadow, and compare hashes.


### Sources
https://www.beyondidentity.com/glossary/rainbow-table-attack  

https://www.techopedia.com/definition/14316/hashing-cybersecurity  

https://www.ssl2buy.com/wiki/difference-between-hashing-and-encryption  

https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html  

https://www.minim.com/blog/rainbow-tables-explained-password-hacking-and-how-to-prevent-against-it  

https://crackstation.net/  

https://linuxize.com/post/how-to-create-users-in-linux-using-the-useradd-command/  

https://www.cyberciti.biz/faq/understanding-etcshadow-file/#:~:text=The%20%2Fetc%2Fshadow%20is%20a,only%20to%20the%20root%20user.  

https://linuxhint.com/shadow-password-file-linux/

### Overcome challenges
The difference between hashing and encryption:  
Encryption is a two-way function that includes encryption and decryption whilst hashing is a one-way function that changes a plain text to a unique digest that is irreversible.  

Hashing and encryption both provide ways to keep sensitive data safe. However, in almost all circumstances, passwords should be hashed, NOT encrypted.

Hashing is a one-way function (i.e., it is impossible to "decrypt" a hash and obtain the original plaintext value). Hashing is appropriate for password validation. Even if an attacker obtains the hashed password, they cannot enter it into an application's password field and log in as the victim.  

Rainbow Table can be used to crack hashed passwords. Rainbow tables are large collections of data that store various common or weak passwords and the hashes that are created from those passwords. During a network attack, the rainbow table compares its hashes to the hashes in the database to crack the code and gain access to information. Hackers can then utilize this information to exploit a vulnerable network.  

Below are two MD5 password hashes. One is a weak password, the other is a string of 16 randomly generated characters. Try to look up both hashes in a Rainbow Table.  

03F6D7D1D9AAE7160C05F71CE485AD31  This hash is cracked using a online free password hash cracker, which uses rainbow tables https://crackstation.net/.  
Because of the weak password.  

03D086C9B98F90D628F2D1BD84CFA6CA  This hash could not be cracked, Its not stored in a rainbow table. Because of the 16 random caracters.  

Create a new user in Linux with the password 12345. Look up the hash in a Rainbow Table. I used the sudo useradd command to add a user.  
To set a password I used the command sudo passwd username.  I used the 12345 password.  

Despite the bad password, and the fact that Linux uses common hashing algorithms, you won’t get a match in the Rainbow Table. This is because the password is salted.  

Between the first- and second-dollar sign is the type of encryption; between the second- and third-dollar sign is the salt, and after the third dollar sign is the hash itself. Below is the encrypted password shown. 

$6$0yMGt.627fBTkpSu$aHJmxDreibVN1tl8slXplz.EYQz19hWw2ctRBYnLttbVWiOa2r1nCFl2gUdavNSO7H1YHr8O4y.S/RI905/5e1:19276:0:99999:7:::  

To understand how salting works, find a peer who has the same password in /etc/shadow, and compare hashes.


### Results  
![hash cracked](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/2893462184fc6f528abc076111696033feb550ab/00_includes/SEC/hash1%20cracked.png)  
Hash cracked, because of the weak password.  
  

![hash not cracked](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/2893462184fc6f528abc076111696033feb550ab/00_includes/SEC/hash2%20not%20cracked.png)  
Hash not cracked, because of the random 16 characters.  
  

![user added with weak password](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/2893462184fc6f528abc076111696033feb550ab/00_includes/SEC/hash%20salt%20ilias.png)  
The user is added with the weak password. The salt and hash is shown.