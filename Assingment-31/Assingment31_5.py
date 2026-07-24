import os
import schedule
import datetime
import time

def CountFiles(directorypath):
    TotalFiles = 0
    for FolderName, SubFolderName, FileName in os.walk(directorypath):
        TotalFiles = TotalFiles + 1

    fobj = open("DirectoryCountLog.txt", "a")

    fobj.write("-" * 40 + "\n")
    fobj.write("Directory Path : " + directorypath + "\n")
    fobj.write("Number of Files : " + str(TotalFiles) + "\n")
    fobj.write("Date and Time : " +
               datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")

    fobj.close()

    print("Log Updated Successfully")



def main():

    drive = input("Enter Drive (E:\\) : ")
    folder = input("Enter Folder Name : ")

    directoryPath = os.path.join(drive, folder)

    if os.path.isdir(directoryPath):

        schedule.every(5).minutes.do(CountFiles, directoryPath)

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid Directory")


if __name__ == "__main__":
    main()   
