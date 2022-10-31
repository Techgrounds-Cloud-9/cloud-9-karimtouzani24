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
NAT  
Stands for network address translation. It’s a way to map multiple local private addresses to   
a public one before transferring the information.  

There are three different types of NATs. People use them for different reasons, but they all still work as a NAT.

1. Static NAT  
When the local address is converted to a public one, this NAT chooses the same one. This means there will be a consistent public IP address associated with that router or NAT device.

2. Dynamic NAT  
Instead of choosing the same IP address every time, this NAT goes through a pool of public IP addresses. This results in the router or NAT device getting a different address each time the router translates the local address to a public address.

3. PAT  
PAT stands for port address translation. It’s a type of dynamic NAT, but it bands several local IP addresses to a singular public one. Organizations that want all their employees’ activity to use a singular IP address use a PAT, often under the supervision of a network administrator.

private subnet:  
If it needs to talk to the internet, must do so through a Network Address Translation (NAT) gateway.  
The router itself does network address translation. Importantly a NAT won’t allow inbound traffic from the internet — that’s what makes a private subnet private. 

public subnet:  
A public subnet has an outbound route that sends all traffic through an Internet Gateway (IGW).  
The IGW lets traffic — IPv4 or IPv6 — out of the VPC without any constraints on bandwidth.  
Instances in public subnets can also receive inbound traffic through the IGW as long as their security groups and Network ACLs allow it.  

The other difference between a public and private subnet:   
A public subnet has a route table that says, “send all outbound traffic (anything to the CIDR block 0.0.0.0/0) via this internet gateway.”   
A private subnet either does not allow outbound traffic to the internet or has a route that says, “send all outbound traffic via this NAT gateway.”

difference NAT Gateway and Internet Gateway:  
Internet Gateway (IGW) allows instances with public IPs to access the internet.
NAT Gateway (NGW) allows instances with no public IPs to access the internet.  
NAT Gateway does something similar to Internet Gateway (IGW), but it only works one way: Instances in a private subnet can connect to services outside your VPC but external services cannot initiate a connection with those instances.

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

https://chrisguitarguy.com/2017/09/28/public-private-subnet-differences-aws-vpc/  

https://medium.com/awesome-cloud/aws-vpc-difference-between-internet-gateway-and-nat-gateway-c9177e710af6#:~:text=Internet%20Gateway%20(IGW)%20allows%20instances,IPs%20to%20access%20the%20internet.  

https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html  

https://www.subnet-calculator.com/

### Overcome challenges
I made 2 diagrams. I would like to show both, to show how i improved. 

I need 3 subnets:
Private subnet B needs 30 available hosts + the ip address for the NAT gateway is 31. 
A /27 has only 32-2 = 30 available.  
So we need to use a /26, which has a max of 64-2 = 62 hosts. 
192.168.0.0/26 is the subnet ID  
192.168.0.1/26 for the NAT gateway  
192.168.0.63/26 is the broadcast address
from 192.168.0.2 to 192.168.0.62 are the available hosts.  

For private subnet A we need 15 hosts. The available hosts for /27 is 32-2 = 30 and for /28 is 16-2 = 14,  
so we are going to use /27.  
the 192.168.0.64 wil be the subnet ID, because the broadcast address of the first subnet is 192.168.0.63.  
The first host wil be 192.168.65/27 and the last 192.168.0.94/27.  
The next IP address wil be the broadcast address, 192.168.0.95/27.

the subnet ID for the last subnet wil be the next IP address, 192.168.0.96
For public subnet A, 5 hosts and an internet gateway need an IP address.  
A /29 wil provide 8-2 = 6 hosts.  
192.168.0.97/29 wil be the first host and 192.168.0.102/27 the last host. 
192.168.0.97/29 wil be for the internet gateway and the other 5 are used for the hosts. 

The diagram is shown in the results. This diagram uses the least amount of addresses but is not very elastic,  
if the company grows it would be difficult to add hosts.  

That is why I made a new diagram and used the same amount of hosts, but here there is space to grow.  
For example I could change an /27 to /26 for more hosts in the future if needed.  
See the results.
 
To calculate the hosts you can use https://www.subnet-calculator.com/subnet.php?net_class=C or do this manually.

### Results  
![subnetting image](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/NTW/NTW_6/06_subnetting.png)  
concept  


![subnetting image 1](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/NTW/NTW_6/subnetV1.png)  
subnetting v1

