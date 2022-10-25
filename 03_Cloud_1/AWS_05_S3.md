# Subject
Simple Storage Service (S3)

## Key terminology
AWS offers object based storage in the form of S3. S3 makes use of buckets as a container for objects. A single object in S3 has a maximum size of 5TB. However, the total size of a bucket is virtually unlimited.  

Bucket names must be globally unique. That is, even other AWS accounts in different regions cannot share the same bucket name. Buckets, and objects within buckets, can be accessed using a URL  

The bucket policy acts as an access control list. Data can be encrypted for even further protection.  

Objects are automatically replicated within a region, so that there’s always at least three copies available. This redundancy greatly increases the availability and durability of objects stored in S3.  

There are 4 storage classes:
- S3 Standard
- S3 Standard-IA
- S3 One-zone IA
- S3 Glacier  

There’s also S3 Glacier Deep archive, a subclass of S3 Glacier. And Intelligent Tiering which is more a cost optimization tool than a class on its own.
Storage classes differ in availability, durability, retrieval time, and cost.  

storage classes more info:  
- S3 standard - General Purpose (for frequent accessed data, big data analytics, mobile and gaming applications, content distribution)  
- S3 standard-IA - Infrequent Access (data less frequent accessed but requires rapid acces, lower cost than s3 standard, used for DR and backups) 

- S3 One-Zone-IA - Infrequent access (in a singel AZ, data is lost when Az is destroyed, used for secundary backups or data you can recreate)  

the glacier storage classes are low cost object storage meant for archiving or backup, price for storage + object retrieval cost.  
- S3 glacier instant retrieval, milisecond retrieval, great for data accessed once a quater.  min storage duration 90 days
- S3 galcierf lexible retrieval, expedited (1-5min) standard (3-5 hours) bulk (5-12 hours). min storage duration 90 days  

- S3 glacier deep archive, for long term storage. standard (12 hours retrieval) bulk (48 hours) min storage duration 180 days 

- S3 intelligent tiering  
small monthly monitoring and auto-tiering fee. moves objects automatically between acces tiers based on usage. there are no tetrieval charges in s3 intelligent-tiering. Frequent, Infrequent, and Archive Instant Access tiers.  

Can move between classes manually or using S3 lifecycle configurations.

In S3, you pay for:
- GBs storage per month
- Transfer OUT to out of the region
- PUT, COPY, POST, LIST, and GET requests  

You don’t pay for:
- Transfer IN to Amazon S3
- Transfer OUT from S3 to CloudFront or EC2 in the same region

Besides storing data for all kinds of purposes (big data, storing videos, archiving, etc.), S3 has another use case: hosting static websites.  

durability vs availability:  
- durability is how many times a object is lost and availability is how readily available a service is. 


## Exercise  
Requirements
- Your AWS environment
- A cat picture (jpg or png)
- AWS’ demo website (index.html, script.js, style.css; can be found in the Google Drive)
- A peer


Exercise 1
- Create new S3 bucket with the following requirements: Region: Frankfurt (eu-central-1)
- Upload a cat picture to your bucket.
- Share the object URL of your cat picture with a peer. Make sure they are able to see the picture.  

Exercise 2
- Create new bucket with the following requirements: Region: Frankfurt (eu-central-1)  
- Upload the four files that make up AWS’ demo website.
- Enable static website hosting.
- Share the bucket website endpoint with a peer. Make sure they are able to see the website.



### Sources
https://aws.amazon.com/s3/storage-classes/

### Overcome challenges


### Results  
![bucket created](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/2c1d567e794ece8676871c655671c454ab8707aa/00_includes/AWS/S3/s3e1.png)  
The bucket is created in the Frankfurt region. It is not public yet.  

![image uploaded](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/2c1d567e794ece8676871c655671c454ab8707aa/00_includes/AWS/S3/s3e1b.png)  
A cat image is uploaded to the bucket.  

![no public acces](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/2c1d567e794ece8676871c655671c454ab8707aa/00_includes/AWS/S3/s3e1c.png)  
No public acces. Permissions need to be edited.  

![edit public acces and policy generated](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/2c1d567e794ece8676871c655671c454ab8707aa/00_includes/AWS/S3/s3e1d.png)  
Block public access is turned off and a bucket policy is generated.  

![publc acces bucket](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/2c1d567e794ece8676871c655671c454ab8707aa/00_includes/AWS/S3/s3e1e.png)  
The bucket is publicly accessible.  

![link to publicly access file](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/2c1d567e794ece8676871c655671c454ab8707aa/00_includes/AWS/S3/s3e1f.png)  
The link to access publicly is send to a peer.  

![result peer](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/2c1d567e794ece8676871c655671c454ab8707aa/00_includes/AWS/S3/results3e1.png)  
The peer is able to view the image.

