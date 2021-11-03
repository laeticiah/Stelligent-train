-----------------------------------------------------------------------------------------------
*Create Launch Template using CLI*
aws cloudformation create-stack --stack-name ec2 --template-body file://1.2-a.yml --profile temp --region us-east-1

-----------------------------------------------------------------------------------------------
*Using Launch Template and CLI to Create Instances*
aws cloudformation update-stack --stack-name ec2 --template-body file://1.2.yml --profile temp --region us-east-1

-----------------------------------------------------------------------------------------------
*Update the windows launch template ami*
aws cloudformation update-stack --stack-name ec2 --template-body file://1.2.yml --profile temp --region us-east-1

**Updated file to use Version 2 of the launch template after changing the ami**

aws cloudformation update-stack --stack-name ec2 --template-body file://1.3.yml --profile temp --region us-east-1

-----------------------------------------------------------------------------------------------
*To describe stack resources*

aws cloudformation describe-stacks --stack-name ec2 --profile temp --region us-east-1

-----------------------------------------------------------------------------------------------

*To get state and metadata of the instance*

aws ec2 describe-instances --instance-ids <instanceid> --profile temp --region us-east-1

-----------------------------------------------------------------------------------------------
*To describe stack events*

aws cloudformation describe-stack-events --stack-name ec2 --profile temp --region us-east-1

-----------------------------------------------------------------------------------------------
aws cloudformation delete-stack --stack-name ec2 --profile temp --region us-east-1

after delete the stack, check the instance status. It Should `Terminate`


*********************************

aws cloudformation create-stack --stack-name ec2 --template-body file://2.1-a.yml --profile temp --region us-east-1

aws cloudformation update-stack --stack-name ec2 --template-body file://2.1-b.yml --profile temp --region us-east-1

aws cloudformation update-stack --stack-name ec2 --template-body file://2.2-a.yml --profile temp --region us-east-1

aws cloudformation update-stack --stack-name ec2 --template-body file://2.2-b.yml --profile temp --region us-east-1

*********************************

