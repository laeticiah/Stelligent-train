aws cloudformation create-stack --stack-name iam-test --template-body file://1.1.yml --capabilities CAPABILITY_IAM --profile temp --region us-east-1

aws cloudformation update-stack --stack-name iam-test --template-body file://1.2.yml --capabilities CAPABILITY_NAMED_IAM --profile temp --region us-east-1

aws cloudformation update-stack --stack-name iam-test --template-body file://1.3.yml --capabilities CAPABILITY_NAMED_IAM --profile temp --region us-east-1

aws cloudformation update-stack --stack-name iam-test --template-body file://1.4.yml --capabilities CAPABILITY_NAMED_IAM --profile temp --region us-east-1

aws cloudformation delete-stack --stack-name iam-test --profile temp --region us-east-1


aws cloudformation create-stack --stack-name iam-test --template-body file://2.1.yml --capabilities CAPABILITY_IAM --profile temp --region us-east-1

aws cloudformation update-stack --stack-name iam-test --template-body file://2.3.yml --capabilities CAPABILITY_IAM --profile temp --region us-east-1


aws cloudformation update-stack --stack-name iam-test --template-body file://3.1.yml --capabilities CAPABILITY_IAM --profile temp --region us-east-1

aws cloudformation update-stack --stack-name iam-test --template-body file://3.2.yml --capabilities CAPABILITY_IAM --profile temp --region us-east-1

aws cloudformation update-stack --stack-name iam-test --template-body file://3.3.yml --capabilities CAPABILITY_IAM --profile temp --region us-east-1

aws cloudformation delete-stack --stack-name iam-test --profile temp --region us-east-1