import boto3

def get_ec2_instances():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    instances = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append({
                'id': instance['InstanceId'],
                'type': instance['InstanceType'],
                'state': instance['State']['Name'],
                'launch_time': instance['LaunchTime']
            })
    return instances


def get_s3_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    return response['Buckets']
