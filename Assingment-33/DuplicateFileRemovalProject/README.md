# Duplicate File Removal Automation

## 1. Project Title

**Duplicate File Removal Automation**

## 2. Project Description

This Python automation project periodically scans a supplied directory and its
subdirectories, calculates file checksums, detects duplicate files based on
their content, preserves the first file in each duplicate group, deletes the
remaining copies, generates a detailed timestamp-based log, and sends the log
to a receiver through email.

## 3. Features

- Recursive directory scanning
- MD5 checksum-based duplicate detection
- Automatic duplicate-file deletion
- Preserves one original file from each duplicate group
- Timestamp-based log generation
- Periodic execution
- Email notification
- Log-file attachment
- Command-line input validation
- Exception handling
- Modular programming
- Help and Usage options

## 4. Requirements

- Python 3.10 or later recommended
- `schedule` Python package
- Python standard libraries used:
  - os
  - sys
  - hashlib
  - datetime
  - smtplib
  - pathlib
  - re
  - email
- Internet connection for sending email
- SMTP credentials / application password

Install the external dependency:

```bash
pip install schedule
```

## 5. Project Structure

```text
DuplicateFileRemovalProject/
|
|-- DuplicateFileRemoval.py
|-- MarvellousModule.py
|-- requirements.txt
|-- README.md
|
|-- Marvellous/
|   `-- generated log files
|
`-- Demo/
    |-- File1.txt
    |-- File2.txt
    |-- CopyFile1.txt
    `-- SubFolder/
        `-- CopyFile2.txt
```

### DuplicateFileRemoval.py

Main script. It processes command-line arguments, supports Help and Usage,
validates input, starts the operation, and schedules repeated execution.

### MarvellousModule.py

User-defined module containing functions for:

- directory validation
- interval validation
- email validation
- checksum calculation
- recursive directory scanning
- duplicate detection
- duplicate deletion
- log creation
- email-body creation
- email sending

### Marvellous

Contains timestamp-based `.log` files generated after each operation.

### Demo

Sample directory for safe testing.

## 6. Command-Line Options

The program accepts three arguments:

1. Absolute directory path
2. Time interval in minutes
3. Receiver email address

## 7. Execution Command

Windows example:

```bash
python DuplicateFileRemoval.py "C:\Users\YourName\Desktop\Demo" 50 receiver@gmail.com
```

Assignment-style example:

```bash
python DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com
```

The operation executes once when the program starts and then repeats according
to the specified interval.

## 8. Help Command

```bash
python DuplicateFileRemoval.py --help
```

or:

```bash
python DuplicateFileRemoval.py -h
```

## 9. Usage Command

```bash
python DuplicateFileRemoval.py --usage
```

or:

```bash
python DuplicateFileRemoval.py -u
```

## 10. Log-File Information

Logs are stored in the `Marvellous` directory created in the current working
directory.

Example:

```text
DuplicateRemovalLog_20_07_2026_23_30_15.log
```

Each log contains:

- scanning start time
- scanning completion time
- scanned directory
- total files scanned
- duplicate files found
- duplicate files deleted
- complete deleted-file paths
- duplicate checksums
- execution errors
- email delivery status

## 11. Email Configuration

Do not hard-code your email password in the Python source code.

This implementation reads the sender credentials from environment variables:

```text
MARVELLOUS_SENDER_EMAIL
MARVELLOUS_EMAIL_APP_PASSWORD
```

For Windows Command Prompt:

```bat
set MARVELLOUS_SENDER_EMAIL=youraccount@gmail.com
set MARVELLOUS_EMAIL_APP_PASSWORD=your_app_password
```

For PowerShell:

```powershell
$env:MARVELLOUS_SENDER_EMAIL="youraccount@gmail.com"
$env:MARVELLOUS_EMAIL_APP_PASSWORD="your_app_password"
```

The supplied implementation uses Gmail SMTP (`smtp.gmail.com`, port 465).
Use an application password where required by your email provider.

## 12. Important Notes

- Duplicate files are detected using file checksums, not filenames.
- The first file from every duplicate checksum group is preserved.
- Remaining duplicate copies are deleted.
- Deleted files may not be recoverable.
- Always test the program on a sample directory first.
- Never test destructive automation on important files.
- Email passwords should never be hard-coded.
- Locked files and permission failures are recorded as errors when possible.
