# Subject
OSI Stack

## Key terminology
the OSI model 

the TCP/IP model


## Exercise  
Study the OSI and TCP/IP models.

### Sources
https://www.geeksforgeeks.org/layers-of-osi-model/  

https://www.imperva.com/learn/application-security/osi-model/  

https://www.practicalnetworking.net/series/packet-traveling/osi-model/



### Overcome challenges
No challenges, information easy to find on the internet. 

### Results  
The OSI model:  
The Open Systems Interconnection (OSI) model describes 7 layers that computer systems uso to communicate over a network. This is the first Model used to communicte over a network. All these layers work collaboratively to transmit the data from one person to another across the globe.
Modern internet is not based on OSI, but on the TCP/IP model.  
Today the OSI model is used to help visualize and communicate how networks operate, and helps isolate and troubleshoot networking problems.  

the OSI layers:  
1 physical layer  
- responsible for the physical connection between devices.  
- responsible for transmitting bits, the 1s and 0s.
- connectors, cables and the wireless technology connecting the devices.  
- bits

2 Data link layer  
- responsible for getting data to nodes on the same network (ethernet) using MAC addresses.  
- Has 2 sublayers, the logic link control and the media access control.  
- frames 

3 Network layer  
- allows different networks to communicate with each other (routers), using IP addresses.  
- 2 functions: 1) logical addressing (IP). 2)Routing (best path).  
- packets

4 Transport layer 
- sorts out which client and server programs are supposed to get the data.  
- most common are TCP (connection oriented, data is reliable delivered) and UDP (connectionless, not reliably delivered).  
- flow control and error control.  
- segments.  

5 Session layer  
- responsible for opening sessions (communication channels) end closing them when communication ends.  
- So responsible for the establishment of connection, maintenance, authentication and security.
- can also set checkpoints during data transfer.  

6 Presentation layer 
- The data from the layer above (application layer) is extracted here and manipulated to the required format to transmit over the network.  
- functions: translation, encryption, compression.  

7 Application layer  
- used by end-user software (like web browser).
- provides protocols that allow software to send and receive information and present meaningful data to users.  

TCP/IP model:
- Uses 5 layers instead of 7. 
- the physical layer (OSI) is called hardware.
- data link layer (OSI) is called Network interface.  
- Network layer (OSI) called Internet layer
- Transport is the same.
- but the application, presentation and session layer are combined in one layer, called the application layer. 

