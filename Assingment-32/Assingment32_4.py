import os
import shutil
import schedule
import time
import datetime

def CopyTextFiles(SourceDirectory, DestinationDirectory):

    fobj = open("CopyLog.txt", "a")

    fobj.write("----------------------------------------\n")
    fobj.write("Copy Time : " +
               datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")

    for FolderName, SubFolderName, FileName in os.walk(SourceDirectory):

        for fname in FileName:

            if fname.endswith(".txt"):

                SourcePath = os.path.join(FolderName, fname)
                DestinationPath = os.path.join(DestinationDirectory, fname)

                try:
                    shutil.copy2(SourcePath, DestinationPath)

                    fobj.write("Copied : " + fname + "\n")

                except Exception as e:
                    fobj.write("Failed : " + fname + "\n")
                    print("Cannot copy :", fname)

    fobj.write("----------------------------------------\n\n")
    fobj.close()


def main():

    SourceDirectory = input("Enter Source Directory : ")
    DestinationDirectory = input("Enter Destination Directory : ")

    if not os.path.isdir(SourceDirectory):
        print("Invalid Source Directory")
        return

    if not os.path.isdir(DestinationDirectory):
        print("Invalid Destination Directory")
        return
    
    schedule.every(10).minutes.do(CopyTextFiles,SourceDirectory,DestinationDirectory)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()