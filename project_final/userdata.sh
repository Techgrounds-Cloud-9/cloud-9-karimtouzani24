#!/bin/bash

sudo yum update -y
sudo yum install -y httpd 
sudo systemctl start httpd
sudo systemctl enable httpd

sudo echo "<h1> Hello world, this is the website to test if it's working</h1>" > /var/www/html/index.html