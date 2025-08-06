import boto3

ec2 = boto3.client('ec2')
sns = boto3.client('sns')

SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:727646469309:lambdatrigger'

def lambda_handler(event, context):
    try:
        response = ec2.describe_instances(Filters=[
            {'Name': 'instance-state-name', 'Values': ['stopped']}
        ])

        instances = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instances.append(instance['InstanceId'])

        if instances:
            ec2.start_instances(InstanceIds=instances)
            message = f"Successfully started instances: {instances}"
        else:
            message = "No stopped instances found."

        sns.publish(TopicArn=SNS_TOPIC_ARN, Message=message, Subject='EC2 Start Report')
        return {'statusCode': 200, 'body': message}

    except Exception as e:
        error_message = f"Failed to start EC2 instances: {str(e)}"
        sns.publish(TopicArn=SNS_TOPIC_ARN, Message=error_message, Subject='EC2 Start Failed')
        return {'statusCode': 500, 'body': error_message}