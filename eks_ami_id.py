import boto3

ec2 = boto3.client('ec2')
ssm = boto3.client('ssm')

# instance_type = 'm7g.xlarge'
instance_type = 'm5.xlarge'

response = ec2.describe_instance_types(InstanceTypes=[instance_type])
# print(response)
architecture = response['InstanceTypes'][0]['ProcessorInfo']['SupportedArchitectures'][0]
print(architecture)

if architecture == 'arm64':
    param_name = f'/aws/service/eks/optimized-ami/1.28/amazon-linux-2-arm64/recommended/image_id'
else:
    param_name = f'/aws/service/eks/optimized-ami/1.28/amazon-linux-2/recommended/image_id'

# # Get the parameter
param = ssm.get_parameter(Name=param_name)
ami_id = param['Parameter']['Value']
print(ami_id)
