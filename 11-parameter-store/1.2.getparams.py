import boto3

client = boto3.client('ssm')

response = client.get_parameters(
    Names=['/laeticia/stelligent-u/lab11/engineer/Laeticia/title', ]
)
print('Single parameter')
for i in response['Parameters']:
    print(i['Name'])
    print(i['Value'])
    print()


print('Multiple parameter')
response = client.get_parameters_by_path(
    Path='/laeticia/stelligent-u/lab11/',
    Recursive=True,
)

for i in response['Parameters']:
    print(i['Name'])
    print(i['Value'])
    print()
