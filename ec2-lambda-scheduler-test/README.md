# EC2 Lambda Scheduler with SNS Notifications

This project demonstrates how to use an AWS Lambda function to automatically start and stop EC2 instances and notify via Amazon SNS. It includes manual control via test events and automated scheduling using Amazon EventBridge.

---

## 📌 Features

- ✅ Start and Stop **all EC2 instances** in a region
- ✅ Send **SNS email notifications** on success or failure
- ✅ Schedule automatic stop using **EventBridge** (e.g., daily at 8 PM IST)
- ✅ Notify when EC2 control actions succeed or fail

---

## 📁 Project Structure

├── lambda_ec2_control.py # Lambda function to start/stop EC2 & send SNS alerts

├── README.md # Project documentation

## 🧱 Infrastructure as Code (YAML)
---
## 🚀 How It Works

1. Deploy the `lambda_ec2_control.py` code in an AWS Lambda function.
2. Attach an IAM role with EC2 and SNS permissions.
3. Create an SNS topic and subscribe your email address.
4. Trigger the function manually or using EventBridge scheduler.
5. Lambda stops/starts all EC2 instances and sends SNS notification.

---

## 📥 Sample Lambda Event Input

To **start** all instances:
```json
{
  "action": "start"
}
To stop all instances:

json
Copy
Edit
{
  "action": "stop"
}
🛠️ Prerequisites
✅ AWS account

✅ EC2 instances in running/stopped state

✅ Confirmed SNS email subscription

✅ IAM Role for Lambda with permissions:

ec2:StartInstances

ec2:StopInstances

ec2:DescribeInstances

sns:Publish

⏰ EventBridge Schedule Setup
To stop instances every day at 8 PM IST (2:30 PM UTC):

Go to Amazon EventBridge > Rules > Create Rule

Select:

Rule type: Schedule

Cron expression:

scss
Copy
Edit
cron(30 14 * * ? *)
(This means 14:30 UTC = 20:00 IST)

Target: your Lambda function

✅ Expected Output
You will receive an email from SNS like this:

Subject:
nginx
Copy
Edit
EC2 Instances Stopped
Body:
diff
Copy
Edit
EC2 instances stopped:
- i-0123abc456def7890
- i-0abc123def4567890
In case of failure:

javascript
Copy
Edit
Error occurred while stopping EC2 instances:
<Error details>
🧪 Testing the Function
Open AWS Lambda Console

Choose your function

Select Test

Create a test event with:

json
Copy
Edit
{ "action": "start" }
or

json
Copy
Edit
{ "action": "stop" }
Check your email for results

