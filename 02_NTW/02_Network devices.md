# Subject
Network Devices

## Key terminology
hub:  
- connects multiple computer networking devices together.
- also acts as a repeater.
- no packet filtering or addressing function. They just send the data to all connected devices.  
- physical layer device. 
- simple and multiport. 

switch:  
- more intelligent than hubs. Can read MAC addresses to transmit to appropriate destination. 
- better performance and security than hubs.  
- switch can work at Data link layer and Network layer. 
- the multilayer switch can act as switch and router.  

router:  
- Passes information between two or more computer networks.
- it inspects the packet's destination IP address, calculates the best way and forwards it.  
- Network layer.  

bridge:  
- used to connect 2 or more hosts or network segments together.
- they use MAC addresses to decide to forward or block the data from crossing.  
- Data link layer.  

gateway:  
- gateways connect two or more autonomous networks, each with its own routing algorithms, protocols, 
topology, domain name service, and network administration procedures and policies.  
- it's a router with added translation functionality.
- work at the transport layer and above.  

modem:  
- Modems (modulators-demodulators) are used to transmit digital signals over analog telephone lines.  
- Digital signals are converted by the modem into analog signals of different frequencies and transmitted to a modem at the receiving location.  
- The receiving modem performs the reverse transformation and provides a digital output to a device connected to a modem, usually a computer.  
- physical and data link layer.   

repeater:  
- A repeater is an electronic device that amplifies the signal it receives.  
- receives a signal and retransmits it at a higher level or higher power so that the signal can cover longer distances.  
- Physical layer.  

access point:  
- wired or wireless connection, it commonly means a wireless device.   
- Operate either as a bridge connecting a standard wired network to wireless devices  
- or as a router passing data transmissions from one access point to another.  
- the Data Link layer 

These devices can also be virtualized. (AWS/Azure)  

DHCP server:  
- The DHCP server, automatically assigns IP addresses and other network configurations like subnet mask, 
default gateway, DNS server, and more to the connected devices so they can exchange information.

## Exercise  
1) Describe network devices:   

2) find your list of connected devices to your router and what are the additional information about these devices?  

3) Where is the DHCP server on your network? what are the configurations?

### Sources
https://blog.netwrix.com/2019/01/08/network-devices-explained/  

https://www.techtarget.com/searchnetworking/definition/router#:~:text=A%20router%20is%20a%20physical,and%20then%20forwards%20it%20accordingly.

https://en.wikiversity.org/wiki/Computer_Networks/Ipconfig/DHCP_Options

https://www.cloudns.net/blog/dhcp-server/  

https://www.efficientip.com/glossary/dhcp-lease/#:~:text=A%20DHCP%20lease%20is%20a,a%20limited%20period%20of%20time.


### Overcome challenges
1) See terminology  

2) To see the list of connected devices to my router, I had to find the IP address of the router first.  
I used the command ipconfig with powershell. The default gateway is the router.  
the IP address of the default gatway is used to enter the settings of the router by typing the ip address in the webbar.  
from here i had to give the username and password to be able to view the list. In the results you can see the list of connected devices.  

For every device on the list, you can find information about the name, MAC address,  
IP address, speed and connected to.  

3) The router is the DHCP server in my network, the ipconfig /all command shows DHCP is enabled and it has the same IP address as the router.  
It also shows when the lease of the assignment is obtained and when it expires.  


### Results  
![ip address router](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/NTW/NTW_2/ipconfig.png)  
The IP address of the router.  


![The connected devices](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/NTW/NTW_2/connected%20devices%20router.png)  


![location DHCP and its configurations](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/NTW/NTW_2/ipconfig%20all%20dhcp.png)  
