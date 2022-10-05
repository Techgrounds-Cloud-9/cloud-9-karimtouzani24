# Subject
IP addresses

## Key terminology  
IP addresse is a unique address that identifies a device on the internet or a local network

IPv4 addresses  
- contain 32 bits (4 bytes)
- written in decimal  
- every block between the points are 1 byte.
- max value of 1 byte is 255
- broadcast, unicst and multicast. 
- configured manualy or DHCP 

All IP addresses are sold out. (public IP). We can use private IP addresses with NAT  
to allow multiple devices to access the Internet through a single public address.  

Private IP addresses are non-routable on the Internet. The address is basically assigned by the network router to your particular device.  
The unique private IP address is provided to every device which is on the same network.  
In this way, devices communicate with one another on the same network without connecting to the entire Internet.  

Private IP address exists within the specific ranges as reserved by the Internet Assigned Numbers Authority (IANA). Following are the address ranges of private IP addresses:  
- In Class A, the address range assigned to Private IP Address: 10.0.0.0 to 10.255.255.255
- In Class B, the address range assigned to Private IP Address: 172.16.0.0 to 172.31.255.255
- In Class C, the address range assigned to Private IP Address: 192.168.0.0 to 192.168.255.255  

Private IP addresses (local reach) can be reused on another network which is not possible with Public IP addresses (global reach).  
Private are free, public are not. Public are assigned and controlled by your internet service provider.  
Private are assigned to your specific device within a private network. 

IPv6 addresses
- contain 128 bits.
- written in hexadecimal  
- huge amount of ip addresses  
- no subnetting problems  
- more secure than ipv4  
- unicast, multicast and anycast.  
- configured manualy, SLAAC or DHCPv6. 
- but harder to configure, difficult to remember and not supported by all websites.  


## Exercise  
- Ontdek wat je publieke IP adres is van je laptop en mobiel op wifi.  
Zijn de adressen hetzelfde of niet? Leg uit waarom.  

- Ontdek wat je privé IP adres is van je laptop en mobiel op wifi.  
Zijn de adressen hetzelfde of niet? Leg uit waarom.  

Verander het privé IP adres van je mobiel naar dat van je laptop. Wat gebeurt er dan?  

Probeer het privé IP adres van je mobiel te veranderen naar een adres buiten je netwerk.  
Wat gebeurt er dan?

Tip: vergeet niet je instellingen weer terug te zetten wanneer je klaar bent met de opdracht.


### Sources
https://www.geeksforgeeks.org/network-address-translation-nat/  

https://www.geeksforgeeks.org/private-ip-addresses-in-networking/?ref=gcse  

https://www.kaspersky.com/resource-center/definitions/what-is-an-ip-address  

https://nordvpn.com/nl/blog/ipv4-vs-ipv6/  

https://www.avast.com/c-ip-address-public-vs-private#:~:text=A%20public%20IP%20address%20identifies,devices%20within%20that%20same%20network.  

https://www.howtogeek.com/117371/how-to-find-your-computers-private-public-ip-addresses/

### Overcome challenges
The easiest way to find your public IP address is by asking a website, since that website sees your public IP address and can tell it to you.  
I userd the site ip4.me. It’s quick, ad-free, and will show your IPv4 address. You can Also acces the routers administration page.  
ALso on your mobile you can search a website for your public IP. The laptop and mobile will show the same public IP address, with NAT all these devices (with private IP address) will acces the internet.  

The devices have different private IP addresses, so they can communicate with each other on the same network.  
I manually changed the private ip address on my mobile to the same Ip address of my laptop to show this will not work. The mobile has no connection because devices can't have the same ip addresses. See results.  

When manually changing the private ip address of the mobile to an address outside the network it will also disconnect, see results,  
because the IP addresses should be on the same network to be able to communicate with each other. 




### Results  
![public IP shown by website](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/NTW/NTW_5/publicIPwebsite.png)  
Using a website to find your public IP address.  

![public IP shown by router page](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/NTW/NTW_5/publicIProuter.png)  
Using the routers administration page to show your public IP.  

![public IP shown on mobile](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/NTW/NTW_5/ipmobiel.png)   
Using your mobile to show your public ip, using a website.  

![laptop private ip address using ipconfig](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/NTW/NTW_5/ipconfig%20ntw.png)   
Using ipconfig to find your private ip on your laptop.  



![mobile private ip address using the settings](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/main/00_includes/NTW/NTW_5/private%20ip%20mobile.png)  
Using the settings in your mobile to find your private ip.  

![same private ip for mobile and laptop](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/NTW/NTW_5/same%20ip%20mobile%20and%20laptop.png)  
Changing the private IP address of the mobile to the same IP address of the laptop, no connection possible.   


![private ip addresses not on same network](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/NTW/NTW_5/mobile%20extern%20private%20ip.png)  
No connection possible if the private IP addresses are not on the same network. 
