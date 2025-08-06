# AWS Lambda EC2 Scheduler

This project contains two AWS Lambda functions that automatically **start** and **stop** all EC2 instances on a daily schedule.

## 🕒 Schedule

| Function | Action         | Time (IST) | Cron (UTC)          |
|----------|----------------|------------|----------------------|
| Start    | Start EC2s     | 11:00 AM   | `cron(30 5 * * ? *)` |
| Stop     | Stop EC2s      | 08:00 PM   | `cron(30 14 * * ? *)`|

---

## 🛠 Setup Instructions

### 1. Create IAM Role for Lambda
- Create a role with the following permissions:
  - `AmazonEC2FullAccess`
  - `SNSPublish`
- Trust relationship must allow Lambda to assume the role.

### 2. Create SNS Topic
Use this ARN in both functions:
```
arn:aws:sns:us-east-1:727646469309:lambdatrigger
```

### 3. Create Lambda Functions
Create **two separate** Lambda functions:

#### lambda_start.py
Starts all stopped EC2 instances and sends an SNS email notification.

#### lambda_stop.py
Stops all running EC2 instances and sends an SNS email notification.

### 4. Setup EventBridge Scheduler

#### For Start (11:00 AM IST):
```bash
cron(30 5 * * ? *)
```

#### For Stop (08:00 PM IST):
```bash
cron(30 14 * * ? *)
```

Use these as EventBridge rule triggers for the respective Lambda functions.

---

## 📂 Files

- `lambda_start.py` — Starts all EC2 instances
- `lambda_stop.py` — Stops all EC2 instances
- `README.md` — Setup documentation