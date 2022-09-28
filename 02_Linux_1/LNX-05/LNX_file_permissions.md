# Subject
File permissions

## Key terminology
Read, write and execute permision for files:

Owner, group and everyone else:  

view file permissions:  

change file permissions, owners and group of the file.  

Any users in /etc/passwd can become the owner.  
Any group in /etc/group can be the group of a file.

## Exercise  
Create a text file.  
Make a long listing to view the file’s permissions.  
Who is the file’s owner and group?  
What kind of permissions does the file have?  
Make the file executable by adding the execute permission (x).  
Remove the read and write permissions (rw) from the file for the group and everyone else, but not for the owner.  
Can you still read it?  
Change the owner of the file to a different user.  
If everything went well, you shouldn’t be able to read the file unless you assume root privileges with ‘sudo’.  
Change the group ownership of the file to a different group.

### Sources  
https://www.cyberciti.biz/faq/create-a-file-in-linux-using-the-bash-shell-terminal/   

https://linuxcommand.org/lc3_man_pages/ls1.html  

https://www.makeuseof.com/linux-file-ownership-groups-guide/  

https://www.guru99.com/file-permissions.html  

https://phoenixnap.com/kb/linux-chown-command-with-examples




### Overcome challenges
I created an empty file, named exercise5.txt, with the > command.  
To make a long listing to view the permissions, I used the ls command with -l for long listing, I added also the -a to see all the files, also the hidden, not needed for this exercise.  
The third column is for owner and the fourth column is the group.  
The file's owner and group is karim, as shown in the results.  
The rw- bits in the after the first bit represent the owner, he has read and write permission not execute.  
The group is represented with the next 3 bits, also rw-, so same permissions as the owner.  
And the last 3 bits are for everyone else, r-- in this example means only read permission.  
I added execute permission to the user and group with chmod ug+x command.  I checked if its correct with the ls -l command.  
I removed the read and write permission for the group and everyone else with the chmod go-rw command, now only the user has rwx permission.  
The file was empty so I added text first with echo >> command and then to show I can read the file, I used cat command.  
I can read the file because I am the owner.  
I changed the owner of the file with the chown command, first I did not succeed  because I did not use sudo. Then with sudo it worked.  
Because lina is the owner now i cant read the file, I showed this with the cat command, but with the sudo command I can.  
To change the group of the file I used the cat /etc/group folder to see witch folder I can use. Then I used the chown :group file command to change the group. It worked, to check this I used the ls -l command.  

### Results 
![image of LNX_05 part 1](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/LNX_05_FP.png) 

![image of LNX_05 part 2](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/LNX_05_FP2.png)  
