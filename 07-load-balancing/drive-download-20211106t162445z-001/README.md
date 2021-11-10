# Collect your subnet id from 3 region (us-east-1a, us-east-1b, us-east-1b)
# Also the VPC id.
# Paste it in params.json***

aws cloudformation create-stack --stack-name elb --template-body file://1.1.yml --parameters file://params.json

aws cloudformation create-stack --stack-name elb --template-body file://1.2.yml --parameters file://params.json

*Generate Self-signed Certifcate*
openssl genrsa 2048 > my-private-key.pem
openssl req -new -x509 -nodes -sha256 -days 365 -key my-private-key.pem -outform PEM -out my-certificate.pem

*Upload to ACM*
aws acm import-certificate --certificate fileb://my-certificate.pem --private-key fileb://my-private-key.pem

*You should get this output*
{
    "CertificateArn": "arn:aws:acm:us-east-1:218063557524:certificate/745f0691-af09-422c-9b45-00acc3e244d7"
}

Copy this ARN and paste in `1.3.yml` line num `123`

aws cloudformation create-stack --stack-name elb --template-body file://1.3.yml --parameters file://params.json