# Subject
Elastic Load Balancing (ELB) & Auto Scaling

One of the main advantages of the cloud is that you don’t need to guess how much capacity you need. You can always scale up and down with on-demand services. One of the services that enables this is called Auto Scaling.

When you run an application with a spiky workload, you can host the application on a fleet of EC2 instances instead of a single server. When the demand for the application is high, Auto Scaling can automatically add instances to the fleet. When the demand is lower, it can similarly remove instances.

To make sure all servers are the same, Auto Scaling makes use of a (custom) AMI. Auto Scaling makes use of CloudWatch metrics to determine whether to add or remove instances.

In a traditional architecture, a client connects to a single server with a single IP address. When dealing with a fleet of servers, this would not work. Therefore, a load balancer can be introduced as a connection endpoint for the client. The load balancer will forward the request to one of the servers in the fleet, and relay the response back to the client.

AWS’ ELB is a managed service that provides load balancing to a fleet of instances. There are four types of ELBs, They all feature the high availability, automatic scaling, and robust security that help make your applications fault tolerant:  

- Application Load Balancer: this ELB works using HTTP and HTTPS protocols (layer 7 of the OSI stack).  

- Network Load Balancer: this ELB works using TCP and UDP (layer 4 of the OSI stack). Because it handles millions of requests per second while maintaining ultra-low latencies, the Network Load Balancer works well for applications that require extreme performance.  

- Classic Load Balancer: this ELB is outdated and not recommended for use. AWS has (so far) never stopped supporting any services. The reason for this is that it can harm existing applications.  

- Gateway Load Balancer: this ELB acts as a gateway into your network, as well as a load balancer. It will first route traffic to a (3rd party) application that checks the traffic, like an IDS/IPS or Firewall. After the packet has been inspected, the GWLB acts like a NLB routing to your application. GWLB act on layers 3 and 4 of the OSI stack.

## Key terminology
As mentioned previously, a load balancer distributes workloads across multiple compute resources, such as virtual servers. ELB load balancers can be configured in the Amazon EC2 service area in the AWS Management Console. Alternatively, you can invoke the service through the AWS Command Line Interface (AWS CLI) or software development kits (SDKs).  

Key features of ELB load balancers include:  

• High availability (HA) – ELB load balancers can distribute traffic across multiple targets—including EC2 instances, containers, and IP addresses—in a single Availability Zone or multiple Availability Zones.  

• Health checks – ELB load balancers can be configured to detect unhealthy targets, stop sending traffic to them, and then spread the load across the remaining healthy targets.  

• Security – You can create and manage security groups that are associated with load balancers. You can also create an internal (non-internet-facing) load balancer.  

• Transport Layer Security (TLS) termination  

• Layer 4 or layer 7 load balancing:  
    • You can load balance Hypertext Transfer Protocol (HTTP) and Secure HTTP (HTTPS) applications for features that are specific to layer 7. Recall that Layer 7 is the application layer in the Open Systems Interconnection (OSI) model.  
      
    • You can also choose to use only layer 4 load balancing for applications that rely purely on TCP. Recall that Layer 4 is the transport layer in the OSI model.  

• Operational monitoring – ELB load balancers can work with Amazon CloudWatch metrics and request tracing. You can use these resources to monitor application performance in real time.  

A load balancer is used for many reasons:  

• To secure access to your web servers through a single exposed point of access  
• To decouple your environment by using both public and internal load balancers  
• To provide high availability and fault tolerance with the ability to distribute traffic across multiple Availability Zones  
• To increase elasticity and scalability with minimal overhead  
- The Application Load Balancer also offers deletion protection and request tracking, enhanced metrics and access logs, and targeted health checks  

Application Load Balancer routes and organizes backend targets. When you configure listeners for the load balancer, you create rules to direct how requests that the load balancer receives are routed to the backend targets. To register those targets to the load balancer and to configure the health check that the load balancer uses for the targets, you create target groups. As the diagram shows, targets can also be members of multiple target groups.  

Before you start using your Application Load Balancer, you must add one or more listeners.
A listener is a process that checks for connection requests from a client to an instance by using the protocol and port that you specify.
The listener rules that you define also determine how the load balancer routes traffic from connecting clients to one or more targets or target groups.  

Amazon EC2 Auto Scaling helps you maintain application availability. It enables you to automatically add or remove Amazon Elastic Compute Cloud (Amazon EC2) instances according to conditions that you define.  
- based on health status checks  
- user-defined policies that are driven by cloudwatch  
- schedules  
- other criteria (for example programmatically)  
- manually using set desired capacity.  

scale out to meet demand and scale in to reduce cost. 

To configure Amazon EC2 Auto Scaling, you must first create a launch configuration, and then create an Auto Scaling group.  

Amazon EC2 Auto Scaling tracks the health state of instances and terminates instances that are marked unhealthy. In this way, you can help ensure that the instances that are part of the Auto Scaling group are all functioning properly.
By default, Amazon EC2 Auto Scaling uses EC2 instance status checks. If an Auto Scaling group is behind a load balancer, either the load balancer's instance checks or the EC2 instance checks are used for health monitoring.

