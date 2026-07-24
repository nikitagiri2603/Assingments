import datetime
import schedule
import time

def PrintTime():
    current = datetime.datetime.now()
    print("Current Date and Time :", current.strftime("%d-%m-%Y %I:%M:%S %p"))

def main():

    schedule.every(1).minutes.do(PrintTime)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()