# Subject
Virtual Private Cloud (VPC)

Amazon VPC is typically described as a virtual private data center in the cloud. It is a virtual network that is logically isolated from other VPCs.
With a VPC you have full control over the design of the network. You can create subnets, internet gateways (igw), NAT gateways, VPN connections, and more.

There is always a default VPC when you create a new AWS account, but you can add up to 5 non-default VPCs per region per account. This is a soft limit. That is, you can request the limit to be raised.
Many services, like EC2, RDS and ECS require a VPC to be placed into.

When you create a VPC, you must assign a CIDR block. Choose your CIDR block and subnet mask carefully, as they have to allow for enough subnets and hosts and cannot be changed after creation.

Subnets can be either public or private. The only difference is that private subnets do not have an entry for the internet gateway (igw) in their route table, where public subnets do. In other words, private subnets cannot access the internet without a NAT gateway or a NAT instance.

VPCs operate at the regional level, while subnets can only be placed into a single Availability Zone.

Elastic IPs are also available from the VPC menu. EIPs are public IP addresses that can be dynamically allocated to resources like EC2 instances or NAT gateways.

## Key terminology
Amazon Virtual Private Cloud (VPC)  
• A VPC is a virtual network dedicated to your AWS account  
• Analogous to having your own DC inside AWS  
• It is logically isolated from other virtual networks in the AWS Cloud  
• Provides complete control over the virtual networking environment  
• You can launch your AWS resources, such as Amazon EC2 instances, into your VPC  
• When you create a VPC, you must specify a range of IPv4 addresses for the VPC in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16  
• A VPC spans all the Availability Zones in the region  
• You have full control over who has access to the AWS resources inside your VPC  
• By default you can create up to 5 VPCs per region  
• A default VPC is created in each region with a subnet in each AZ

## Exercise
Exercise 1  
- Allocate an Elastic IP address to your account.
- Use the Launch VPC Wizard option to create a new VPC with the following requirements:
    * Region: Frankfurt (eu-central-1)
    * VPC with a public and a private subnet
    * Name: Lab VPC
    * CIDR: 10.0.0.0/16  

- Requirements for the public subnet:
    * Name: Public subnet 1
    * CIDR: 10.0.0.0/24
    * AZ: eu-central-1a  

- Requirements for the private subnet:
    * Name: Private subnet 1
    * CIDR: 10.0.1.0/24
    * AZ: eu-central-1a  

Exercise 2
- Create an additional public subnet without using the wizard with the following requirements:  
    * VPC: Lab VPC
    * Name: Public Subnet 2
    * AZ: eu-central-1b
    * CIDR: 10.0.2.0/24  

- Create an additional private subnet without using the wizard with the following requirements:  
    * VPC: Lab VPC
    * Name: Private Subnet 2
    * AZ: eu-central-1b
    * CIDR: 10.0.3.0/24  

- View the main route table for Lab VPC. It should have an entry for the NAT gateway. Rename this route table to Private Route Table.  
- Explicitly associate the private route table with your two private subnets.  
- View the other route table for Lab VPC. It should have an entry for the internet gateway. Rename this route table to Public Route Table.  
- Explicitly associate the public route table to your two public subnets.  

Exercise 3
- Create a Security Group with the following requirements:  
    * Name: Web SG  
    * Description: Enable HTTP Access  
    * VPC: Lab VPC  
    * Inbound rule: allow HTTP access from anywhere  
    * Outbound rule: Allow all traffic  

Exercise 4
- Launch an EC2 instance with the following requirements:  
    * AMI: Amazon Linux 2  
    * Type: t3.micro  
    * Subnet: Public subnet 2  
    * Auto-assign Public IP: Enable  
    * User data:   
- Tag:  
    * Key: Name  
    * Value: Web server  
- Security Group: Web SG  
- Key pair: no key pair  
- Connect to your server using the public IPv4 DNS name.




### Sources
https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html  

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html  

https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html

### Overcome challenges


### Results