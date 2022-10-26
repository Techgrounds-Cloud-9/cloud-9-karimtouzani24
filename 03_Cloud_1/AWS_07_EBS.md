# Subject
Elastic Block Store (EBS)  

EBS can be seen as virtual hard drives in the cloud. They can be either root volumes (like an internal hard disk), or seperate volumes (like an external hard disk). One instance of an EBS is called a volume. One volume can usually only be attached to one EC2 instance at a time, although for every non-root volume, you can detach it and attach it to a different EC2 instance. EBS Multi-Attach is only available in specific cases.  

You can create snapshots of a volume to create backups or new identical volumes. These snapshots will be stored in S3.
There are four different volume types. Generally speaking, lower performance means lower cost, but newer generations or specialized hardware might give better performance for lower costs.  

For security, EBS volumes can be encrypted. Volumes can be scaled up, but not down.  

Any external device, including EBS, needs to be mounted if you want to use them in Linux

## Key terminology


## Exercise
Exercise 1
- Navigate to the EC2 menu.
- Create a t2.micro Amazon Linux 2 machine with all the default settings.
- Create a new EBS volume with the following requirements:
-  Volume type: General Purpose SSD (gp3)
-  Size: 1 GiB
-  Availability Zone: same as your EC2
- Wait for its state to be available.

Exercise 2
- Attach your new EBS volume to your EC2 instance.
- Connect to your EC2 instance using SSH.
- Mount the EBS volume on your instance.
- Create a text file and write it to the mounted EBS volume.

Exercise 3
- Create a snapshot of your EBS volume.
- Remove the text file from your original EBS volume.
- Create a new volume using your snapshot.
- Detach your original EBS volume.
- Attach the new volume to your EC2 and mount it.
- Find your text file on the new EBS volume.

### Sources
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html  

https://devopscube.com/mount-ebs-volume-ec2-instance/

### Overcome challenges
It was easy to make create an EC2 instance, EBS volume, snapshot. To attach and detach the volume and to connect to the SSH. By just following the steps on the console, see results.  

To only part i had to solve is how to mount a volume on the EC2 instance, I used a couple of command wich i found on the internet, see the sources and results. I did not have permissions to make a file. Only as root was allowed. So i changed to root user.  

### Results  
![instance created](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/fb77c7bd713b474c21e4866268a0db8356524326/00_includes/AWS/EBS/ebs_1%20instance%20created.png)  
Instance created with default settings.  

![new EBS volume](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/fb77c7bd713b474c21e4866268a0db8356524326/00_includes/AWS/EBS/ebs_2%20new%20ebs%20available.png)  
New EBS volume created in same Availablity zone and is available.  

![attaching the volume to the instance](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/fb77c7bd713b474c21e4866268a0db8356524326/00_includes/AWS/EBS/ebs_3%20attaching%20ebs.png)  
Attaching the volume to the EC2 instance.  

![attached volume](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/fb77c7bd713b474c21e4866268a0db8356524326/00_includes/AWS/EBS/ebs_4%20attached%20ebs.png)  
The new volume is attached.  

![ssh mount and file added](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/fb77c7bd713b474c21e4866268a0db8356524326/00_includes/AWS/EBS/ebs_5%20ssh%20mount%20and%20text.png)  
Connected with ssh, mounted the volume and added a text file.  

![snapshot created](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/fb77c7bd713b474c21e4866268a0db8356524326/00_includes/AWS/EBS/ebs_6%20snapshot.png)  
Snapshot created from the original EBS and after that the text file is deleted from the original EBS.  

![volume from snapshot](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/fb77c7bd713b474c21e4866268a0db8356524326/00_includes/AWS/EBS/ebs_7%20volume%20from%20snapshot.png)  
New volume created from volume.  

![detach original EBS and attach new EBS](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/fb77c7bd713b474c21e4866268a0db8356524326/00_includes/AWS/EBS/ebs_8%20detach%20and%20attach.png)  
The original EBS is detached and the EBS from snapshot is attached.  

![New EBS from snapshot mounted and file is shown](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/fb77c7bd713b474c21e4866268a0db8356524326/00_includes/AWS/EBS/ebs_9%20file%20new%20ebs.png)  
The new EBS from snapshot is mounted and the file is shown. The file was deleted on the original EBS after the snapshot was created. So that is why the file is shown.  


