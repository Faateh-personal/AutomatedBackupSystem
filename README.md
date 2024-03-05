# Automated Backup System

An automated system for backing up files and directories to AWS S3 with encryption for added security.

## Features

- Compresses and encrypts files before backup
- Uploads encrypted backups to AWS S3
- Configurable backup directories and schedule
- Logging for monitoring and troubleshooting

## Requirements

- Python 3.8 or higher
- AWS S3 account and bucket
- `boto3` and `cryptography` Python libraries

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/AutomatedBackupSystem.git
   ```

2. Navigate to the project directory:
   ```
   cd AutomatedBackupSystem
   ```

3. Install the required Python libraries:
   ```
   pip install -r requirements.txt
   ```

4. Configure your AWS credentials. You can do this by setting up the AWS CLI or by configuring environment variables:
   ```
   aws configure
   ```
   Or set environment variables:
   ```
   export AWS_ACCESS_KEY_ID=your_access_key_id
   export AWS_SECRET_ACCESS_KEY=your_secret_access_key
   ```

5. Update the `config/settings.py` file with your backup directories, S3 bucket name, and encryption key.

## Usage

Run the `main.py` script to start the backup process:
```
python src/main.py
```

Check the `logs/backup.log` file for logs and any errors that may occur during the backup process.

