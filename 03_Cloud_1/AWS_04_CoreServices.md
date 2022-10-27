# Subject
Core Services

## Key terminology
This document should be used as a sort of guide to your AWS Cloud Practitioner certification. It highlights the services that you should know in more detail, and describes how to deal with the other services that might appear in the (practice) exam.  

There are a lot of services in AWS, but some are more important than others. AWS lists the following key services that you should have some in-depth knowledge about for the Cloud Practitioner exam:  

- Amazon EC2  
- AWS Lambda  
- AWS Elastic Beanstalk
- Amazon VPC
- Amazon Route 53
- Amazon S3
- Amazon S3 Glacier
- Amazon CloudFront
- Amazon RDS
- Amazon DynamoDB
- Amazon CloudWatch
- Amazon CloudFormation
- AWS Identity and Access Management  

Of course, there’s many more services that might appear on your exam. For those, it is usually enough to just learn the product page you can find online (click here for an example of an AWS product page https://aws.amazon.com/codestar/).  

Besides the different services, you can also expect questions on cloud concepts, like the Well-Architected Framework or the cloud pricing model, as well as questions on the different support categories.

## Exercise  
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

- AWS Lambda  
Is a type of serverless service which is a compute service which enables us to run code. You can run code without provisioning or managing servers. You pay only for the compute time that you consume—there's no charge when your code isn't running. You can run code for virtually any type of application or backend service—all with zero administration. Just upload your code and Lambda takes care of everything required to run and scale your code with high availability. You can set up your code to automatically trigger from other AWS services or call it directly from any web or mobile app.  

an event is the trigger: this can be the cli, api or sdk. then lambda code gets executed.  

used cases: data processing, real time file processing, real time stream processing, build serverless backends for web mobile iot and 3rd party api requests.  

- AWS Elastic Beanstalk  
you can quickly deploy and manage applications in the AWS Cloud without worrying about the infrastructure that runs those applications. AWS Elastic Beanstalk reduces management complexity without restricting choice or control. You simply upload your application, and AWS Elastic Beanstalk automatically handles the details of capacity provisioning, load balancing, scaling, and application health monitoring.  

- Amazon VPC  
Enables you to launch AWS resources into a virtual network that you've defined. This virtual network closely resembles a traditional network that you'd operate in your own data center, with the benefits of using the scalable infrastructure of AWS..  

- Amazon Route 53  
Amazon Route 53 is a highly available and scalable Domain Name System (DNS) web service. You can use Route 53 to perform three main functions in any combination: domain registration, DNS routing, and health checking.  

DNS resolves an ip addresses.

- Amazon S3  
serverless service. Is an object storage service that offers industry-leading scalability, data availability, security, and performance. Customers of all sizes and industries can use Amazon S3 to store and protect any amount of data for a range of use cases, such as data lakes, websites, mobile applications, backup and restore, archive, enterprise applications, IoT devices, and big data analytics. Amazon S3 provides management features so that you can optimize, organize, and configure access to your data to meet your specific business, organizational, and compliance requirements.  

- Amazon S3 Glacier  
Amazon S3 Glacier (S3 Glacier) is a secure and durable service for low-cost data archiving and long-term backup.  

- Amazon CloudFront  
Amazon CloudFront is a web service that speeds up distribution of your static and dynamic web content, such as .html, .css, .js, and image files, to your users. CloudFront delivers your content through a worldwide network of data centers called edge locations. When a user requests content that you're serving with CloudFront, the request is routed to the edge location that provides the lowest latency (time delay), so that content is delivered with the best possible performance.  

- Amazon RDS  
Amazon Relational Database Service (Amazon RDS) is a web service that makes it easier to set up, operate, and scale a relational database in the AWS Cloud. It provides cost-efficient, resizable capacity for an industry-standard relational database and manages common database administration tasks.  

- Amazon DynamoDB  
serverless service. A fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. You can use Amazon DynamoDB to create a database table that can store and retrieve any amount of data, and serve any level of request traffic. Amazon DynamoDB automatically spreads the data and traffic for the table over a sufficient number of servers to handle the request capacity specified by the customer and the amount of data stored, while maintaining consistent and fast performance.  

- Amazon CloudWatch  
Amazon CloudWatch is a performance monitoring service, it provides a reliable, scalable, and flexible monitoring solution that you can start using within minutes. You no longer need to set up, manage, and scale your own monitoring systems and infrastructure.  

- Amazon CloudFormation  
Enables you to create and provision AWS infrastructure deployments predictably and repeatedly. It helps you leverage AWS products such as Amazon EC2, Amazon Elastic Block Store, Amazon SNS, Elastic Load Balancing, and Auto Scaling to build highly reliable, highly scalable, cost-effective applications in the cloud without worrying about creating and configuring the underlying AWS infrastructure. AWS CloudFormation enables you to use a template file to create and delete a collection of resources together as a single unit (a stack).  

- AWS Identity and Access Management  
AWS Identity and Access Management (IAM) is a web service for securely controlling access to AWS services. With IAM, you can centrally manage users, security credentials such as access keys, and permissions that control which AWS resources users and applications can access.

### Sources
https://d1.awsstatic.com/training-and-certification/docs-cloud-practitioner/AWS-Certified-Cloud-Practitioner_Exam-Guide.pdf  

https://docs.aws.amazon.com/

