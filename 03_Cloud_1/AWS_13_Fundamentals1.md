Elastic Beanstalk:  
• Managed service for web applications on Amazon EC2 instances and Docker containers
• Deploys an environment that can include Auto Scaling, Elastic Load Balancing and databases
• Considered a Platform as a Service (PaaS) solution
• Allows full control of the underlying resources
• Code is deployed using a ZIP file, WAR file or Git repository  

Cloudfront:  
• CloudFront is a content delivery network (CDN) that allows you to store (cache) your content at “edge locations” located around the world
• This allows customers to access content more quickly and provides security against DDoS attacks
• CloudFront can be used for data, videos, applications, and APIs
• CloudFront reduces latency for global users  

Route53:  
• Route 53 is the AWS Domain Name Service
• Route 53 performs three main functions:
    - Domain registration – Route 53 allows you to register domain names
    - Domain Name Service (DNS) – Route 53 translates name to IP addresses using a global network of authoritative DNS servers
    - Health checking – Route 53 sends automated requests to your application to verify that it’s reachable, available and functional  

• Amazon Route 53 Routing Policies
    - Simple – IP address associated with name
    - Failover – if primary is down, route to secondary
    - Geolocation – route based on geographic location of request
    - Geoproximity – route to closes Region withing geo area
    - Latency – use lowest latency route to resources
    - Multivalue answer – returns several IP addresses
    - Weighted – relative weights (e.g. 80%/20%)  

EFS:  
• Amazon Elastic File System (EFS)
• File-based storage system
• Uses the NFS protocol
• Can connect many EC2 instance concurrently
• EC2 instances can be connected from multiple AZs
• Only available for Linux instances
• Can connect instances from other VPCs  

RDS:  
• RDS uses EC2 instances, so you must choose an instance family/type
• Relational databases are known as Structured Query Language (SQL) databases
• RDS is an Online Transaction Processing (OLTP) type of database
• Easy to setup, highly available, fault tolerant, and scalable
• Common use cases include online stores and banking systems
• Can encrypt your Amazon RDS instances and snapshots at rest
• Encryption uses AWS Key Management Service (KMS)
• Amazon RDS supports the following database engines:
• SQL Server, Oracle, MySQL Server, PostgreSQL, Aurora,MariaDB
• Scales up by increasing instance size (compute and storage)
• Read replicas option for read heavy workloads (scales out for reads/queries only)
• Disaster recovery with Multi-AZ option  

Aurora:  
• Amazon Aurora is an AWS database offering in the RDS family
• Amazon Aurora is a MySQL and PostgreSQLcompatible relational database built for the cloud
• Amazon Aurora features a distributed, fault-tolerant, selfhealing storage system that auto-scales up to 128TB per database instance  

Practical exercise:  

EFS  

Exercise:  
Create an Amazon EFS file system, launch a Linux virtual machine on Amazon EC2, mount the file system, create a file, terminate the instance, and delete the file system.  

To create a file system, just go to the EFS page and click on create file system. I created a new security group allowing ssh and nfs. EFS only works on linux,  
so i created two linux instances in different AZ. I connected to the instances and mounted the filesystems, first i had to install the amazon-efs-utils package, then made a efs directory  
then mounted the efs file (if you click on attach you can see which code to use). Then created a file in the efs directory in one instance to see if it is shared with the instance in the other AZ.  

Result:  
![efs created](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/418480e35ed4bcc6637cd378f7c141f5550e8371/00_includes/AWS/EFS/efs1.png)  
- EFS created  

![EC2 instances created](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/418480e35ed4bcc6637cd378f7c141f5550e8371/00_includes/AWS/EFS/efs2%20instance%20created%20zones.png)  
- 2 EC2 instances created in different AZ.  

![connected to EC2](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/418480e35ed4bcc6637cd378f7c141f5550e8371/00_includes/AWS/EFS/efs3%20ec2%20connected.png)  
- conncected to the instances.  

![install amazon-efs-utils](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/418480e35ed4bcc6637cd378f7c141f5550e8371/00_includes/AWS/EFS/efs4%20ec2%20install%20efs%20utils.png)  
- To mount EFS on the instance first you have to install amazon-efs-utils package.  

![result](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/418480e35ed4bcc6637cd378f7c141f5550e8371/00_includes/AWS/EFS/efs5%20result.png)  
- An EFS directory is created and the EFS is mounted to the directory. In the directory a file is created. This file is shared with the other instance in the other AZ.  


Source:  
https://aws.amazon.com/getting-started/tutorials/create-network-file-system/  

https://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-helper-ec2-linux.html

https://www.youtube.com/watch?v=Aux37Nwe5nc  

https://www.youtube.com/watch?v=4jy2FILK5R8  
<p>&nbsp;  </p>  
 RDS

