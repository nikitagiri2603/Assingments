"""
MarvellousModule.py

User-defined module containing validation, checksum calculation,
recursive scanning, duplicate deletion, logging, and email functions.
"""

import os
import re
import hashlib
import datetime
import smtplib
from pathlib import Path
from email.message import EmailMessage


def validate_directory(directory_path):
    """Validate the supplied directory path."""
    if directory_path is None or directory_path.strip() == "":
        return False, "Directory path is not provided."

    if not os.path.isabs(directory_path):
        return False, "Directory path must be absolute."

    if not os.path.exists(directory_path):
        return False, "Specified path does not exist."

    if not os.path.isdir(directory_path):
        return False, "Specified path is not a directory."

    if not os.access(directory_path, os.R_OK):
        return False, "Directory is not readable."

    return True, ""


def validate_interval(interval_text):
    """Validate and convert the interval to a positive number of minutes."""
    try:
        interval = float(interval_text)

        if interval <= 0:
            return False, None, "Time interval must be greater than zero."

        return True, interval, ""

    except ValueError:
        return False, None, "Time interval must be numeric."


def validate_email(email_address):
    """Perform basic email-address format validation."""
    if email_address is None or email_address.strip() == "":
        return False, "Receiver email address is not provided."

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if re.match(pattern, email_address) is None:
        return False, "Invalid receiver email address."

    return True, ""


def calculate_checksum(file_path):
    """Calculate the MD5 checksum of a file by reading it in blocks."""
    hash_object = hashlib.md5()

    with open(file_path, "rb") as file_object:
        while True:
            buffer = file_object.read(1024 * 1024)

            if not buffer:
                break

            hash_object.update(buffer)

    return hash_object.hexdigest()


def scan_directory(directory_path):
    """
    Recursively scan the directory.

    Returns:
        checksum_map : {checksum: [file paths]}
        total_files  : number of regular files encountered
        errors       : list of errors
    """
    checksum_map = {}
    errors = []
    total_files = 0

    for folder_name, subfolder_names, file_names in os.walk(directory_path):
        for file_name in file_names:
            file_path = os.path.join(folder_name, file_name)
            total_files += 1

            try:
                if not os.path.exists(file_path):
                    errors.append(f"File does not exist: {file_path}")
                    continue

                if not os.path.isfile(file_path):
                    errors.append(f"Not a regular file: {file_path}")
                    continue

                if not os.access(file_path, os.R_OK):
                    errors.append(f"File is not readable: {file_path}")
                    continue

                checksum = calculate_checksum(file_path)

                if checksum not in checksum_map:
                    checksum_map[checksum] = []

                checksum_map[checksum].append(file_path)

            except PermissionError as error:
                errors.append(f"Permission error for {file_path}: {error}")

            except OSError as error:
                errors.append(f"OS error for {file_path}: {error}")

            except Exception as error:
                errors.append(f"Unexpected error for {file_path}: {error}")

    return checksum_map, total_files, errors


def find_duplicates(checksum_map):
    """Return only checksum groups containing more than one file."""
    duplicates = {}

    for checksum, file_paths in checksum_map.items():
        if len(file_paths) > 1:
            duplicates[checksum] = file_paths

    return duplicates


def delete_duplicate_files(duplicates):
    """
    Keep the first file from every duplicate group and delete the rest.

    Returns:
        deleted_files : [(path, checksum), ...]
        errors        : list of errors
    """
    deleted_files = []
    errors = []

    for checksum, file_paths in duplicates.items():
        # file_paths[0] is preserved as the original.
        for file_path in file_paths[1:]:
            try:
                if not os.path.exists(file_path):
                    errors.append(f"File does not exist before deletion: {file_path}")
                    continue

                if not os.path.isfile(file_path):
                    errors.append(f"Cannot delete non-regular file: {file_path}")
                    continue

                parent_directory = os.path.dirname(file_path)

                if not os.access(parent_directory, os.W_OK):
                    errors.append(f"No delete permission for: {file_path}")
                    continue

                os.remove(file_path)
                deleted_files.append((file_path, checksum))

            except PermissionError as error:
                errors.append(f"Permission error while deleting {file_path}: {error}")

            except OSError as error:
                errors.append(f"Could not delete {file_path}: {error}")

            except Exception as error:
                errors.append(f"Unexpected deletion error for {file_path}: {error}")

    return deleted_files, errors


def create_log_directory():
    """Create/reuse the Marvellous log directory in the current working directory."""
    log_directory = Path.cwd() / "Marvellous"
    log_directory.mkdir(parents=True, exist_ok=True)
    return log_directory


def create_log_file(log_directory):
    """Generate a timestamp-based log filename."""
    timestamp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    return log_directory / f"DuplicateRemovalLog_{timestamp}.log"


def format_time(value):
    """Format datetime for log/email output."""
    return value.strftime("%d %B %Y, %I:%M:%S %p")


