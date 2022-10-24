# Subject
AWS Global Infrastructure  

## Key terminology
In the cloud, everything from servers to networking is virtualized. As an AWS customer, you don’t have to worry about the underlying physical infrastructure. That being said, the physical location of an application in the cloud can be important.  

AWS has a global infrastructure made up of the following components:  

- Regions  
- Availability Zones  
- Local zone 
- Edge Locations  

As a customer, you have different amounts of control over where your stuff is located depending on the service you use.
For example, IAM is a global service, so you get no control over where its information is stored. In contrast, you can select specific Availability Zones for RDS instances.  

When you launch an instance, select a Region that puts your instances closer to specific customers, or meets the legal or other requirements that you have. By launching your instances in separate Availability Zones, you can protect your applications from the failure of a single location  

What is Cache?  
Caching helps the software to deliver content faster and cheaper. Cache is fast storage that copies and stores parts of data. The data is stored in hardware that can deliver content fast, for example, RAM (Random-access memory). The main job of the cache is to deliver content fast. The data is saved in the fast hardware layer so that it does not have to use the slow storage hardware.


## Exercise  
What is an AWS Availability Zone? 
- multiple, isolated locations within each Region.  
- The code for Availability Zone is its Region code followed by a letter identifier. For example, us-east-1a.  
- When you launch an instance, you select a Region and a virtual private cloud (VPC), and then you can either select a subnet from one of the Availability Zones or let us choose one for you.  
- Availability Zone us-east-1a for your AWS account might not be the same physical location as us-east-1a for another AWS account. To coordinate Availability Zones across accounts, you must use the AZ ID, which is a unique and consistent identifier for an Availability Zone. For example, use1-az1 is an AZ ID for the us-east-1 Region and it has the same physical location in every AWS account.  
- Each AZ has independent power, cooling, and physical security and is connected via redundant, ultra-low-latency networks. AWS customers focused on high availability can design their applications to run in multiple AZs to achieve even greater fault-tolerance. 


What is a Region?  
- A separate geographic area.  
- Is a physical location around the world where we cluster data centers. We call each group of logical data centers an Availability Zone.
- Each Region is designed to be isolated from the other Regions. This achieves the greatest possible fault tolerance and stability.
- Some AWS resources might not be available in all Regions. Ensure that you can create the resources that you need in the desired Regions before you launch an instance.

What is an Edge Location?  
- A site that CloudFront uses to cache copies of your content for faster delivery to users at any location.  
- Data Center used to deliver content fast to your users. It is the site that is nearest your users.  
- The content is delivered faster because the data is no longer requested from the primary location. It is delivered from the Edge Location. The location nearest to the user.  

A Local Zone  
- is an extension of an AWS Region in geographic proximity to your users. Local Zones have their own connections to the internet and support AWS Direct Connect, so that resources created in a Local Zone can serve local users with low-latency communications.  
- The code for a Local Zone is its Region code followed by an identifier that indicates its physical location. For example, us-west-2-lax-1 in Los Angeles.

Why would you choose one region over another? (e.g. eu-central-1 (Frankfurt) over us-west-2 (Oregon))?  

There are four main factors that play into evaluating each AWS Region for a workload deployment:  
- Compliance. If your workload contains data that is bound by local regulations, then selecting the Region that complies with the regulation overrides other evaluation factors. This applies to workloads that are bound by data residency laws where choosing an AWS Region located in that country is mandatory.  

- Latency. A major factor to consider for user experience is latency. Reduced network latency can make substantial impact on enhancing the user experience. Choosing an AWS Region with close proximity to your user base location can achieve lower network latency. It can also increase communication quality, given that network packets have fewer exchange points to travel through.  

- Cost. AWS services are priced differently from one Region to another. Some Regions have lower cost than others, which can result in a cost reduction for the same deployment.  

- Services and features. Newer services and features are deployed to Regions gradually. Although all AWS Regions have the same service level agreement (SLA), some larger Regions are usually first to offer newer services, features, and software releases. Smaller Regions may not get these services or features in time for you to use them to support your workload.


### Sources
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-availability-zones  

https://www.w3schools.com/aws/aws_cloudessentials_awsedgelocations.php  

https://aws.amazon.com/about-aws/global-infrastructure/regions_az/  

https://aws.amazon.com/blogs/architecture/what-to-consider-when-selecting-a-region-for-your-workloads/

