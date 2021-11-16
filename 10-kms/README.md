*Create stack that creates a CMK key in KMS*
```
aws cloudformation create-stack --stack-name kms-lh --template-body file://10.1.1.yaml --parameters --profile temp
```
-------------------------------------------------------------------------------------------------------
*Create a KMS alias and update the stack*
```
aws cloudformation update-stack --stack-name kms-lh --template-body file://10.1.2.yaml --parameters --profile temp
```
-------------------------------------------------------------------------------------------------------
*Use the key to encrypt a plain text file*
```
aws kms encrypt --key-id 88ff5a76-86d6-4864-8869-905a9debc6bb --plaintext fileb://10.1.3.txt --output text --query CiphertextBlob | base 64 --decode > myencryptedfile.dat
```
-------------------------------------------------------------------------------------------------------
*Decrypt the file*
```
aws kms decrypt --ciphertext-blob fileb://myencryptedfile.dat --output text --query Plaintext | base64 --decode 
```

Here is the output I got

Combination lock to my private hangar: 9007369%                                                                  

--------------------------------------------------------------------------------------------------------
*Ran python script*
```
python3 10.2.1.py 
```

newFile.txt was created