import boto3

ec2 = boto3.client('ec2')
sns = boto3.client('sns')

# Replace with your actual SNS topic ARN
SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:123456789012:ec2-lambda-alerts'

def lambda_handler(event, context):
    try:
        action = event.get('action', '').lower()

        if action == 'start':
            instances = ec2.describe_instances(
                Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}]
            )
        elif action == 'stop':
            instances = ec2.describe_instances(
                Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
            )
        else:
            msg = "Invalid action. Use 'start' or 'stop'."
            publish_to_sns("EC2 Action Failed", msg)
            return {'statusCode': 400, 'body': msg}

        instance_ids = [
            i['InstanceId']
            for r in instances['Reservations']
            for i in r['Instances']
        ]

        if not instance_ids:
            msg = f"No EC2 instances to {action}."
            publish_to_sns("EC2 Lambda Info", msg)
            return {'statusCode': 200, 'body': msg}

        if action == 'start':
            ec2.start_instances(InstanceIds=instance_ids)
        else:
            ec2.stop_instances(InstanceIds=instance_ids)

        msg = f"EC2 instances {action}ed:\n" + "\n".join(instance_ids)
        publish_to_sns(f"EC2 Instances {action.title()}ed", msg)
        return {'statusCode': 200, 'body': msg}

    except Exception as e:
        error_msg = f"Error during EC2 {action}:\n{str(e)}"
        publish_to_sns("EC2 Lambda Error", error_msg)
        return {'statusCode': 500, 'body': error_msg}

def publish_to_sns(subject, message):
    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject=subject,
        Message=message
    )
