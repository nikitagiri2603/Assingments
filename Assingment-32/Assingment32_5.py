import os
import schedule
import time
import datetime

def DeleteEmptyFiles(directoryPath):

    fobj = open("DeleteLog.txt", "a")

    fobj.write("----------------------------------------\n")
    fobj.write("Delete Time : " +
               datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")

    for FolderName, SubFolderName, FileName in os.walk(directoryPath):
        for fname in FileName:
            FilePath = os.path.join(FolderName, fname)
            try:
                if os.path.getsize(FilePath) == 0:
                    os.remove(FilePath)
                    print("Deleted :", FilePath)
                    fobj.write(FilePath + "\n")
            except PermissionError:
                print("Permission Denied :", FilePath)

    fobj.write("----------------------------------------\n\n")
    fobj.close()


def main():

    directoryPath = input("Enter Directory Path : ")

    if not os.path.isdir(directoryPath):
        print("Invalid Directory")
        return

    schedule.every(1).hours.do(DeleteEmptyFiles, directoryPath)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()