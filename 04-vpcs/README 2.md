*change your username in params.json*

aws cloudformation create-stack --stack-name vpstask --template-body file://1.1.yml --parameters file://params.json --profile temp --region us-east-1

aws cloudformation update-stack --stack-name vpctask --template-body file://1.2.yml --parameters file://params.json --profile temp --region us-east-1

*create a ssh-key with name `myec2kp.pem`*
aws --region us-east-1 --profile temp ec2 create-key-pair --key-name myec2kp  --key-type rsa --output text > ~/.ssh/myec2kp.pem

move file to project directory

cp ~/.ssh/myec2kp.pem ~/Documents/stelligenttrainingu/Stelligent-train/04-vpcs/myec2kp.pem

 aws cloudformation create-stack --stack-name vpctask-1 --template-body file://1.4.yml --parameters file://params2.json --profile temp --region us-east-1

aws cloudformation update-stack --stack-name vpcstack-1 --template-body file://1.5.yml --parameters file://params2.json --profile temp --region us-east-1


aws cloudformation update-stack --stack-name ec2-1 --template-body file://1.6.yml --parameters file://params2.json

aws cloudformation update-stack --stack-name ec2-1 --template-body file://1.7yml --parameters file://params2.json
