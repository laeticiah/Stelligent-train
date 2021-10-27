aws cloudformation create-stack --stack-name iam-task --template-body file://iam3.1.1.yaml --capabilities CAPABILITY_IAM --profile temp --region us-east-1

aws cloudformation update-stack --stack-name iam-task --template-body file://iam3.1.2.yaml --capabilities CAPABILITY_NAMED_IAM --profile temp

aws cloudformation update-stack --stack-name iam-task --template-body file://iam3.1.3.yaml --capabilities CAPABILITY_NAMED_IAM --profile temp

aws cloudformation update-stack --stack-name iam-task --template-body file://iam3.1.4.yaml --capabilities CAPABILITY_NAMED_IAM --profile temp

aws cloudformation delete-stack --stack-name iam-task --profile temp