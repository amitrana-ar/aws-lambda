# EC2 Lambda Scheduler Test

This repository demonstrates how to use AWS Lambda to start and stop all EC2 instances in a region, with email notifications via SNS and automatic daily scheduling using Amazon EventBridge.

## Features

- ✅ Start or stop **all EC2 instances** in a given region.
- 📧 Send **SNS email notifications** for both success and failure events.
- 🕗 **Scheduled stop** at 8 PM IST using **Amazon EventBridge**.
- 🧪 Manual invocation support for testing.

## Lambda Function Overview

- Language: **Python 3.12**
- Dependencies: Uses `boto3` (already available in AWS Lambda)
- Triggered manually or by EventBridge.
- Sends notifications via Amazon SNS.

## How It Works

- The Lambda function:
  - Fetches all EC2 instance IDs in the specified region.
  - Starts or stops them based on the `event["action"]` input.
  - Sends an SNS email with a list of affected instances.
  - Catches and reports any errors via SNS.

## Files

- `lambda.py` – The core Lambda function.
- `README.md` – This file.

## Setup Instructions

### 1. Create an SNS Topic

- Go to **Amazon SNS > Topics > Create topic**
- Type: **Standard**
- Name: `ec2-notifier`
- Create a subscription (email) and confirm it.

### 2. Create IAM Role for Lambda

Attach a policy with the following permissions:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:StartInstances",
        "ec2:StopInstances",
        "ec2:DescribeInstances",
        "sns:Publish"
      ],
      "Resource": "*"
    }
  ]
}
```

### 3. Create Lambda Function

- Runtime: Python 3.12
- Timeout: 30 seconds
- Paste contents from `lambda.py`
- Add environment variable: `SNS_TOPIC_ARN` = `arn:aws:sns:REGION:ACCOUNT_ID:ec2-notifier`
- Attach the IAM role created above.

### 4. Add Manual Testing Event

```json
{
  "action": "start"
}
```

or

```json
{
  "action": "stop"
}
```

### 5. Schedule EC2 Stop at 8 PM IST

- Go to **Amazon EventBridge > Scheduler**
- Create a new rule:
  - Fixed rate: `Every 1 day`
  - Time: `14:30 UTC` (which is 8:00 PM IST)
  - Target: Your Lambda function
  - Constant input: `{ "action": "stop" }`

## Expected Output

- 🟢 Email: EC2 Instances Started
- 🔴 Email: EC2 Instances Stopped
- ⚠️  Email: Error message if something fails

## Repository Name

> `ec2-lambda-scheduler-test`

## Author

Silicon IT Hub — DevOps Testing