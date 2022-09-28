# Subject
Processes  

## Key terminology
Daemons:  
A process wich runs in the background and is not interactive.  

Service:  
A process that responds to requests from programs, can be interactive.  

Program:  
A process is run and used by users.  

ssh:  
Secure shell  

telnet:  

process:  
  
PID number:

## Exercise  
Start the telnet daemon.  
Find out the PID of the telnet daemon.  
Find out how much memory telnetd is using.
Stop or kill the telnetd process.

### Sources
https://www.javatpoint.com/linux-telnet-command  

https://medium.com/@codingmaths/service-masking-in-linux-f7265d9b2181  

https://shapeshed.com/unix-kill/  


### Overcome challenges  
First I checked with the hostnamectl command which linux version I have. Because there may be differences how to solve this issue depending on the version.  

After updating linux with sudo apt update I installed telnetd with the sudo apt install telnetd command.  

To check if the service is running I used the systemctl status inetd command. Unfortunately the service is inactive because the service is masked. To solve this I unmasked the service with the commands systemctl unmask inetd.service.  

After allowing port 23 in the firewall en reloading the firewall I started the telnet deamon by connecting to the localhost with the command telnet localhost.  

To find the PID of the telnet daemon I used the ps aux command. telnetd is shown with the PID of 12618, telnet is using 0.0% memory.  

To stop the telnetd process I used the sudo kill 12618 command. 

### Results  
![image of service masked](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/LNX_6/LNX_06a.png)  
Service masked.  

![image of masked service solved](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/LNX_6/LNX_06b.png)  
Service masked solved. 

![image of telnet daemon started](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/LNX_6/LNX_06c.png)  
Daemon started. 

![image of pid, memory and service stopped](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/LNX_6/LNX_06d.png)  
PID, memory and service stopped. 

