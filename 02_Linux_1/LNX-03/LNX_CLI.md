# Subject
Working with text, CLI.

## Key terminology
echo command:  
This command is used to display the output to the screen or file.  

redirections:  
The standard input device is the keyboard and the standard output is the screen, stdin and stdout.
The > and >> are used for stdout. With > you can redirect to a file, it will overwrite and >> wil append the file.  
The < is for input redirection. 

pipe command:  
The | lets you use two ore more commands at the same time. The output of the first command will be the input of the next command.  

grep command:  
The grep command will search and show only the information you wanted.  

tee command:  
The tee command shows the result on the screen, stdout, and also saves it into a file.


## Exercise  

1) Use the echo command and output redirection to write a new sentence into your text file using the command line.  
The new sentence should contain the word ‘techgrounds’.  

2) Use a command to write the contents of your text file to the terminal.  
Make use of a command to filter the output so that only the sentence containing ‘techgrounds’ appears.  

3) Read your text file with the command used in the second step, once again filtering for the word ‘techgrounds’.  
This time, redirect the output to a new file called ‘techgrounds.txt’.


### Sources
https://vitux.com/echo-into-file/   

https://www.geeksforgeeks.org/echo-command-in-linux-with-examples/#:~:text=echo%20command%20in%20linux%20is,the%20screen%20or%20a%20file.&text=In%20above%20example%2C%20text%20after,and%20omitted%20trailing%20new%20line.  

https://www.guru99.com/linux-redirection.html  

https://www.guru99.com/linux-pipe-grep.html

https://www.geeksforgeeks.org/tee-command-linux-example/


### Overcome challenges
1) I used the echo command and the >> to add text to an existing file.  
2) I used the cat command to write the file to the terminal.  
I added a pipe with a grep command to only show the line with the word techground.  
3) I used the cat command to view the file, I added a pipe and grep command to choose for specific word. Then I added a pipe and tee command to save the result into a new file.

### Results  
![image of results](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/LNX_03_CLI.png) 
