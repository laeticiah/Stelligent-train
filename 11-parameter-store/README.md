*Create stack with parameters*
```
aws cloudformation create-stack --stack-name LHssm --template-body file://1.1.yml --parameters file://params.json --profile temp
```

*********************************************************************************************************
*Get Parameters*

```
python3 1.2.getparams.py
```

```
aws ssm get-parameter --name /laeticia/stelligent-u/lab11/engineer/Laeticia/title --profile temp
```

```
aws ssm get-parameters --names /laeticia/stelligent-u/lab11/engineer/Laeticia/name /laeticia/stelligent-u/lab11/engineer/Laeticia/title --profile temp
```

 ```   
aws ssm get-parameters-by-path --path /laeticia/stelligent-u/lab11/engineer --recursive --profile temp
```
*********************************************************************************************************
*Create a web EC2 stack with the parameters from 1.1 listed on the webpage*

```
aws cloudformation create-stack --stack-name LHssm-ec2 --template-body file://1.3.yml --parameters file://params2.json --profile temp
```
Added an output of the URL

http://my-application-load-balancer-873233979.us-east-1.elb.amazonaws.com/

*********************************************************************************************************
*Create a KMS key*
```
aws kms create-key --profile temp
```

"KeyId": "6c1999a7-df67-41ec-8dac-c0040e9c62a4"

```
aws ssm put-parameter --name /laeticia/stelligent-u/lab11/engineer/Laeticia/middle-name --type  SecureString  --value Onyebuchi --key-id 6c1999a7-df67-41ec-8dac-c0040e9c62a4 --profile temp
```

```
aws cloudformation create-stack --stack-name ssm-ec2 --template-body file://1.4.yml --parameters file://params2.json --profile temp
```