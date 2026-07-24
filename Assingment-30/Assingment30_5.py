import schedule
import time
import datetime
def Task():
    fobj = open("Marvellous.txt","a")
    fobj.write(f"Task executed at : {datetime.datetime.now()}\n")
    fobj.close()
def main():
    schedule.every(5).minutes.do(Task)
    while True:
        schedule.run_pending()
        time.sleep(290)

if __name__ == "__main__":
    main()