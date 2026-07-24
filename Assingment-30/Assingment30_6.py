import schedule
import time

def lunchTime():
    print("Lunch Time!")

def wrapUpWork():
    print("Wrap up work")

def main():
    schedule.every().day.at("13:00").do(lunchTime)   
    schedule.every().day.at("18:00").do(wrapUpWork) 

    print("Scheduler started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()