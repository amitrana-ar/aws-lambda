import boto3

ec2 = boto3.client('ec2')
sns = boto3.client('sns')

SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:727646469309:lambdatrigger'

def lambda_handler(event, context):
    try:
        response = ec2.describe_instances(Filters=[
            {'Name': 'instance-state-name', 'Values': ['running']}
        ])

        instances = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instances.append(instance['InstanceId'])

        if instances:
            ec2.stop_instances(InstanceIds=instances)
            message = f"Successfully stopped instances: {instances}"
        else:
            message = "No running instances found."

        sns.publish(TopicArn=SNS_TOPIC_ARN, Message=message, Subject='EC2 Stop Report')
        return {'statusCode': 200, 'body': message}

    except Exception as e:
        error_message = f"Failed to stop EC2 instances: {str(e)}"
        sns.publish(TopicArn=SNS_TOPIC_ARN, Message=error_message, Subject='EC2 Stop Failed')
        return {'statusCode': 500, 'body': error_message}