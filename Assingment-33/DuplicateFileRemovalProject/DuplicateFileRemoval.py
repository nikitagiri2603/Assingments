"""
DuplicateFileRemoval.py

Main script for Duplicate File Removal Automation.

Usage:
    python DuplicateFileRemoval.py <AbsoluteDirectoryPath> <TimeIntervalInMinutes> <ReceiverEmailAddress>

Options:
    --help, -h      Display help
    --usage, -u     Display usage
"""

import sys
import time
import schedule

from MarvellousModule import (
    validate_directory,
    validate_interval,
    validate_email,
    perform_duplicate_removal,
)

HELP_TEXT = """
Duplicate File Removal Automation

This script scans a directory recursively, identifies duplicate files using
checksums, deletes duplicate copies, creates a log file, and sends the log file
through email.

Usage:
python DuplicateFileRemoval.py <DirectoryPath> <IntervalInMinutes> <ReceiverEmail>

Example:
python DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com

Arguments:
DirectoryPath       Absolute path of the directory to scan.
IntervalInMinutes   Positive numeric interval in minutes.
ReceiverEmail       Email address that receives the operation report.

Options:
--help, -h           Display this help.
--usage, -u          Display command usage.
"""

USAGE_TEXT = """
Usage:
python DuplicateFileRemoval.py <AbsoluteDirectoryPath> <TimeIntervalInMinutes> <ReceiverEmailAddress>
"""


def main():

    if len(sys.argv) == 2:
        if sys.argv[1] in ("--help", "-h"):
            print(HELP_TEXT)
            return

        if sys.argv[1] in ("--usage", "-u"):
            print(USAGE_TEXT)
            return

    if len(sys.argv) != 4:
        print(USAGE_TEXT)
        return

    directory_path = sys.argv[1]
    interval_text = sys.argv[2]
    receiver_email = sys.argv[3]

    valid, error = validate_directory(directory_path)
    if not valid:
        print("Error:", error)
        return

    valid, interval, error = validate_interval(interval_text)
    if not valid:
        print("Error:", error)
        return

    valid, error = validate_email(receiver_email)
    if not valid:
        print("Error:", error)
        return


    perform_duplicate_removal(directory_path, receiver_email)

    schedule.every(interval).minutes.do(
        perform_duplicate_removal,
        directory_path,
        receiver_email,
    )

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
