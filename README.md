# Audacity DevOps Capstone -Williams Obinkyereh

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
##### 2. I used WAS Cloud9 enviroment and Github to develop the application. The was a push and pull and commits beteween AWS Cloud9 and Github repository
##### 3. I pushed the appliaction to Docker for a docker for docker build to obtain a docker image.
##### 4. I used circleci for countinous testing  and continues intergration of my code and build.
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

##           The Project
             ___________


    

