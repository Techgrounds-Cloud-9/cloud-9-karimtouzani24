# Subject
Make an SSH-connection to your machine. SSH requires the key file to have specific permissions, so you might need to change those.  

When the connection is successful, type whoami in the terminal. This command should show your username.  

## Key terminology
pem file:  
ppk file:  
SSH:  
Putty:

## Exercise  
create a remote connection to your machine.

### Sources
https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=powershell  
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html  

### Overcome challenges  
I am using powershell, I need to run as administrator. Then i have to check if Openssh is installed on my windows laptop.  
The server is not installed so i had to install it.  
I configured a firewall rule to open the ssh-port.
With putty i wanted to connect to the linux container. But not succeeded, because of permission denied (publickey).  
With Puttygen i had to convert the pem file to ppk file (key). Now i succeeded to connect with Putty.


### Results  
![screenshot of exercise succes](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/linux1_exercise1.png)