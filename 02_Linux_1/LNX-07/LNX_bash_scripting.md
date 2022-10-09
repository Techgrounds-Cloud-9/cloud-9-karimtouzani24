# Subject
Bash scripting

## Key terminology
Bash shell:  
The CLI in linux.  

Script:  
A series of commands written in a text file. You can execute multiple commands in a row by just executing the script.  
In order to be able to execute the script, a user needs to have permissions to execute (x) the file.  

Linux will only be able to find the script if you specify the path name, or if you add the path to the directory in which the script lives to the PATH variable.

Although there are no file extensions in Linux, it’s easier for humans to understand if you end your script names with ‘.sh’.  

variables:  

Conditions:  

Loops:  

.sh:  
End your script with .sh.  

PATH variable:  

=:  

reading the value of a  variable:  

if:  

elif:  

else:





## Exercise  
1) Create a directory called ‘scripts’. Place all the scripts you make in this directory.  

Add the scripts directory to the PATH variable.  

Create a script that appends a line of text to a text file whenever it is executed.  

Create a script that installs the httpd package, activates httpd, and enables httpd. 
Finally, your script should print the status of httpd in the terminal.  

2) Create a script that generates a random number between 1 and 10, stores it in a variable, and then appends the number to a text file.  

3) Create a script that generates a random number between 1 and 10, stores it in a variable, and then appends the number to a text file only if the number is bigger than 5. If the number is 5 or smaller, it should append a line of text to that same text file instead.

### Sources  

1)
https://linuxconfig.org/how-to-add-directory-path-to-path-variable  

https://linuxize.com/post/how-to-add-directory-to-path-in-linux/  

https://www.guru99.com/introduction-to-shell-scripting.html  

https://www.cyberciti.biz/faq/linux-append-text-to-end-of-file/  

https://www.andrewcbancroft.com/blog/musings/make-bash-script-executable/

https://www.baeldung.com/linux/scripting-yes-during-install  

https://www.cloudsigma.com/installing-the-apache-server-on-ubuntu-18-04-a-how-to-guide/  
https://linuxize.com/post/start-stop-restart-apache/  

https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/run-Unix-shell-script-Linux-Ubuntu-command-chmod-777-permission-steps#:~:text=Step%2Dby%2Dstep%20shell%20script%20execution&text=Create%20a%20file%20in%20your,name%20in%20the%20Terminal%20window

2)  




### Overcome challenges
1)  
I created a directory called scripts1 with the mkdir command. I added this directory to the PATH variable, by using the command  
export PATH="/script1:$PATH", To check if directory is added I used the command echo $PATH.  
To permanently add to $PATH I added the export command to the end of the .bashrc file with the command vim ~/.bashrc.  
To safe this changes use the following command source ~/.bashrc

Next I made a .sh file called firstscript with vi.  
With echo 'text' >> filename, the script appends text to the file. The script has no execute permission so I added this with the chmod u+x filename. To check if it works i run ./scriptname.   

For the next exercise I created a new script, with commands to install, enable and activate apache2, the httpd and to show the status. Made the script executable to run. See results which commands I used.  I added -y to automatic answer with yes.  








### Results