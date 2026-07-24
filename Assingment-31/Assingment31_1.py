import sys
import schedule
import time

def PrintMessage(msg):
    print(msg)

def main():

    if len(sys.argv) != 3:
        print("Usage : python Demo.py <Message> <Interval>")
        return
    
    interval = int(sys.argv[2])

    if interval <= 0:
        print("Enter a positive interval")
        return

    schedule.every(interval).seconds.do(PrintMessage,sys.argv[1])

    while True:
        schedule.run_pending()
        time.sleep(2)

if __name__ == "__main__":
    main()