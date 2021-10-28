aws cloudformation create-stack --stack-name s3stack --template-body file://iam3.1.1.yaml --capabilities CAPABILITY_IAM

aws cloudformation update-stack --stack-name s3stack --template-body file://iam3.1.2.yaml --capabilities CAPABILITY_NAMED_IAM

aws cloudformation update-stack --stack-name 3stack --template-body file://iam3.1.3.yaml --capabilities CAPABILITY_NAMED_IAM

aws cloudformation update-stack --stack-name s3stack --template-body file://iam3.1.4.yaml --capabilities CAPABILITY_NAMED_IAM

aws cloudformation delete-stack --stack-name s3stack