## Exercise
Exercise 1
- Launch an EC2 instance with the following requirements:
    * Region: Frankfurt (eu-central-1)
    * AMI: Amazon Linux 2
    * Type: t3.micro
    * User data: see google drive  
    * Security Group: Allow HTTP
- Wait for the status checks to pass.
- Create an AMI from your instance with the following requirements:
- Image name: Web server AMI    

Exercise 2
- Create an application load balancer with the following requirements:
    * Name: LabELB
    * Listener: HTTP on port 80
    * AZs: eu-central-1a and eu-central-1b
    * Subnets: must be public
    * Security Group: 
        - Name: ELB SG
        - Rules: allow HTTP access
    * Target Group:
        - Name: LabTargetGroup
        - Targets: to be registered by Auto Scaling
  
Exercise 3
- Create a launch configuration for the Auto Scaling group. It has to be identical to the server that is currently running.
- Create an auto scaling group with the following requirements:
    * Name: Lab ASG
    * Launch Configuration: Web server launch configuration
    * Subnets: must be in eu-central-1a and eu-central-1b
    * Load Balancer: LabELB
    * Group metrics collection in CloudWatch must be enabled
    * Group Size:
        - Desired Capacity: 2
        - Minimum Capacity: 2
        - Maximum Capacity: 4
    * Scaling policy: Target tracking with a target of 60% average CPU utilisation


Exercise 4
- Verify that the EC2 instances are online and that they are part of the target group for the load balancer.
- Access the server via the ELB by using the DNS name of the ELB.
- Perform a load test on your server(s) using the website on your server to activate auto scaling. There might be a delay on the creation of new servers in your fleet, depending on the settings on your Auto Scaling Group.

### Sources
https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/tkv-create-ami-from-instance.html  

https://aws.amazon.com/elasticloadbalancing/?nc=sn&loc=0  

https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html  

https://docs.aws.amazon.com/autoscaling/ec2/userguide/get-started-with-ec2-auto-scaling.html  



### Overcome challenges


### Results  

exercise 1:  

![EC2 instance launched](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/4707ad1d13434e1fbf1b2775c26e822f62fa47fd/00_includes/AWS/ELB/ELB1%20ec2%20created.png)  
- EC2 instance launched and checks passed.  

![create image](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/4707ad1d13434e1fbf1b2775c26e822f62fa47fd/00_includes/AWS/ELB/ELB2%20step%20to%20create%20AMI.png)  
- How to create the AMI from the instance.  

![AMI created](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/4707ad1d13434e1fbf1b2775c26e822f62fa47fd/00_includes/AWS/ELB/ELB3%20AMI%20created.png)  
- AMI created.  

exercise 2:  

![create target group](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/4707ad1d13434e1fbf1b2775c26e822f62fa47fd/00_includes/AWS/ELB/ELB4%20targetgroup%20created.png)  
- first a target group is created.  

![ELB created](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/4707ad1d13434e1fbf1b2775c26e822f62fa47fd/00_includes/AWS/ELB/ELB5_ELB%20create.png)  
- The application load balancer created.  

![ELB active](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/4707ad1d13434e1fbf1b2775c26e822f62fa47fd/00_includes/AWS/ELB/ELB6%20ELB%20active.png)  
- The ELB is active.  

![launch template created](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/4707ad1d13434e1fbf1b2775c26e822f62fa47fd/00_includes/AWS/ELB/ELB7%20create%20launch%20template.png)  
- Launch template created.  

![ASG created](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/4707ad1d13434e1fbf1b2775c26e822f62fa47fd/00_includes/AWS/ELB/ELB8%20ASG%20created.png)  
- ASG created.  

![succesfull launch 2 instances](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/4707ad1d13434e1fbf1b2775c26e822f62fa47fd/00_includes/AWS/ELB/ELB9%20ASG%20succesfull%20launch%202%20ec2.png)  
- The ASG succesfully launched 2 instances.  

exercise 4:  

![instances created are healthy](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/4707ad1d13434e1fbf1b2775c26e822f62fa47fd/00_includes/AWS/ELB/ELB10%20healthy%20instances.png)  
- The created instances by ASG are healthy.  

![accessing server](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/4707ad1d13434e1fbf1b2775c26e822f62fa47fd/00_includes/AWS/ELB/ELB11%20dns%20server.png)  
- Accessing the server by using the link.  

![accessed server](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/4707ad1d13434e1fbf1b2775c26e822f62fa47fd/00_includes/AWS/ELB/ELB12%20elb%20server%20accessed.png)  
- Accessed the server.  

![load test server](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/4707ad1d13434e1fbf1b2775c26e822f62fa47fd/00_includes/AWS/ELB/ELB13%20load%20test%20server.png)  
- load test server.  

![new instance created by ASG](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/4707ad1d13434e1fbf1b2775c26e822f62fa47fd/00_includes/AWS/ELB/ELB14%20new%20instances%20created.png)  
- New instance is created by ASG.  

![result](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/4707ad1d13434e1fbf1b2775c26e822f62fa47fd/00_includes/AWS/ELB/ELB15%20result.png)  
- The ASG succesfully added the instance.  

