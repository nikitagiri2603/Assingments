import time

import schedule

def Print():
    print("Jay Ganesh...")

def main():
    schedule.every(2).seconds.do(Print)
    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__ == "__main__":
    main()