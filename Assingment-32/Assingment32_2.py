import os
import time
import datetime
import schedule
import sys

def MonitorSize(filePath):

    currentTime = datetime.datetime.now()

    try:
        size = os.path.getsize(filePath)

        fobj = open("FileSizeLog.txt", "a")

        fobj.write("--------------------------------------\n")
        fobj.write("File Path : " + filePath + "\n")
        fobj.write("File Size : " + str(size) + " Bytes\n")
        fobj.write("Date and Time : " +
                   currentTime.strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
        fobj.write("--------------------------------------\n")

        fobj.close()

    except FileNotFoundError:
        print("File does not exist")

def main():

    schedule.every(30).seconds.do(MonitorSize, sys.argv[1])

    while True:
        schedule.run_pending()
        time.sleep(25)

if __name__ == "__main__":
    main()