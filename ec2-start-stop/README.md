# 🖥️ Manual EC2 Start/Stop using AWS Lambda + SNS Email

This project demonstrates how to **manually** start and stop **all EC2 instances** in an AWS region using **AWS Lambda**, with **email notifications** via **Amazon SNS**.

## 📦 Features

- ✅ Manually trigger Lambda to start or stop EC2 instances
- ✅ Email notifications via SNS (Amazon Simple Notification Service)
- ✅ Notification includes success and failure messages
- ✅ Uses Lambda test events for manual control

## 📁 Files

- `lambda_ec2_control.py`: Lambda function to control EC2 instances and send email via SNS

## 🚀 How to Use

1. Deploy the Lambda function from `lambda_ec2_control.py` in AWS Lambda.
2. Replace the `SNS_TOPIC_ARN` with your actual SNS topic ARN.
3. Add email subscriptions to the SNS topic and confirm them.
4. Test the function with event JSON:
```json
{ "action": "start" }
```
or
```json
{ "action": "stop" }
```

## ✅ Output Example

If instances are stopped:
```
EC2 instances stopped:
i-0123456789abcdef0
i-0fedcba9876543210
```

If no instances are running:
```
No EC2 instances to stop.
```

If the action is invalid:
```
Invalid action. Use 'start' or 'stop'.
```

---

✅ Ideal for manual EC2 management without needing to log in to the AWS Console.