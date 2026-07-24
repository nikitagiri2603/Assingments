
import time
import schedule
import datetime

def CreateLogFile():

    CurrentTime = datetime.datetime.now()
    filename = "MarvellousLog_" + CurrentTime.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"
    fobj = open(filename,"w")
    fobj.write("Log file created successfully.\n")
    fobj.write("Creation Time : " + CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p"))
    fobj.close()

def main():
    schedule.every(10).minutes.do(CreateLogFile)
    while True:
        schedule.run_pending()
        time.sleep(3)

if __name__ == "__main__":
    main()