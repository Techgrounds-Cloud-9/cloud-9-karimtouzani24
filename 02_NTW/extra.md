# Subject
Subnetting.  

## Exercise  
Maak een netwerkarchitectuur die voldoet aan de volgende eisen:
- 1 private subnet dat alleen van binnen het LAN bereikbaar is. Dit subnet moet minimaal 15 hosts kunnen plaatsen.  

- 1 private subnet dat internet toegang heeft via een NAT gateway.  
Dit subnet moet minimaal 30 hosts kunnen plaatsen (de 30 hosts is exclusief de NAT gateway).  
 
### Overcome challenges
For the first exercise we are need a private subnet for 15 hosts. Layer 2 switches do not use IP addresses,  
so we use a layer 3 switch. The available hosts for /27 is 32-2 = 30 and for /28 is 16-2 = 14,  
so we are going to use 192.168.0.0/27.  
the 192.168.0.1 is the first host and the 192.168.0.30 the last host. 0 and 31 are not used because 0 is the subnet ID  
and 31 is the broadcast address. 32 will be the next subnet ID. 

The second exercise we need to connect to the internet, so we need a router.  
The router uses NAT, with NAT we can use the public IP address of the router to connect to the internet.  
We need 30 available hosts + the ip address for the NAT gateway is 31. A /27 has only 32-2 = 30 available.  
So we need to use a /26, which has a max of 64-2 = 62 hosts. 
these are the private IP addresses to communicate locally:
192.168.0.0/26 is the subnet ID  
192.168.0.1/26 for the NAT gateway  
192.168.0.63/26 is the broadcast address
from 192.168.0.2 to 192.168.0.62 are the available hosts.  
The router (NAT device) needs a public IP address to communicate with other networks over the internet.  

To calculate the hosts you can use https://www.subnet-calculator.com/subnet.php?net_class=C or do this manually.

### Results
![image exercise 1](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/NTW/NTW_6extra/1subnetting.png)  
Image of exercise 1  



![image exercise 2](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/NTW/NTW_6extra/2subnetting.png)
Image of exercise 2