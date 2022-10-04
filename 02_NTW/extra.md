# Subject
Subnetting.

## Key terminology
Network:  
A network is a group of two or more computers or other electronic devices that are interconnected for the purpose of exchanging data and sharing resources.  

LAN:   
A Local Area Network, A local area network (LAN) is a collection of devices connected together in one physical location,  
such as a building, office, or home. A LAN can be small or large,  
ranging from a home network with one user to an enterprise network with thousands of users and devices in an office or school.  

A range of private Ip addersses are assigned to a LAN, every device gets it's own IP address from the range.  

subnet mask (prefix):  
Subnet mask defines the range of IP addresses that can be used within a network or subnet.  
It also separates an IP address into two parts: network bits and host bits. The 255 parts are the network part and the 0s the host.

CIDR notation:  
Describing the network prefix’s width as a single number, e.g. 192.168.0.1/24.  
Instead of the 255.255.255.0 the /24 is used.  

available valid hosts depends on block size in subnetting:  
Block size is the sum of network address, valid host addresses and broadcast address. For example, if in a network there are 6 valid hosts than block size of that network is 8 (1 network address + 6 valid hosts + 1 broadcast address).  

NAT:  
NAT stands for network address translation. It’s a way to map multiple local private addresses to   
a public one before transferring the information.  

There are three different types of NATs. People use them for different reasons, but they all still work as a NAT.

1. Static NAT
When the local address is converted to a public one, this NAT chooses the same one. This means there will be a consistent public IP address associated with that router or NAT device.

2. Dynamic NAT
Instead of choosing the same IP address every time, this NAT goes through a pool of public IP addresses. This results in the router or NAT device getting a different address each time the router translates the local address to a public address.

3. PAT
PAT stands for port address translation. It’s a type of dynamic NAT, but it bands several local IP addresses to a singular public one. Organizations that want all their employees’ activity to use a singular IP address use a PAT, often under the supervision of a network administrator.

## Exercise  
Maak een netwerkarchitectuur die voldoet aan de volgende eisen:
- 1 private subnet dat alleen van binnen het LAN bereikbaar is. Dit subnet moet minimaal 15 hosts kunnen plaatsen.  

- 1 private subnet dat internet toegang heeft via een NAT gateway.  
Dit subnet moet minimaal 30 hosts kunnen plaatsen (de 30 hosts is exclusief de NAT gateway).  

- 1 public subnet met een internet gateway. Dit subnet moet minimaal 5 hosts kunnen plaatsen (de 5 hosts is exclusief de internet gateway).  

- Plaats de architectuur die je hebt gemaakt inclusief een korte uitleg in de Github repository die je met de learning coach hebt gedeeld.


### Sources
https://www.ionos.com/digitalguide/server/know-how/what-is-a-network/  

https://www.cisco.com/c/en/us/products/switches/what-is-a-lan-local-area-network.html  

https://www.freecodecamp.org/news/subnet-mask-definition/  

https://www.shellhacks.com/cidr-notation-explained-examples/  

https://www.computernetworkingnotes.com/ccna-study-guide/subnetting-tutorial-subnetting-explained-with-examples.html  

https://www.youtube.com/watch?v=_opHbSebrK0  

https://community.fs.com/blog/layer-2-switch-vs-layer-3-switch-which-one-do-you-need.html  

https://www.comptia.org/content/guides/what-is-network-address-translation#:~:text=NAT%20stands%20for%20network%20address,as%20do%20most%20home%20routers.  

https://www.geeksforgeeks.org/difference-between-private-and-public-ip-addresses/

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