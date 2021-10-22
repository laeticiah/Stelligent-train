---------------------Create session token------------------
-----------------------------------------------------------

aws sts get-session-token \
    --serial-number arn:aws:iam::324320755747:mfa/USERNAME \
    --token-code 123456` \
/

-------------Update Credentials file in .aws/-------------
----------------------------------------------------------

Temporary credentials will be generated

"Credentials": {
    "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
    "SessionToken": "AQoDYXdzEJr...<remainder of security token>",
    "Expiration": "2018-10-11T10:09:50Z",
    "AccessKeyId": "ASIAIOSFODNN7EXAMPLE",
  }
}

Use the temporary credentials to edit the credentials file
[temp]
output = json
region = us-east-1
aws_access_key_id = AKIAIOSFODNN7EXAMPLE
aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
aws_session_token = AQoDYXdzEJr...<remainder of security token>

--------------------Deploy the CFN Template----------------------
-----------------------------------------------------------------


wells3 % aws cloudformation deploy --template-file mats3.yaml --stack-name laeticias3buckmat --profile temp --region us-east-1

--------------Add template file and update the stack-------------
-----------------------------------------------------------------

aws cloudformation update-stack --template-body  file://mys3bucket.yaml --stack-name laeticiascftasky --parameters file://parameterfile.json --profile temp --region us-east-1


---------------------------Delete Stack--------------------------
-----------------------------------------------------------------

aws cloudformation delete-stack --stack-name laeticiascftasky


-------------Use AWS Vault to list buckets in region-------------
-----------------------------------------------------------------

aws cloudformation delete-stack --stack-name laeticiascftasky --profile temp --region us-east-1


