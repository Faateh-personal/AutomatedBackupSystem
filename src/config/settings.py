# Paths to directories or files you want to back up
BACKUP_DIRS = [
    'path/to/dir1',
    'path/to/dir2'
]

# AWS S3 bucket name
S3_BUCKET_NAME = 'your-s3-bucket-name'

# Encryption key for encrypting backup files
# Note: In a real application, you should generate this key securely and store it safely.
ENCRYPTION_KEY = b'your-encryption-key'

# Name of the compressed backup file
BACKUP_FILE_NAME = 'backup.tar.gz'

# Name of the encrypted backup file
ENCRYPTED_BACKUP_FILE_NAME = 'backup_encrypted.tar.gz'
