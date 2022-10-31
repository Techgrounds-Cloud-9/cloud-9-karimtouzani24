# Subject
Shared Responsibility Model  

The Shared Responsibility Model describes who is responsible for the security of what part of the cloud.  
In general, you can say that AWS is responsible for security of the cloud, while the customer is responsible for security in the cloud.  
AWS is always responsible for securing the physical infrastructure, while the customer is always responsible for encrypting customer data.


## Key terminology  

The AWS shared responsibility model defines customer/AWS responsibilities:  
• AWS are responsible for “Security of the Cloud”  
- AWS is responsible for protecting the infrastructure that runs all of the services offered in the AWS Cloud
- This infrastructure is composed of the hardware, software, networking, and facilities that run AWS Cloud services
• Customers are responsible for “Security in the Cloud”  
- For EC2 this includes network level security, operating systempatches and updates, IAM user access management, and client and server-side data encryption  

Customers should carefully consider the services they choose as their responsibilities vary depending on the services used, the integration of those services into their IT environment, and applicable laws and regulations. The nature of this shared responsibility also provides the flexibility and customer control that permits the deployment.  

AWS responsibility “Security of the Cloud” 
- AWS is responsible for protecting the infrastructure that runs all of the services offered in the AWS Cloud. This infrastructure is composed of the hardware, software, networking, and facilities that run AWS Cloud services.  

Customer responsibility “Security in the Cloud”  

- Customer responsibility will be determined by the AWS Cloud services that a customer selects. This determines the amount of configuration work the customer must perform as part of their security responsibilities.  
- For example: 

A service such as Amazon Elastic Compute Cloud (Amazon EC2) is categorized as Infrastructure as a Service (IaaS) and, as such, requires the customer to perform all of the necessary security configuration and management tasks.
Customers that deploy an Amazon EC2 instance are responsible for management of the guest operating system (including updates and security patches), any application software or utilities installed by the customer on the instances, and the configuration of the AWS-provided firewall (called a security group) on each instance.  

Amazon S3 and Amazon DynamoDB, AWS operates the infrastructure layer, the operating system, and platforms, and customers access the endpoints to store and retrieve data. Customers are responsible for managing their data (including encryption options), classifying their assets, and using IAM tools to apply the appropriate permissions.  

Inherited Controls – Controls which a customer fully inherits from AWS.

Physical and Environmental controls
Shared Controls – Controls which apply to both the infrastructure layer and customer layers, but in completely separate contexts or perspectives. In a shared control, AWS provides the requirements for the infrastructure and the customer must provide their own control implementation within their use of AWS services. Examples include:

Patch Management – AWS is responsible for patching and fixing flaws within the infrastructure, but customers are responsible for patching their guest OS and applications.
Configuration Management – AWS maintains the configuration of its infrastructure devices, but a customer is responsible for configuring their own guest operating systems, databases, and applications.
Awareness & Training - AWS trains AWS employees, but a customer must train their own employees.
Customer Specific – Controls which are solely the responsibility of the customer based on the application they are deploying within AWS services. Examples include:

Service and Communications Protection or Zone Security which may require a customer to route or zone data within specific security environments.

Once a customer understands the AWS Shared Responsibility Model and how it generally applies to operating in the cloud, they must determine how it applies to their use case. Customer responsibility varies based on many factors, including the AWS services and Regions they choose, the integration of those services into their IT environment, and the laws and regulations applicable to their organization and workload.

## Exercise
Study The AWS Shared Responsibility Model  

### Sources
https://aws.amazon.com/compliance/shared-responsibility-model/

### Results  
![SRM](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/b8c4d969608a6fbf7d76d196574170919db45307/00_includes/AWS/SRM/SRM.png)  
