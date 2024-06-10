#!/usr/bin/env python

import boto3
import json

def get_aws_inventory():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    inventory = {
        'all': {
            'hosts': []
        },
        '_meta': {
            'hostvars': {}
        }
    }
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            inventory['all']['hosts'].append(instance['PublicDnsName'])
            inventory['_meta']['hostvars'][instance['PublicDnsName']] = {
                'ansible_host': instance['PublicIpAddress']
            }
    return inventory

if __name__ == "__main__":
    print(json.dumps(get_aws_inventory()))
