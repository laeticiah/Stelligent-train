aws cloudformation create-stack --stack-name elb --template-body file://7.1.1.yml --parameters file://params.json --profile temp

aws cloudformation create-stack --stack-name elb --template-body file://7.1.2.yml --parameters file://params.json --profile temp

*Generate Self-signed Certifcate*
openssl genrsa 2048 > my-private-key.pem
openssl req -new -x509 -nodes -sha256 -days 365 -key my-private-key.pem -outform PEM -out my-certificate.pem

*Upload to ACM*
aws acm import-certificate --certificate fileb://my-certificate.pem --private-key fileb://my-private-key.pem --profile temp

$ aws acm import-certificate --certificate fileb://Certificate.pem --certificate-chain fileb://CertificateChain.pem --private-key fileb://PrivateKey.pem

*My output*
{
    "CertificateArn": "arn:aws:acm:us-east-1:324320755747:certificate/391142ae-65ed-4f47-afe8-db115766ce28"
}

Used this ARN in `7.1.3.yml` line num `133`

aws cloudformation create-stack --stack-name elb --template-body file://7.1.3.yml --parameters file://params.json --profile temp

*CF Output*
https://test-Application-Load-Balancer-76418464.us-east-1.elb.amazonaws.com