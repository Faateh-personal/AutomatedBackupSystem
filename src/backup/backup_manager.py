import os
import tarfile
from .encryption import encrypt_file
from .s3_client import upload_to_s3


def compress_files(file_paths, output_filename):
    """Compresses files into a tar.gz archive."""
    with tarfile.open(output_filename, 'w:gz') as tar:
        for file_path in file_paths:
            tar.add(file_path, arcname=os.path.basename(file_path))


def backup_files(file_paths, output_filename, encrypted_filename, encryption_key, bucket_name):
    """Performs the backup process: compress, encrypt, and upload."""
    # Compress files
    compress_files(file_paths, output_filename)

    # Encrypt the compressed file
    encrypt_file(output_filename, encrypted_filename, encryption_key)

    # Upload the encrypted file to S3
    upload_to_s3(encrypted_filename, bucket_name, encrypted_filename)

    # Clean up local files
    os.remove(output_filename)
    os.remove(encrypted_filename)
