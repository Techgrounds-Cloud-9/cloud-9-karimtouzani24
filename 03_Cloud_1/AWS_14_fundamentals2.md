ECS:  
• ECS is used for running Docker containers in the cloud  
• ECS containers are known as tasks  
• EC2 launch type:  
    - You managed EC2 instances which are the hosts for running the tasks  
• Fargate launch type:  
    - AWS manage the underlying compute, cluster, and scaling  
• Amazon Elastic Container Registry (ECR) is a private container image registry  

AWS support plans:  
Trusted Advisor:  
• Online resource that helps to reduce cost, increase performance and improve security by optimizing your AWS environment
• Provides real time guidance to help you provision your resources following best practices
• Advises you on Cost Optimization, Performance, Security, and Fault Tolerance  

AWS config:  
• Fully-managed service for compliance management
• Helps with compliance auditing, security analysis, resource change tracking and troubleshooting  

AWS cloud trail:  
• CloudTrail logs API activity for auditing
• By default, management events are logged and retained for 90 days
• A CloudTrail Trail logs any events to S3 for indefinite retention
• Trail can be within Region or all Regions
• CloudWatch Events can be triggered based on API calls in CloudTrail
• Events can be streamed to CloudWatch Logs  

IAM:  
• AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources
• You use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources
• Users are individual accounts you log in with
• Users have NO permissions by default
• Groups are used for organizing users and applying policies
• Policies are used for defining permissions
• Roles are used for delegating permissions and are assumed by services  
• Users log in to the AWS Management Console with a username and password
• Access keys are used for CLI/API access (programmatic)
• Access keys consist of an access key ID and secret access key
• The root user is the user that created the account
• Root users have full permissions and cannot be restricted
• Multi-factor authentication (MFA)uses a second factor in addition to a password – typically a code generated on a device  

IAM Best Practices:
• Lock away your AWS account root user access keys
• Create individual IAM users
• Use groups to assign permissions to IAM users
• Grant least privilege
• Get started using permissions with AWS managed policies
• Use customer managed policies instead of inline policies
• Use access levels to review IAM permissions
• Configure a strong password policy for your users
• Enable MFA  
• Use roles for applications that run on Amazon EC2 instances
• Use roles to delegate permissions
• Do not share access keys
• Rotate credentials regularly
• Remove unnecessary credentials
• Use policy conditions for extra security
• Monitor activity in your AWS account  

AWS Cloudwatch:  

DynamoDB:  
• Fully managed NoSQL database service
• Key/value store and document store
• It is a non-relational, key-value type of database
• Fully serverless service
• Push button scaling  

Charged for reading, writing, and storing data On-demand capacity mode
• Charged for reads and writes
• No need to specify how much capacity is required
• Good for unpredictable workloads
Provisioned capacity mode
• Specify number of reads and writes per second
• Can use Auto Scaling
• Good for predictable workloads
• Consistent traffic or gradual changes  

Lambda:  
• AWS Lambda executes code only when needed and scales automatically
• You pay only for the compute time you consume (you pay nothing when your code is not running)
• Benefits of AWS Lambda:
    - No servers to manage
    - Continuous scaling
    - Millisecond billing
    - Integrates with almost all other AWS services

billing:    
• Number of requests
• Duration of request – rounded up to the nearest millisecond
• Price is dependent on the amount of memory allocated to the function  

SNS:  
• Publisher / subscriber model
• Amazon SNS is used for building and integrating looselycoupled, distributed applications
• Provides instantaneous, push-based delivery (no polling)
• Uses simple APIs and easy integration with applications
• Offered under an inexpensive, pay-as-you-go model with no up-front costs  

SQS:  
• SQS offers a reliable, highly-scalable, hosted queue for storing messages in transit between computers
• SQS is used for distributed/decoupled applications
• SQS uses a message-oriented API
• SQS uses pull based (polling) not push based  

Event Bridge:  
• Serverless event bus
• Used for building event-driven architectures
• Ingests data and routes it to target AWS services