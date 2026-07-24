import os
import datetime
import schedule
import time

def ScanDirectory(directoryPath):

    TotalFiles = 0
    TotalSubDirectories = 0

    for FolderName, SubFolderName, FileName in os.walk(directoryPath):

        for subf in SubFolderName:
            TotalSubDirectories = TotalSubDirectories + 1

        for fname in FileName:
            TotalFiles = TotalFiles + 1

    print("-" * 40)
    print("Directory Scanned :", directoryPath)
    print("Total Files :", TotalFiles)
    print("Total Subdirectories :", TotalSubDirectories)
    print("Scan Time :", datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
    print("-" * 40)


def main():

    drive = input("Enter Drive (E:\\) : ")
    folder = input("Enter Folder Name : ")

    directoryPath = os.path.join(drive, folder)

    if os.path.isdir(directoryPath):

        schedule.every(1).minutes.do(ScanDirectory, directoryPath)

        print("Directory Scanner Started...")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid Directory")


if __name__ == "__main__":
    main()  