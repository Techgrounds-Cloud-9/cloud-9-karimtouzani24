# Subject
Users and groups.

## Key terminology
Root user:  
Is a special type of user, the root user is allowed to do anything.  

sudo:  
This command gives you temporary root permissions, if you are allowed to do this.  

Users, passwords and groups are stored in different files in linux.  

users in the /etc/passwd file  
passwords in the /etc/shwadow file  
groups in the /etc/group file

## Exercise  
1) Create a new user in your VM.  
The new user should be part of an admin group.  
The new user should have a password.  
The new user should be able to use sudo.  

2) Locate the files that store users, passwords, and groups.  
See if you can find your newly created user’s data in there

### Sources
https://www.cyberciti.biz/faq/where-are-the-passwords-of-the-users-located-in-linux/#:~:text=The%20%2Fetc%2Fpasswd%20is%20the,is%20one%20entry%20per%20line.  

https://linuxhint.com/list-all-groups-linux/  

https://linuxize.com/post/how-to-create-users-in-linux-using-the-useradd-command/  

https://phoenixnap.com/kb/how-to-create-sudo-user-on-ubuntu



### Overcome challenges  
It was not difficult to do. Just using the right commands, to be sure I checked to links above to use the right commands.  
To add a user I used the sudo adduser command, then I entered a password.  
I added the user to the admin group and sudo group, to use sudo, with the sudo usermod -a -G group username command.  
To locate if the user is added, I used the cat /etc/passwd with grep command.  
To view if the user is added to the groups, I used the cat /etc/group with grep command.  
To view the password data of the new user, I had to use sudo cat /etc/shadow with grep command.


### Results  
![image of results](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/LNX_04_UG.png)
