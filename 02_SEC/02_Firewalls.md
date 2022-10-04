# Subject
Firewalls

## Key terminology
Firewall:  
A firewall is a network security device that monitors incoming and outgoing network traffic and decides whether to allow or block specific traffic based on a defined set of security rules.  

A firewall can be hardware, software, software-as-a service (SaaS), public cloud, or private cloud (virtual).  

firewalld:  
FirewallD uses zones and services instead of iptables chain and rules.  
Zones are a set of rules that specify what traffic should be allowed depending on the level of trust you have in a network your computers connected to. Network interfaces assigned a zone to dictate a behavior that the firewall should allow.  

ufw:  
The default firewall configuration tool for Ubuntu is ufw. Developed to ease iptables firewall configuration, ufw provides a user friendly way to create an IPv4 or IPv6 host-based firewall. By default UFW is disabled.  

When you turn UFW on, it uses a default set of rules (profile). All 'incoming' is being denied, with some exceptions to make things easier for home users.

iptables:  
A firewall program for Linux. It will monitor traffic from and to your server using tables.  
These tables contain sets of rules, called chains, that will filter incoming and outgoing data packets.

Packet-filtering firewalls:  
- The most common type of firewall, examine packets and prohibit them from passing through if they don’t match an established security rule set.  
This type of firewall checks the packet’s source and destination IP addresses.  
If packets match those of an “allowed” rule on the firewall, then it is trusted to enter the network.  

- they can't determine if the contents of the request that's being sent will adversely affect the application it's reaching.  
Next-generation firewalls and proxy firewalls are more equipped to detect such threats.

Packet-filtering firewalls are divided into two categories: stateful and stateless

stateful firewall:  
remember information about previously passed packets and are considered much more secure.  

stateless firewall:  
Examine packets independently of one another and lack context, making them easy targets for hackers.  

Next Generation Firewall (NGFW):  
Deep packet inspection Firewall with application-level inspection.  

Proxy service:  
Network security system that protects while filtering messages at the application layer.

hardware firewall:  
A physical firewall is a piece of equipment installed between your network and gateway.  

software firewall:  
A software firewall is a program installed on each computer and regulates traffic through port numbers and applications

## Exercise  
- Installeer een webserver op je VM.
- Bekijk de standaardpagina die met de webserver geïnstalleerd is.
- Stel de firewall zo in dat je webverkeer blokkeert, maar wel ssh-verkeer toelaat.
- Controleer of de firewall zijn werk doet.

### Sources
https://www.forcepoint.com/cyber-edu/firewall  

https://www.cisco.com/c/en/us/products/security/firewalls/what-is-a-firewall.html  

https://www.checkpoint.com/cyber-hub/network-security/what-is-firewall/  

https://help.ubuntu.com/community/UFW  

https://www.digitalocean.com/community/tutorials/how-to-setup-a-firewall-with-ufw-on-an-ubuntu-and-debian-cloud-server  

https://www.hostinger.com/tutorials/iptables-tutorial  

https://support.kaspersky.com/KICSforNetworks/2.9/en-US/151470.htm

### Overcome challenges


### Results