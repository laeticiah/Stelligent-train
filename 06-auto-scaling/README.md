# Topic 6: Auto Scaling
----------------------------------------------------------------------------------------------------
*Using Launch Template and CLI to Create Debian Instance*
```
aws cloudformation create-stack --stack-name asgtask --template-body file://1.1.yml --profile temp
```
----------------------------------------------------------------------------------------------------
*Using CLI to create a ASG*
```
aws autoscaling create-auto-scaling-group --auto-scaling-group-name asg-laeticia --instance-id i-0af13264d02be15d7 --min-size 1 --max-size 1 --desired-capacity 1
```
-----------------------------------------------------------------------------------------------------
*Creating Launch Configuration and ASG*
```
aws cloudformation create-stack --stack-name asgtask-1 --template-body file://1.2.yml --profile temp
```
------------------------------------------------------------------------------------------------------
*Changing instance size in Launch Configuration and Updating Stack*
```
aws cloudformation update-stack --stack-name asgtask-1 --template-body file://1.3.yml --profile temp --region us-east-1
```


-------------------------------------------------------------------------------------------------------
*Changing the Update policy in the ASG*
```
aws cloudformation update-stack --stack-name asgtask-1 --template-body file://1.4.yml --profile temp --region us-east-1
```
-------------------------------------------------------------------------------------------------------
*Switched out Launch Configuration for Launch Template*
```
aws cloudformation create-stack --stack-name asgtask-1 --template-body file://1.5.yml --profile temp --region us-east-1
```
-------------------------------------------------------------------------------------------------------
*To describe stack resources*

aws cloudformation describe-stacks --stack-name asgtask --profile temp

*Tear down stacks*
```
aws cloudformation delete-stack --stack-name asgtask --profile temp --region us-east-1

aws cloudformation delete-stack --stack-name asgtask-1 --profile temp --region us-east-1
```
--------------------------------------------------------------------------------------------------------
*Creating Launch Configuration and ASG*
```
aws cloudformation create-stack --stack-name asgtask-1 --template-body file://2.1.yml --profile temp
```

*List stack resources*
```
aws cloudformation describe-stack-resources --stack-name asgtask-1 --profile temp
```

*Query an Instance's Id From the Stack's Resource Description*
```
aws cloudformation describe-stack-resources --stack-name asgtask-1 --query "StackResources[?LogicalResourceId==`myASG`].PhysicalResourceId | [0]"

```
-----------------------------------------------------------------------------------------------------------
*Changed the max and desired number of instances and Updated the Stack*
```
aws cloudformation update-stack --stack-name asgtask-1 --template-body file://2.2.yml --profile temp --region us-east-1
```
------------------------------------------------------------------------------------------------------------
6.2.3

*Identify the instances in the stack*
aws autoscaling describe-auto-scaling-instances --profile temp --region us-east-1

*Manually make an instance unhealthy*

aws autoscaling set-instance-health --instance-ids <i-080a2bc5a72257833> --health-status Unhealthy --profile temp --region us-east-1

------------------------------------------------------------------------------------------------------------
6.2.4

*Manually put an instance on standby*
aws autoscaling enter-standby --instance-ids >i-05b4f7d5be44822a6> --auto-scaling-group-name my-asg --should-decrement-desired-capacity -- profile temp --region us-east-1

--------------------------------



