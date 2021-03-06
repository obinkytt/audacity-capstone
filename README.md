# Audacity DevOps Capstone-Williams Obinkyereh

## Project Requiremnet

#### In this project you will apply the skills and knowledge which were developed throughout the Cloud DevOps Nanodegree program. These include:

Working in AWS
Using Jenkins to implement Continuous Integration and Continuous Deployment
Building pipelines
Working with Ansible and CloudFormation to deploy clusters
Building Kubernetes clusters
Building Docker containers in pipelines
As a capstone project, the directions are rather more open-ended than they were in the previous projects in the program. You will also be able to make some of your own choices in this capstone, for the type of deployment you implement, which services you will use, and the nature of the application you develop.

You will develop a CI/CD pipeline for micro services applications with either blue/green deployment or rolling deployment. You will also develop your Continuous Integration steps as you see fit, but must at least include typographical checking (aka “linting”). To make your project stand out, you may also choose to implement other checks such as security scanning, performance testing, integration testing, etc.!

Once you have completed your Continuous Integration you will set up Continuous Deployment, which will include:

Pushing the built Docker container(s) to the Docker repository (you can use AWS ECR, create your own custom Registry within your cluster, or another 3rd party Docker repository) ; and
Deploying these Docker container(s) to a small Kubernetes cluster. For your Kubernetes cluster you can either use AWS Kubernetes as a Service, or build your own Kubernetes cluster. To deploy your Kubernetes cluster, use either Ansible or Cloudformation. Preferably, run these from within Jenkins as an independent pipeline.

#### In the capstone project, each project is unique to the student. You’ll build a CI/CD pipeline for a microservices application for different deployment strategies. Students define the scope of the project and select the right deployment strategy based on different business requirements.


## Summary of my Project.

##### 1. I developed a python flask appliaction called webapp with python and HTML. The HTML is in Template folder
##### 2. I used AWS Cloud9 enviroment and Github to develop the application. Then I can push and pull and commits beteween AWS Cloud9 and Github repository
##### 3. I pushed the application to Docker for docker build and got a docker image.
##### 4. I used circleci for countinous testing  and continous intergration of my code and build.
##### 5. I pushed my docker image from docker container to Amazon Elastic Container Registry (Amazon ECR).
##### 6. I used cloudFormation to deploy my Appliaction immage in AWS ECR to Amazon Elastic Container Service (Amazon ECS).
##### 7. I also deployed my appliaclication image in AWS ECR to Amazon Elastic Kubernetes Service (Amazon EKS) using EKS Cluster and CloudFormation.

## Software, applications and eviroments used in this Project:
##### 1. AWS Cloud9
##### 2. Github Repository
##### 3. Github Desktop for Windows
##### 4. MacOS on Vmware WorkStation
##### 5. Docker and Kubernetes on macos
##### 6. Visual Studio Code for Windows
##### 7. Windows 10 Powershell
##### 8. circleci
##### 9. chocolatey (installation manager for Windows)
##### 10. Minikube
##### 11. Kubectl

## Amazon AWS Services used in this project:
##### AWS Account, AWS Identity and Access Management (IAM), AWS CLI.
##### AWS CloudFormation for building stacks for VPCs, EKS clusters, EKS Worker Nodes and AWS ECS container
##### AWS ECS, AWS ECR, AWS ECR and AWS cloud9

## --------------------About my Application-------------------------
#### This file contains information about the web application called webapp. The app is the webapp.py file. The application is a Python Flask Application that used an HTML file to display a community website I developed in WordPress. I developed this site for a Ghana Community and the community has about 100,000 users. The will app named web app run and call the index.html file which is in the template directory.

