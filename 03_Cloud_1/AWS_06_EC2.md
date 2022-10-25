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
launching the instance was easy. Just followed the steps to fill in the requirements. To terminate the instance I had to search how to disable the termination protection. 

### Results  
![ec2 instance created](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/75710020ecafe283afa203a47288555ef39b7ce4/00_includes/AWS/EC2/ec2e1a.png)  
EC2 instance created and running.  

![connected to instance with instance connect](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/75710020ecafe283afa203a47288555ef39b7ce4/00_includes/AWS/EC2/ec2e1b.png)  
Connected to the instance. Instance connect is used.  

![change termination protection](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/75710020ecafe283afa203a47288555ef39b7ce4/00_includes/AWS/EC2/ec2e1c.png)  
To terminate the instance, the termination protection option should be disabled.  

![uncheck enable](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/75710020ecafe283afa203a47288555ef39b7ce4/00_includes/AWS/EC2/ec2e1d.png)  
uncheck enable to terminate the instance.  
