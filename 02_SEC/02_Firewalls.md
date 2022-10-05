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

https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04  

https://www.tecmint.com/setup-ufw-firewall-on-ubuntu-and-debian/  

https://ubiq.co/tech-blog/how-to-change-default-index-page-in-apache/  

https://www.howtogeek.com/devops/how-to-find-your-apache-configuration-folder/  

https://www.vultr.com/docs/how-to-configure-uncomplicated-firewall-ufw-on-ubuntu-20-04/  

https://www.cyberciti.biz/faq/how-to-configure-firewall-with-ufw-on-ubuntu-20-04-lts/  

https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands  

https://www.tecmint.com/setup-ufw-firewall-on-ubuntu-and-debian/

### Overcome challenges
I have installed apache2. To check the default page, I have two options. To open the index.html file in /var/www/html with the cat command  
or to see the file in a webbrowser, by entering the host IP address and webport, see results.  

The firewall is disabled. Before enabling the firewall it's important to add rules to firewall to allow ssh traffic. This prevents you from getting locked out. To add ssh, I used the command sudo ufw allow ssh and also for the specific port sudo ufw allow 52209/tcp.  

To check what is allowed and what is denied I used the command sudo ufw status. This showed that the ssh trafic and webtrafic is allowed.  

To deny webtraffic I used the commands sudo ufw deny http, and also the same command is used to deny Apache Full and https, to deny all webtraffic. SSH is still allowed.  
  
To check if the firewall works I opened the webbrowser to reach the webserver as in the first part of this exercise. Now it was not possible because of the firewall is doing its work.  

### Results  
![index.html](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/SEC/index1.png)  
index.html is the default webpage.  


![webbrowser default webpage](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/SEC/apache%20works.png)  
The webbrowser shows the default webpage.  

![allow ssh and enable ufw](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/SEC/ssh_allow_ufw_enable.png)  
The ssh port is allowed en the ufw enabled.  

![webtraffic deny and ufw status](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/SEC/denywebtraffic.png)  
All webtraffic deny, and to check what is allowed and denied.  

![the webbrowser can't reach the webserver](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/SEC/firewall%20works.png)  
The firewall works, the webbrowser can't reach the webserver.  
