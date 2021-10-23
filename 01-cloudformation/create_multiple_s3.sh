for reg in us-east-1 us-east-2 us-west-1 us-west-2
do
aws cloudformation create-stack --stack-name iam-3 --template-body file://cloudformation1.3.1.yaml --parameters file://parameter3.json --region $reg
done