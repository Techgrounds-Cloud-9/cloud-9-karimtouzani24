# Subject
Bash scripting

## Key terminology
Bash shell:  
The CLI in linux.  

Script:  
A series of commands written in a text file.  

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

2)  




### Overcome challenges
1)  
I created a directory called scripts with the mkdir command. I added this directory to the PATH variable, by editing the bashrc file with vim, see result.  
To check if directory is added I used echo $PATH.  
Next I made a .sh file called firstscript with vi.  

With echo 'text' >> filename, the script appends text to the file. The script has no execute permission so I added this with the chmod u+x filename. To check if it works i run ./scriptname. I had to rewrite the code to make the path specific to the file. Because another file was created. Now with the path rewritten, it succeeded to add the text to the file.  

For the next exercise I created a new script, with commands to install, enable and activate apache2, the httpd and to show the status. Made the script executable to run. See results which commands I used.  I added -y to automatic answer with yes.  

2)  







### Results