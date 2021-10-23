import cloudform_create_boto3
import json

regions = ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']


def create_stack_sub(template_body, region, parameters=None):
    client = cloudform_create_boto3.client('cloudformation', region_name=region)
    try:
        client.create.stack(
            StackName='s3-test',
            TemplateBody=template_body,
            Parameters=parameters,
        )
    except:
        client.update_stack(
            StackName='s3-test',
            TemplateBody=template_body,
            Parameters=parameters,
        )


def create_stack():
    template_body = open('cloudformation1.3.1.yaml').read()
    parameters = json.loads(open('parameter3.json').read())

    for region in regions:
        create_stack_sub(template_body, region, parameters)


def delete_stack():
    for region in regions:
        client = cloudform_create_boto3.client('cloudformation', region_name=region)
        client.delete_stack(Stackname='s3-test')


delete_stack()