def generate_email_body(statistics):
    """Generate the operation-statistics email body."""
    return f"""Jay Ganesh,

The duplicate-file removal operation has been completed successfully.

Operation Statistics:

Starting time of scanning: {format_time(statistics["start_time"])}
Completion time of scanning: {format_time(statistics["completion_time"])}
Directory scanned: {statistics["directory"]}
Total number of files scanned: {statistics["total_files"]}
Total number of duplicate files found: {statistics["duplicates_found"]}
Total number of duplicate files deleted: {statistics["duplicates_deleted"]}

Please find the detailed log file attached to this email.

Regards,
Marvellous Automation System
"""


def write_log(log_path, statistics, deleted_files, errors, email_status):
    """Write all operational details to the log file."""
    with open(log_path, "w", encoding="utf-8") as log_file:
        log_file.write("-" * 70 + "\n")
        log_file.write("Marvellous Infosystems - Duplicate File Removal Automation\n")
        log_file.write("-" * 70 + "\n\n")

        log_file.write(
            f"Starting time of directory scanning : "
            f"{format_time(statistics['start_time'])}\n"
        )
        log_file.write(
            f"Completion time of directory scanning : "
            f"{format_time(statistics['completion_time'])}\n"
        )
        log_file.write(f"Name of directory scanned : {statistics['directory']}\n")
        log_file.write(f"Total number of files scanned : {statistics['total_files']}\n")
        log_file.write(
            f"Total number of duplicate files found : "
            f"{statistics['duplicates_found']}\n"
        )
        log_file.write(
            f"Total number of duplicate files deleted : "
            f"{statistics['duplicates_deleted']}\n"
        )

        log_file.write("\nDeleted Duplicate Files\n")
        log_file.write("-" * 70 + "\n")

        if deleted_files:
            for file_path, checksum in deleted_files:
                log_file.write(f"Path     : {file_path}\n")
                log_file.write(f"Checksum : {checksum}\n\n")
        else:
            log_file.write("No duplicate files were deleted.\n")

        log_file.write("\nErrors Encountered\n")
        log_file.write("-" * 70 + "\n")

        if errors:
            for error in errors:
                log_file.write(error + "\n")
        else:
            log_file.write("No errors encountered.\n")

        log_file.write("\nEmail Delivery Status\n")
        log_file.write("-" * 70 + "\n")
        log_file.write(email_status + "\n")


def send_email(receiver_email, log_path, statistics):
    """
    Send the log as an email attachment.

    Credentials are read from environment variables:
        MARVELLOUS_SENDER_EMAIL
        MARVELLOUS_EMAIL_APP_PASSWORD

    Example for Gmail SMTP is used here.
    """
    sender_email = os.getenv("MARVELLOUS_SENDER_EMAIL")
    app_password = os.getenv("MARVELLOUS_EMAIL_APP_PASSWORD")

    if not sender_email or not app_password:
        return (
            "Email not sent: configure MARVELLOUS_SENDER_EMAIL and "
            "MARVELLOUS_EMAIL_APP_PASSWORD environment variables."
        )

    try:
        message = EmailMessage()
        message["Subject"] = "Duplicate File Removal Automation Report"
        message["From"] = sender_email
        message["To"] = receiver_email
        message.set_content(generate_email_body(statistics))

        with open(log_path, "rb") as file_object:
            log_data = file_object.read()

        message.add_attachment(
            log_data,
            maintype="application",
            subtype="octet-stream",
            filename=Path(log_path).name,
        )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, app_password)
            smtp.send_message(message)

        return "Email sent successfully."

    except smtplib.SMTPAuthenticationError as error:
        return f"Email authentication failed: {error}"

    except smtplib.SMTPException as error:
        return f"SMTP error: {error}"

    except OSError as error:
        return f"Email/network/file error: {error}"

    except Exception as error:
        return f"Unexpected email error: {error}"


def perform_duplicate_removal(directory_path, receiver_email):
    """Perform one complete duplicate-file removal operation."""
    start_time = datetime.datetime.now()

    checksum_map, total_files, scan_errors = scan_directory(directory_path)
    duplicates = find_duplicates(checksum_map)

    # Count only the removable copies. The first file in each group is preserved.
    duplicates_found = sum(len(file_paths) - 1 for file_paths in duplicates.values())

    deleted_files, deletion_errors = delete_duplicate_files(duplicates)
    completion_time = datetime.datetime.now()

    statistics = {
        "start_time": start_time,
        "completion_time": completion_time,
        "directory": directory_path,
        "total_files": total_files,
        "duplicates_found": duplicates_found,
        "duplicates_deleted": len(deleted_files),
    }

    errors = scan_errors + deletion_errors

    log_directory = create_log_directory()
    log_path = create_log_file(log_directory)

    # Create the log first so that it exists before email attachment.
    write_log(
        log_path,
        statistics,
        deleted_files,
        errors,
        "Email delivery pending.",
    )

    email_status = send_email(receiver_email, log_path, statistics)

    # Rewrite/update the same log with final email delivery status.
    write_log(
        log_path,
        statistics,
        deleted_files,
        errors,
        email_status,
    )

    return log_path
