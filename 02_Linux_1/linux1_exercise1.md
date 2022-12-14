# Subject  
Create a remote connection to your machine.  

## Key terminology
PEM file:  
A container file format often used to store cryptographic keys.  

PPK file:    
PPK files are PuTTY Private Key Files developed by Putty and they serve as storage for the private keys the program generated.  
These files are used to enable communication securely with another party having the corresponding public key.  

SSH:  
A network communication protocol that enables two computers to communicate.  

Putty:  
A free and open-source terminal emulator, serial console and network file transfer application.

## Exercise  
Make an SSH-connection to your machine. SSH requires the key file to have specific permissions, so you might need to change those.  
When the connection is successful, type whoami in the terminal. This command should show your username.

### Sources
https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=powershell  

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html  

### Overcome challenges  
I am using powershell, I need to run this as an administrator. I have to check if Openssh is installed on my windows laptop.  
The server is not installed so I installed it.  
I configured a firewall rule to open the ssh-port.
With putty I wanted to connect to the linux container. But did not succeed, because of permission denied (publickey).  
With Puttygen I had to convert the PEM file to PPK file (key). Now I succeeded to connect with Putty.


### Results  
![screenshot of exercise succes](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/linux1_exercise1.png)