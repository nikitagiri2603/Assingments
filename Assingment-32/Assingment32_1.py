import time
import schedule
import datetime

def CreateTextFile():

    currentTime = datetime.datetime.now()

    filename = "File_" + currentTime.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    fobj = open(filename, "w")

    fobj.write("File Name : " + filename + "\n")
    fobj.write("Creation Date : ")
    fobj.write(currentTime.strftime("%d-%m-%Y"))
    fobj.write("\nCreation Time : ")
    fobj.write(currentTime.strftime("%d %I:%M:%S %p"))

    fobj.close()

def main():

    schedule.every(5).seconds.do(CreateTextFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


