# EC2 Lambda Scheduler (Start/Stop EC2 Instances Daily)

This project contains two AWS Lambda functions:

- ✅ `lambda_start-ec2.py`: Starts all EC2 instances every day at **11:00 AM IST**
- ✅ `lambda_stop-ec2.py`: Stops all EC2 instances every day at **8:00 PM IST**
- 📩 Sends notification via **Amazon SNS** on success/failure

---

## 🛠️ Prerequisites

- An AWS account
- IAM permissions to manage EC2, SNS, Lambda, EventBridge
- Python 3.12+ runtime for Lambda

---

## 📁 Project Structure

ec2-start-stop-automatic/
├── lambda_start.py # Start EC2 Instances
├── lambda_stop.py # Stop EC2 Instances
└── README.md # Setup Instructions


------------------------------------------------------------------------

## 🔔 Step 1: Create an SNS Topic (for Email Notifications)

1. Go to the **SNS** service in AWS Console.
2. Click **Topics** > **Create topic**
3. Choose:
   - **Type:** Standard
   - **Name:** `lambdatrigger` (or any name you like)
4. After creating, copy the **Topic ARN**
5. Click **Create subscription**:
   - **Protocol:** Email
   - **Endpoint:** Your email address
6. Check your inbox and confirm the subscription.

------------------------------------------------------------------------

## 🔐 Step 2: Create IAM Role for Lambda

1. Go to **IAM** > **Roles**
2. Click **Create role**
3. Select:
   - **Trusted entity type:** AWS service
   - **Use case:** Lambda
4. Attach these policies:
   - `AmazonEC2FullAccess`
   - `AmazonSNSFullAccess`
   - `CloudWatchLogsFullAccess`
   - `AmazonEventBridgeFullAccess`
5. Give the role a name like `LambdaEC2StartStopRole`

------------------------------------------------------------------------

## ⚙️ Step 3: Create Lambda Function - Start EC2

1. Go to **Lambda** > **Create function**
2. Choose:
   - **Name:** `startEC2Instances`
   - **Runtime:** Python 3.12
   - **Permissions:** Use existing role → Select `lambda-ec2-scheduler-role`
3. Paste content from `lambda_start-ec2.py`
4. Replace this line with your SNS Topic ARN:
   ```python
   SNS_TOPIC_ARN = 'arn:aws:sns:region:account-id:topic-name'

------------------------------------------------------------------------

⚙️ Step 4: Create Lambda Function - Stop EC2
1. Repeat steps like above, with:
    - Name: stopEC2Instances
    - Paste content from lambda_stop-ec2.py
    - Use the same role and SNS topic

------------------------------------------------------------------------

🕒 Step 5: Create EventBridge Rule for Daily Scheduling
🔁 Start at 11:00 AM IST (UTC 05:30 → 05:30 AM UTC)
1. Go to Amazon EventBridge → Rules → Create rule
2. Name: start-ec2-daily
3. Schedule pattern:
    - Cron expression: 30 5 * * ? *
    - (This runs at 11:00 AM IST daily)
4. Target: Select the Lambda startEC2Instances

------------------------------------------------------------------------

🔁 Stop at 8:00 PM IST (UTC 05:30 → 14:30 UTC)
1. Create another rule:
    - Name: stop-ec2-daily
    - Cron expression: 30 14 * * ? *
    - Target: Lambda stopEC2Instances

------------------------------------------------------------------------

✅ Testing
You can test manually by:
    - Clicking Test in Lambda console
    - Monitoring logs in CloudWatch
    - Checking for email via SNS

------------------------------------------------------------------------