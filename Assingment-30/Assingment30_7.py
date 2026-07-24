
import os
import shutil
import schedule
import time
import sys
import datetime 

def BackupFile(sourceFile, destinationDirectory):

    CurrentTime = datetime.datetime.now()

    BackupFileName = "filecopy_" + CurrentTime.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    DestinationPath = os.path.join(destinationDirectory, BackupFileName)

    shutil.copy2(sourceFile, DestinationPath)

    fobj3 = open("backup_log.txt", "a")
    fobj3.write("Backup completed successfully at ")
    fobj3.write(CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p"))
    fobj3.write("\n")
    fobj3.close()

    print("Backup completed successfully...")


# def BackupFile(sourceFile, destinationDirectory):

#     CurrentTime = datetime.datetime.now()
#     fobj1 = open(sourceFile,"rb")
#     Data = fobj1.read()

#     BackupFileName = "filecopy_" + CurrentTime.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"
#     DestinationPath = os.path.join(destinationDirectory, BackupFileName)

#     fobj2 = open(DestinationPath, "wb")
#     fobj2.write(Data)

#     fobj3 = open("backup_log.txt","a")
#     fobj3.write(f"Backup Completed at {datetime.datetime.now()}\n")

#     fobj1.close()
#     fobj2.close()
#     fobj3.close()

def main():

    sourceFile = sys.argv[1]
    destinationDirectory = sys.argv[2]

    schedule.every(1).hours.do(BackupFile, sourceFile, destinationDirectory)

    print("Backup scheduler started...")

    while True:
        schedule.run_pending()
        time.sleep(3)

if __name__ == "__main__":
    main()