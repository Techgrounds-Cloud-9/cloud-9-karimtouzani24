# Subject
Simple Storage Service (S3)

## Key terminology
AWS offers object based storage in the form of S3. S3 makes use of buckets as a container for objects. A single object in S3 has a maximum size of 5TB. However, the total size of a bucket is virtually unlimited.  

We can connect to S3 with the browser and http protocol. An object consist of:  
- key (name of object)  
- version ID  
- value (actual data)  
- metadata  
- subresources  
- acces control info  

You can connect an instance to S3 ,over the internet using public addresses (vpc, internet gateway) or a private addresses (private connection, S3 gateway endpoint)

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
- S3 galcierf flexible retrieval, expedited (1-5min) standard (3-5 hours) bulk (5-12 hours). min storage duration 90 days  

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

you can store any type of file in S3. Files can max 5 TB. There is unlimited storage available. S3 name must be globally unique, but buckets are created in a region. Because of latency create physically closest.  

features:  
- tranfer acceleration  
- requester pays  
- events  
- static web hosting  
- versioning and replication


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
To make a bucket public accessable, I changed the block public acces option to off and you need to add a bucket policy. I used the policy generator with the following options: allow, a * to allow for everyone, the getobject action and the added a /* to the end of the arn so it works for everything in the bucket.  

To make a static website enable it in the properties tab of the bucket.

### Results  
exercise 1
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


exercise 2  
![new bucket and files uploaded](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/aa88271987786e21b84b326ee9f35ad6b705f9da/00_includes/AWS/S3/s3e2a.png)  
New bucket and files uploaded.  

![static website hosting enabled](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/aa88271987786e21b84b326ee9f35ad6b705f9da/00_includes/AWS/S3/s3e2b.png)  
In the bucket, go to the properties tab and enable static website hosting dwon the page. The homepage is also specified.  

![static website hosting enabled and website endpoint can be used.](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/aa88271987786e21b84b326ee9f35ad6b705f9da/00_includes/AWS/S3/s3e2c.png)  
Static website hosting enabled and website endpoint can be used.  

![result](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/aa88271987786e21b84b326ee9f35ad6b705f9da/00_includes/AWS/S3/results3e2.png)  
The website is accesible.





