# Subject
Protocols

## Key terminology
wireshark:  
- a free and open-source packet analyzer. It is used for network troubleshooting, analysis, software, and communications protocol development.  
- It lets you see what’s happening on your network at a microscopic level  
- Wireshark is a cross-platform tool that runs on Linux, Microsoft Windows, macOS, BSD, Solaris, and other Unix-like operating systems.  

what wireshark is used for:  
- Network administrators use it to troubleshoot network problems
- Network security engineers use it to examine security problems
- Developers use it to debug protocol implementations
- Others use it to learn network protocol internals

## Exercise  
1) Identify several other protocols and their associated OSI layer. Name at least one for each layer.
2) Figure out who determines what protocols we use and what is needed to introduce your own protocol.
3) Look into wireshark and install this program. Try and capture a bit of your own network data. Search for a protocol you know and try to understand how it functions.


### Sources
https://osi-model.com/physical-layer/  

https://www.linuxandubuntu.com/home/how-to-use-wireshark-to-inspect-network-traffic  

https://www.router-switch.com/faq/what-is-presentation-layer-and-function.html  

https://www.comptia.org/content/guides/what-is-a-network-protocol#:~:text=The%20following%20groups%20have%20defined%20and%20published%20different,Union%20%28ITU%29%20The%20World%20Wide%20Web%20Consortium%20%28W3C%29  

https://www.internetx.com/en/news-detailview/who-creates-the-standards-and-protocols-for-the-internet/  

https://www.quora.com/How-do-you-write-your-own-protocol-that-sits-on-top-of-TCP-IP  

https://www.alphr.com/wireshark-filter-port/

### Overcome challenges  
1)the layers and it's protocols:  
- physical layer: Ethernet physical layer (10Base-T), USB, GSM, Bluetooth. 
- data link layer: ARP, NDP, ethernet.
- network layer: IPv4, IPv6, ICMP, IGMP.
- transport layer: TCP and UDP
- session layer: NetBIOS, PAP, PPTP.
- presentation layer: telnet, Lightweight Presentation Protocol (LPP)
- application layer: HTTP, LDAP, NTP.

2) These are the organizations that help define internet protocols and standards
Technical experts, academics, and policy-makers have come together under the roof of organizations that can ensure the interoperability of the internet: 

- world wide web consortium (W3C)
- Institute of Electrical and Electronics Engineers (IEEE)
- Internet Engineering Task Force (IETF)
- International Organization for Standardization (ISO)
- International Telecommunications Union (ITU)  

For you to create your own protocol it has to be on top of the transport layer. So the data reaches the application layer.  
You can choose TCP or UDP.  

3) I have installed Wireshark on my machine. To show it is working I started capturing packages, then I opened a webbrowser. To find what I did on the network, I filtered to see only tcp port 443. In the results it shows the information about this activity and information about the data link, internet and transport layer.   
like for transport layer TCP is used.  
In the network layer, IPv4 is used and the source and destination are visible.  
Ethernet II shows the data link layer, the MAC addresses of the source and destination. 
### Results