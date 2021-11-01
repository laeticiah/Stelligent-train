*Run python script for sts*
python3 edit_creds.py 
Then enter token code

----------------------------------------------------------------------------------------------------------
*Create stack that creates a VPC and Subnet by using the template and parameter files*

aws cloudformation create-stack --stack-name vpctask --template-body file://1.1.yml --parameters file://params.json --profile temp --region us-east-1

----------------------------------------------------------------------------------------------------------
*Update stack with new template that creates and attaches IGW to VPC; Creates Subnet RTB, adds IGW to it*

aws cloudformation update-stack --stack-name vpctask --template-body file://1.2.yml --parameters file://params.json --profile temp --region us-east-1

----------------------------------------------------------------------------------------------------------
*Create a ssh-key with name `myec2kp.pem`*
ssh-keygen -t rsa -m PEM

---------------------------------------------------------------------------------------------------------
*Move file to project directory*

cp ~/.ssh/myec2kp.pem ~/Documents/stelligenttrainingu/Stelligent-train/04-vpcs/myec2kp.pem

---------------------------------------------------------------------------------------------------------
*Update stack with template and parameter file that launches an EC2 instance*

 aws cloudformation create-stack --stack-name vpctask-1 --template-body file://1.4.yml --parameters file://params2.json --profile temp --region us-east-1

---------------------------------------------------------------------------------------------------------
*Update stack with template and parameter file that adds a SG*
aws cloudformation update-stack --stack-name vpctask-1 --template-body file://1.5.yml --parameters file://params2.json --profile temp --region us-east-1

---------------------------------------------------------------------------------------------------------
*Update stack with template that adds EIP*
aws cloudformation update-stack --stack-name vpctask-1 --template-body file://1.6.yml --parameters file://params2.json --profile temp --region us-east-1

---------------------------------------------------------------------------------------------------------
*Update stack with template that adds NAT Gateway*
aws cloudformation update-stack --stack-name vpctask-1 --template-body file://1.7.yml --parameters file://params2.json --profile temp --region us-east-1
