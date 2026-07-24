
import schedule
import time

def PrintTime():
    print("Coding Kar...")

def main():
    schedule.every(30).minutes.do(PrintTime)
    while True:
        schedule.run_pending()
        time.sleep(25)
    
if __name__ == "__main__":
    main()