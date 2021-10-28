<!-- mkdir data
cd data
touch airport.cs
touch mytestfile1.txt
aws s3 mb s3://stelligent-u-laeticia.harper/ --profile temp --region us-west-2 
aws s3 ls s3://stelligent-u-laeticia.harper --profile temp
touch private.txt
aws s3 sync . s3://stelligent-u-laeticia.harper/ --exclude private.txt --profile temp
aws s3 ls s3://stelligent-u-laeticia.harper --profile temp
aws s3 rm  s3://stelligent-u-laeticia.harper/airport.cs --profile temp
aws s3 rm  s3://stelligent-u-laeticia.harper/mytestfile1.txt --profile temp
aws s3 rb s3://stelligent-u-laeticia.harper --profile temp
aws s3 mb s3://stelligent-u-laeticia.harper/ --profile temp --region us-west-2
aws s3 sync . s3://stelligent-u-laeticia.harper/ --profile temp
aws s3 sync . s3://stelligent-u-laeticia.harper/ --profile temp --acl public-read
aws s3 cp s3://stelligent-u-laeticia.harper/data/private.txt . --profile temp
aws s3 sync . s3://stelligent-u-laeticia.harper/data/private.txt --profile temp --acl bucket-owner-read
aws s3api delete-objects --bucket stelligent-u-laeticia.harper --delete file://delete.json --profile temp
aws s3 rb --force s3://stelligent-u-laeticia.harper --profile temp
aws cloudformation create-stack --template-body file://data/cloudformation2.2.4.yaml --stack-name s3taskstack2 --profile temp --region us-west-2
aws s3 sync . s3://stelligent-u-laeticia.harper/ --profile temp
aws cloudformation update-stack --template-body file://data/cloudformation2.2.4.yaml --stack-name s3taskstack2 --profile temp --region us-west-2 --capabilities CAPABILITY_NAMED_IAM

aws cloudformation create-stack --template-body file://data/cloudformation2.3.1.yaml --stack-name s3taskstack3 --profile temp --region us-west-2
aws s3api put-bucket-versioning --bucket stelli-u-laeticia.harper --versioning-configuration status=Enabled --profile temp --region us-west-2
vi private.txt
aws s3 sync . s3://stelli-u-laeticia.harper/ --profile temp
aws s3 ls s3://stelli-u-laeticia.harper --profile temp --region us-west-2
aws s3api get-object --bucket stelli-u-laeticia.harper --key private.txt --version-id RFINNeITVA2aWApUldlbllfANqAZdTfL --profile temp --region us-west-2 outfile
aws s3api delete-object --bucket stelli-u-laeticia.harper --key private.txt --version-id RFINNeITVA2aWApUldlbllfANqAZdTfL --profile temp --region us-west-2 
aws s3api put-bucket-tagging --bucket stelli-u-laeticia.harper --tagging 'TagSet=[{Key=dept,Value=development},{Key=aws:cloudformation:stack-id,Value=arn:aws:cloudformation:us-west-2:324320755747:stack/s3taskstack3/98065480-3609-11ec-bb27-06e121f4f885},{Key=aws:cloudformation:stack-name,Value=s3taskstack3},{Key=aws:cloudformation:logical-id,Value=S3Bucket}]' --profile temp --region us-west-2 -->