![Presentation1](https://user-images.githubusercontent.com/4149567/90983607-0cdc1a00-e535-11ea-8273-cc8e6d1fb3c2.jpg)

##  -----------------------The Project--------------------------------
### Preparing the project ernviroment
##### Login to Github and create a new repository (audacity-capstone )
##### I created the neceaasry folders and file. (See the Github Reposotory for folders and file created)
##### Login to AWS Management Console and start Cloud9 to prepare the coding enviroment.

### Command to get rsa key to connect cloud9 to Github Repository

#### $ ssh-keygen -t rsa
#### $ cat /home/ec2-user/.ssh/id_rsa.pub

![Cloud9-1](https://user-images.githubusercontent.com/4149567/90931329-12fdb980-e3c2-11ea-92aa-bc25b42a2484.jpg)

### Prepare pyhton virtual enviroment in AWS Cloud9
#### $ python3 -m venv capstone

### Activate virtual enviroment
#### $ source capstone/bin/activate

### I created the following file and folders: 
#### makefile, requirement.txt, Dockerfile, webapp.py, template/index.html, .circleci/config.yml, run_docker.sh, run_kubernetes.sh and readme.md

### I run my make install (This should be run from inside a virtualenv)
#### This will run pip install --upgrade pip &&\pip install -r requirements.txt and install all the necessary software for the application to run

### Command
#### $ make install


![makeinstall](https://user-images.githubusercontent.com/4149567/90936487-dd110300-e3ca-11ea-8ff6-768e9b781995.jpg)

### Testing my FLASK APP on port 5000
### Cammand:
#### $ export FLASK_APP=myapp.py
#### $ flask run


![app](https://user-images.githubusercontent.com/4149567/90939190-9faf7400-e3d0-11ea-8bd7-db1dbfeed0b6.jpg)

### Test Flask webapp in AWS cloud9 virtualenv 
### run commad: 
#### $ python webapp.py
#### Then go to AWS EC2 instance and edit security gruops inboud rules
#### Add port 8080 to all tracfic
#### copy EC2 port and paste it in a browser and add port 8080

![webapp](https://user-images.githubusercontent.com/4149567/90941473-dc329e00-e3d7-11ea-84f9-28aeb4ff8204.jpg)


### Test code with circleci using .circleci/config.yml

![CiecleC1 1](https://user-images.githubusercontent.com/4149567/90939873-80194b00-e3d2-11ea-942f-f89218ff279d.jpg)

### Test code with circleci using .circleci/config.yml

![CiecleC1 2](https://user-images.githubusercontent.com/4149567/90939952-bbb41500-e3d2-11ea-9e7a-e2ae7bc9f97d.jpg)


## I have tested my webapp and have tested my code with circleci. Time to do a Docker Build


### Docker Build using Dockerfile

### Command

#### $ docker build -t webapp .

#### Docker build succesfully

![ECR build](https://user-images.githubusercontent.com/4149567/90940793-ae4c5a00-e3d5-11ea-9f9c-e35498ff6b1a.jpg)

### List docker build

### Command

#### $ docker image ls


![Docker_image](https://user-images.githubusercontent.com/4149567/90942028-a42c5a80-e3d9-11ea-83c4-f23e85cf9031.jpg)

### Testing wbapp image docker 
### docker run -p 8000:5001 webapp.


![webapp](https://user-images.githubusercontent.com/4149567/90941473-dc329e00-e3d7-11ea-84f9-28aeb4ff8204.jpg)


## Now I will push docker build image to Elastic Container Registry (Amazon ECR)

### Creating ECR Repository

![ecr repo](https://user-images.githubusercontent.com/4149567/90946939-62aaa800-e3f7-11ea-89d5-9d0a1a1972d1.jpg)


### Click on the Respository name and then the view push command and go to the push command page


![ecr push comd](https://user-images.githubusercontent.com/4149567/90947145-21b39300-e3f9-11ea-8e22-0a2eba7336a2.jpg)

## Now followed the instructions to build ECR imgage from Docker Contianer

#### $ docker build -t udacity-capstone-image .

![ECR build](https://user-images.githubusercontent.com/4149567/90947308-68ee5380-e3fa-11ea-8c6d-436edbea8f95.jpg)

### Tag image to push

#### $ docker tag udacity-capstone-image:latest 073492515851.dkr.ecr.us-east-1.amazonaws.com/udacity-capstone-image:latest

### Push image to your newly created AWS repository

![image pust to ECR](https://user-images.githubusercontent.com/4149567/90947553-5543ec80-e3fc-11ea-9692-80a3b10a5c9c.jpg)

### Check and comfirm the image is build and push to AWS Repository


![image push2](https://user-images.githubusercontent.com/4149567/90947769-13b44100-e3fe-11ea-8a5f-040416d2c260.jpg)

## Application Deployment: With Rolling Deployment Using Amazon AWS ECS

### Time to deploy the application on ECS Cluster in Amazon AWS. I used Amazon AWS Managemnet Console

### Step 1: Register a task definition

### Stap 2 Create a cluster

![ECS Cluster](https://user-images.githubusercontent.com/4149567/90949705-ff793f80-e40f-11ea-9138-734f41a6896f.jpg)

## Cluster Resources


![Cluster Res](https://user-images.githubusercontent.com/4149567/90949790-21bf8d00-e411-11ea-95d6-f0f823b29f9e.jpg)


## Step 3: Create a Service in a cluster.
### This will use a cloudFormation to create Stacks, VPC, EC2 instances, Fargate and curity Groups 
### You can choose between AWS EC2 ond AWS Fargate to build the ECS cluster


![new cluaster services1](https://user-images.githubusercontent.com/4149567/90963208-992a0680-e47b-11ea-8818-57c89ef8dc0a.jpg)


### Step 4: Register a task definition and check the task is running


![ECS ser2](https://user-images.githubusercontent.com/4149567/90963123-e194f480-e47a-11ea-957f-c55577be460b.jpg)


## The task is runing to deploy Application

### This will take a while. About 10 to 20 munites. 


![new Task run](https://user-images.githubusercontent.com/4149567/90963314-37b66780-e47c-11ea-98f4-3bc1d44bc8a7.jpg)

## Check for the application deployment info which will specify the IP.
### Also check the security group of the instance and make sure the inboud rule is set to allow port 8080

![ecsportIP1](https://user-images.githubusercontent.com/4149567/90964124-63891b80-e483-11ea-8efe-fa66791a01b9.jpg)

## AWS ECS Deplymnet information

![Cluster deply](https://user-images.githubusercontent.com/4149567/90981790-a2bd7800-e528-11ea-803d-cadfd523c220.jpg)


## We can find the application deploymnet IP Address here

![ecsportIP2](https://user-images.githubusercontent.com/4149567/90964187-e5794480-e483-11ea-935c-64f379f81d52.jpg)


## Deployment IP Address canbe found here

![ecsportIP3](https://user-images.githubusercontent.com/4149567/90964455-620d2280-e486-11ea-83a7-cc7d65671189.jpg)


## Copy and paste IP Address and add port 8080 to access the Application.

## 54.165.145.123:8080 


![ecsport8080](https://user-images.githubusercontent.com/4149567/90964550-32aae580-e487-11ea-8487-d1a069844ba9.jpg)


## Post-deployment add testing of your application woth Circleci


![App post test](https://user-images.githubusercontent.com/4149567/90982305-f087af80-e52b-11ea-8398-00649be4eaa1.jpg)


## Circleci continous testing details and information


![App post test2](https://user-images.githubusercontent.com/4149567/90982364-570ccd80-e52c-11ea-94b2-89e3181eb5f9.jpg)



## Note: This ptoject attracted some Amazon AWS charges. 
## The Appliaction will be up for 2 days and I will delete all AWS intnaces and services after 2 days time.






































            


    

