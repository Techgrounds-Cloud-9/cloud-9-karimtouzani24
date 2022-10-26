# Subject
Security Groups

Security groups. A firewall that controls traffic to and from an ENI / EC2 instance.  
Security Groups are stateful virtual firewalls that can be assigned to instances. They do not run in the OS, but rather in the VPC.  

One Security Group can be assigned to multiple instances. The other way around, one instance can have up to 5 Security Groups.

Security Groups only have allow rules. Everything not explicitly allowed is automatically implicitly denied.  
Rules include IP addresses and other security groups.  

NACL. A firewall that controls traffic to and from subnets.  
A Network Access Control List (NACL) is a stateless firewall that runs on the subnet level in a VPC.
A NACL has both explicit allow and deny rules. Rules only include IP addresses.  
Rules have a number assigned to them. This number indicates the order in which the rules are applied.

By default, a NACL is configured to allow all traffic in and out of the network.  

## Key terminology
difference security groups and Network ACLs:  

- SG operate at instance level and the NACL at the subnet level.  
- SG support allow rules only and the NACL support s allow and deny rules.  
- SG is stateful, return traffic atuomatically allowed regardless of any rules. NACL is stateless, return traffic must be explicitly allowed by rules.  
- SG evaluate all rules to decide to allow traffic. NACL process rules in number order to decide to allow.  
- SG applies to an instance only if you specify when launching or associate the SG later with the instance. NACL automatically applies to all instances in the subnets its associated with. (therfore you dont have to rely on users to specify the SG)

## Exercise
study:  
Security Groups in AWS
Network Access Control Lists in AWS  

### Sources
https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html  
