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