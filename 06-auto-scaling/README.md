# Topic 6: Auto Scaling
----------------------------------------------------------------------------------------------------
Lab 6.1.1
*Using Launch Template and CLI to Create Debian Instance*
```
aws cloudformation create-stack --stack-name asgtask --template-body file://1.1.yml --profile temp
```

*Using CLI to create a ASG*
```
aws autoscaling create-auto-scaling-group --auto-scaling-group-name asg-laeticia --instance-id i-0ba5f75451731fb01 --min-size 1 --max-size 1 --desired-capacity 1 --profile temp
```
-----------------------------------------------------------------------------------------------------
Lab 6.1.2
aws cloudformation update-stack --stack-name asgtask --template-body file://1.2.yml --profile temp --region us-east-1     

*Creating Launch Configuration and ASG*
```
aws cloudformation create-stack --stack-name asgtask-1 --template-body file://1.2.yml --profile temp
```
------------------------------------------------------------------------------------------------------
Lab 6.1.3
*Changing instance size in Launch Configuration and Updating Stack*
```
aws cloudformation update-stack --stack-name asgtask --template-body file://1.3.yml --profile temp --region us-east-1
```
-------------------------------------------------------------------------------------------------------
Lab 6.1.4
*Changing the Update policy in the ASG*
```
aws cloudformation update-stack --stack-name asgtask --template-body file://1.4-a.yml --profile temp
```
```
aws cloudformation update-stack --stack-name asgtask --template-body file://1.4-b.yml --profile temp
```
-------------------------------------------------------------------------------------------------------
Lab 6.1.5
*Switched out Launch Configuration for Launch Template*
```
aws cloudformation update-stack --stack-name asgtask --template-body file://1.5.yml --profile temp
```
-------------------------------------------------------------------------------------------------------
Lab 6.1.6
*Tear down stacks*
```
aws cloudformation delete-stack --stack-name asgtask --profile temp 
```
--------------------------------------------------------------------------------------------------------
Lab 6.2.1
*Creating Launch Configuration and ASG*

aws cloudformation create-stack --stack-name asgtask-1 --template-body file://2.1.yml --profile temp

*List stack resources*

aws cloudformation describe-stack-resources --stack-name asgtask-1 --profile temp

*Query an Instance's Id From the Stack's Resource Description*

aws cloudformation describe-stack-resources --stack-name asgtask-1 --logical-resource-id Debian --query StackResourceDetail.PhysicalResourceId --profile temp

-----------------------------------------------------------------------------------------------------------
Lab 6.2.2
*Changed the max and desired number of instances and Updated the Stack*

aws cloudformation update-stack --stack-name asgtask-1 --template-body file://2.2.yml --profile temp

------------------------------------------------------------------------------------------------------------
Lab 6.2.3
*Identify the instances in the stack*

aws autoscaling describe-auto-scaling-instances --profile temp

*Manually make an instance unhealthy*
```
aws autoscaling set-instance-health --instance-ids <i-080a2bc5a72257833> --health-status Unhealthy --profile temp
```
------------------------------------------------------------------------------------------------------------
Lab 6.2.4
*Manually put an instance on standby*

```
aws autoscaling enter-standby --instance-ids >i-05b4f7d5be44822a6> --auto-scaling-group-name my-asg --should-decrement-desired-capacity -- profile temp
```
------------------------------------------------------------------------------------------------------------
Lab 6.3.1
*Simple Scale-Out - Add a Cloudwatch Alarm and associate it with your ASG*
```
aws cloudformation update-stack --stack-name asgtask-1 --template-body file://3.1.yml --profile temp
```

*SSH into instance and add stress*
```
sudo apt update
```
```
sudo apt-get install stress
```
```
stress --cpu 200 --timeout 120
```

---------------------------------------------------------------------------------------------------------
Lab 6.3.2
*Simple Scale-In*
```
aws cloudformation update-stack --stack-name asgtask-1 --template-body file://3.2.yml --profile temp
```
----------------------------------------------------------------------------------------------------------
Lab 6.3.3
*Target tracking policy*

```
aws cloudformation update-stack --stack-name asgtask-1 --template-body file://3.3-a.yml --profile temp
```
```
aws cloudformation update-stack --stack-name asgtask-1 --template-body file://3.3-b.yml --profile temp
```

-----------------------------------------------------------------------------------------------------------
*Target Tracking Scale-In

```
aws cloudformation update-stack --stack-name asgtask-1 --template-body file://3.3-b.yml --profile temp
```