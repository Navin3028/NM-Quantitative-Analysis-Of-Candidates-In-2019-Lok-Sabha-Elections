import json
import boto3
from datetime import datetime, timezone

def lambda_handler(event, context):
    client1 = boto3.client('sns')
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
    message = "\nThese are the volumes that are not attached:\n"
    
    for i in regions:
        ec2 = boto3.client('ec2', region_name=i)
        available_volumes = ec2.describe_volumes(Filters=[{
            'Name': 'status',
            'Values': ['available']
        }])
        
        if available_volumes['Volumes']:
            list_of_regions = f"Region Name: {i}"
            message += f"\n{list_of_regions}\n"
            
            for volume in available_volumes['Volumes']:
                volume_id = volume['VolumeId']
                create_time = volume['CreateTime']
                current_time = datetime.now(timezone.utc)
                duration = current_time - create_time
                days_available = duration.days
                
                volume_info = f"\n\tVolume ID: {volume_id}, Available for: {days_available} days"
                message += f"{volume_info}\n"
                
    print(message)
                
    response = client1.publish(
        TargetArn='arn:aws:sns:ap-south-1:191124798140:Ec2instanceCreation_tag',
        Message=message,
        Subject='Volumes are not Attached'
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Message sent successfully!')
    }
