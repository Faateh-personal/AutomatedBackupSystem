import sys
from backup.backup_manager import backup_files
from config.settings import (
    BACKUP_DIRS,
    S3_BUCKET_NAME,
    ENCRYPTION_KEY,
    BACKUP_FILE_NAME,
    ENCRYPTED_BACKUP_FILE_NAME,
)
from logging.logger import logger

def main():
    try:
        logger.info("Starting backup process...")
        backup_files(
            file_paths=BACKUP_DIRS,
            output_filename=BACKUP_FILE_NAME,
            encrypted_filename=ENCRYPTED_BACKUP_FILE_NAME,
            encryption_key=ENCRYPTION_KEY,
            bucket_name=S3_BUCKET_NAME,
        )
        logger.info("Backup process completed successfully.")
    except Exception as e:
        logger.error(f"An error occurred during backup: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

