# Subject


## Key terminology
Nmap:  
short for Network Mapper, is a free and open source tool used for vulnerability checking, port scanning and, of course, network mapping  

Wireshark:  
Wireshark is a free open source tool that analyzes network traffic in real-time for Windows, Mac, Unix, and Linux systems.  
It captures data packets passing through a network interface (such as Ethernet,  LAN, or SDRs)  
and translates that data into valuable information for IT professionals and cybersecurity teams.

Wireshark is a type of packet sniffer (also known as a network protocol analyzer, protocol analyzer, and network analyzer).  
Packet sniffers intercept network traffic to understand the activity being processed and harvest useful insights.


## Exercise  
Scan the network of your Linux machine using nmap. What do you find?  

Open Wireshark in Windows/MacOS Machine. Analyse what happens when you open an internet browser.  
(Tip: you will find that Zoom is constantly sending packets over the network. You can either turn off Zoom for a minute, or look for the packets sent by the browser between the packets sent by Zoom.)


### Sources
https://unixcop.com/how-to-install-and-use-nmap-on-ubuntu/  

https://phoenixnap.com/kb/how-to-find-ip-address-linux  

https://sourcedigit.com/25899-find-my-ip-address-in-ubuntu-terminal/

https://www.networkworld.com/article/3296740/what-is-nmap-why-you-need-this-network-mapper.html  

https://www.wireshark.org/docs/wsug_html_chunked/ChapterIntroduction.html
### Overcome challenges
I have installed nmap on the linux machine. To find my IP address I used the command hostname -i.  
There are more options to find the IP address, like the command ip a or ifconfig.  
To scan the network of the linux machine I used the command sudo nmap -sS and the IP address.  
It showed the open ports, which are ssh 22/tcp, telnet 23/tcp and http 80/tcp.  

The next exercise shows what happens in Wireshark when I open a webbrowser.  
I used a filter to show all 443 packets, while I opened the webbrowser. The result is a lot of packets are send.  
To show the difference, I opened the same webbrowser but used another filter (ssh, 22). Now no packets are send.  
Wireshark shows all network traffic or you can filter it to look specific.

### Results  
![image of nmap in action](https://raw.githubusercontent.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/main/00_includes/SEC/nmap_exercise.png)  
Nmap 