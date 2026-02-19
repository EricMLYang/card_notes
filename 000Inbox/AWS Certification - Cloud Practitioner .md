---
tags:
  - aws
---
# AWS Certification - Cloud Practitioner 




| **Category** | **Foundational** | 
|---|---|
| Exam duration | 90 minutes | 
| Exam format | 65 questions; either multiple choice or multiple response | 
| Cost | 100 USD.**1** Visit [Exam pricing](https://www.google.com/search?q=https%3C1%3E://aws.amazon.com/certification/pricing/) for additional cost information, including foreign exchange rates | 
| Test in-person or online | Pearson VUE testing center or online proctored exam | 

### Basics of the Cloud Adoption Framework (CAF)

![CleanShot 2024-12-07 at 07.33.20@2x.png](./AWS%20Certification%20-%20Cloud%20Practitioner%20-assets/CleanShot%202024-12-07%20at%2007.33.20@2x.png)



### The Shared Responsibility Model

- AWS's Responsibility

   - Facility Management

   - Personnel Management

   - Physical Security of the Datacenter

   - Separating compute assets and network traffic so that even on shared hardware, nocustomers' data ever crosses lines

   - Accurately enforcing those rules which you do specify

- Your Responsibility

   - Accurately specifying the rules you wish to be enforced

   - Patching the operating systems and software of servers you run

   - Protecting and safeguarding customer data



### AWS Artifact

- AWS Artifact is a self-service portal for accessing AWS compliance reports and agreements. It's not a computing service, but rather a documentation and compliance resource.

- Encryption

   - At-Rest Encryption

   - At-Rest Encryption

- Observability

   - Cloudwatch

   - CloudTrail vs. Cloudwatch

      - Cloud Trail logs all configuration changes to AWS resources along with the lAM information of who took the operation.

         Cloud Trail needs to be enabled, unlike CloudWatch, which collects logs by default

         CloudWatch would log what happens ON your server; Cloud Trail would log what happens TO your server.

- AWS Config

   - AWS Config stores historical data about server configurations and can go back in time to see what a server looked like on a given day.

   - It can also track compliance across servers.

- IAM

   - IAMUsers

      - Can log in

      - Can have console passwords

      - Can have programmatic API access keys

      - Can have policies attached directly

      - Can belong to groups

      - Can assume roles

   - IAM Groups

   - IAM Role

      - SUPERCEDE user and group policies

      - You become acting "as" the role for as long as it's assumed

      - Preferred in complex setups and for Organizations

      - Can be directly attached to servers and services

         - "This EC2 has the right to upload images to S3"

         - "This CodePipeline has the right to deploy CloudFormations"



## \[ EC2 \]

- Elastic Cloud Compute (EC2) is the most important AWS service.

- EC2 creates virtual servers with AMIs (Amazon Machine Images) and allocates them computing resources.

-  AMI represents a blueprint for creating a virtual machine (EC2 instance) in the AWS cloud. Here are key details about AMI:

- You can do virtually anything with an EC2. By installing specific software on it, you can make it into any kind of server.

- Remember that if AWS offers "Thing As A Service", it is more correct to use that specific service than to recreate the service by building from the ground up on an EC2.