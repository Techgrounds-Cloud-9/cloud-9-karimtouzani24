# Subject
Elastic Compute Cloud (EC2)  

The service with which you can run Virtual Machines in AWS is called EC2. These VMs can be used for anything a regular server is used for. Since they’re located at a remote location, connecting to the machine has to be done via the internet. For a connection to Linux machines, you use the Secure Shell (ssh) protocol. For a connection to Windows machines, you use the Remote Desktop Protocol (RDP).  

When creating an EC2 instance, you first need to select an Amazon Machine Image (AMI). An AMI is a blueprint for your machine. It contains a template for the OS among other things.  

EC2 can have different sizes, called instance types. Every instance type has a different amount of (virtual)CPUs, memory, and network performance.  

For the root volume, an instance can use Elastic Block Store (EBS) or Instance store depending on its type. Instance store is known as ephemeral storage, while EBS is known as persistent storage.  

Every instance has a Security Group. This is a stateful firewall that works using explicit allow rules. By using the Security Group service, you don’t have to worry about firewalls on the OS level.  

With User Data you can specify a (bash) script that runs on boot. This is a way to quickly configure servers without having to log in and without doing any manual work.  

The price of an EC2 instance depends on the instance type, the AMI, the region it’s in, the number of seconds it’s running, and the type of purchase you make.  

On demand instances are the most expensive option, but they’re also the most flexible.
Reserved instances provide a greater discount depending on how much you pay up front. You can reserve instances only for 1 or 3 years.
Spot instances are generally considered the cheapest, but their availability depends on the demand, so they’re not always reliable.


## Key terminology
- Amazon EC2  
EC2 = elastic Compute Cloud = Infrastructure as a service. 
Is a web service that provides resizable computing capacity—literally, servers in Amazon's data centers—that you use to build and host your software systems.  

options:   
OS - linux, windows or mac os.  
CPU - how much compute power and cores  
RAM - how much random-acces memory  
storage - network-attached (EBS and EFS), hardware (EC2 instance store)  
network card - speed, public IP address  
firewall rules - security group  
bootstrap script -  EC2 user data (configures at first launch)  

launching an EC2 instance - select an instance type - an AMI.

EC2 user data  
To bootstrap our instances, means launching commands when a machine starts.  
that script is only run once at the instance first start.  

EC2 user data is used to automate boot tasks such as:  
installing updates/software or downloading common files from the internet.  

EC2 user data script runs with the root user.  

EC2 metadata is data about your EC2 instance. 

there different 7 types of instances. types for general purpose, compute optimized, memory optimized, accelerated computing, storage optimized, instance feature and measuring instance performance.  

general purpose instance type (T or M): great for diversity of workloads such as web servers or code repositories (balance between compute memory networking)  

compute optimized (C): great for compute intensive tasks for high performance processors (batch processing workloads, media transcoding, high perf. webservers and high perf. computing HPC, machine learning and dedicated gaming servers.)  

memory optimized (R, X): workloads that process large data sets in memory (high perf. databases, BI, applications performing real-time processing of big unstructured data.)

naming instance:  
t = instance class  
2 = generation  
micro = size within the instance class

example t2.mmicro (is part of the aws free tier up to 750 hours per month)

EC2 instance purchasing options:  
- on demand instances. short workload, predictable pricing, pay by second after the first minute for linux or windows, other OS by the hour. Higest cost but no upfront payment. No long term commitment. recommended for short-term un-interrupted workloads where you cant predict te behaviour.  

- reserved (1 or 3 years): 2 types, reserverd instances for long workloads and convertible reserved instances for long workload with flexible instance. Discount compared to on-demand. You reserve an attribute (instance type, region, tenancy, OS). payment options effect on discount, no opfront, partial upfront or all upfront. You can choose the regional or zonal scope. Recommended for database. You can buy and sell in the reserved instance marketplace. The convertible reserved instance less discount but more flexible because you can change type, OS, scope and tenancy.  

- saving plans (1 or 3 years): commitment to an amount os usage, long workload.  
Discount based on long-term usage (up to 72 procent, like RI), commit to a certain type of usage (10 dollar per hour for one year), usage beyond is billed at the on-demand price. locked to a specific instance family and region.  

- spot instances: short workload, cheap, can lose instances.  
can get a discount up to 90 procent compared to on-demand. useful for workloads that are resilient to failure (batch jobs, data analysis, image processing, workloads with a flexible start end time), not suitable for critical jobs or databases.  

- dedicated hosts: book an entire physical server, control instance placement.  
the most expensive option. useful for software that have complicated licensing model or for companies that have strong regulatory or compliance needs. Purchasing options are on demand or reserved.  

- dedicated instances: run on hardware that is dedicated to you, may share hardware with other instances in same account, no control over instance placement. 

- capacity reservations: reserve capacity in a specific AZ for any duration.  
you always have acces to ec2 capacity when you need it. No time commitment (create/cancel anytime). Combine with regional reserved instances and saving plans to benifit from discounts. you are charged at on-demand rate wheter you run instances or not. suitable for shor term, uninterrupted workloads that needs to be in a specific AZ.  

Amazon lightsail is a simple version of EC2. Used when simple virtual server is required by a user with little or no AWS experience.

## Exercise
Exercise 1  

Navigate to the EC2 menu.  
Launch an EC2 instance with the following requirements:  
- AMI: Amazon Linux 2 AMI (HVM), SSD Volume Type  
- Instance type: t2.micro  
- Default network, no preference for subnet  
- Termination protection: enabled  

User data:
#!/bin/bash
 yum -y install httpd
systemctl enable httpd
systemctl start httpd
 echo '<html><h1>Hello From Your Web Server!</h1></html>' >   /var/www/html/index.html  

- Root volume: general purpose SSD, Size: 8 GiB  
- New Security Group:  
Name: Web server SG
Rules: Allow SSH, HTTP and HTTPS from anywhere

Exercise 2
- Wait for the Status Checks to get out of the initialization stage. When you click the Status Checks tab, you should see that the System reachability and the Instance reachability checks have passed.  
- Log in to your EC2 instance using an ssh connection.
- Terminate your instance.

### Sources
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html

### Overcome challenges
launching the instance was easy. Just followed the steps to fill in the requirements and connected with the instance connect option. To terminate the instance I had to search how to disable the termination protection. This is done withn the instance settings.

### Results  
![ec2 instance created](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/75710020ecafe283afa203a47288555ef39b7ce4/00_includes/AWS/EC2/ec2e1a.png)  
EC2 instance created and running.  

![connected to instance with instance connect](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/75710020ecafe283afa203a47288555ef39b7ce4/00_includes/AWS/EC2/ec2e1b.png)  
Connected to the instance. Instance connect is used.  

![change termination protection](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/75710020ecafe283afa203a47288555ef39b7ce4/00_includes/AWS/EC2/ec2e1c.png)  
To terminate the instance, the termination protection option should be disabled.  

![uncheck enable](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/75710020ecafe283afa203a47288555ef39b7ce4/00_includes/AWS/EC2/ec2e1d.png)  
uncheck enable to terminate the instance.  
