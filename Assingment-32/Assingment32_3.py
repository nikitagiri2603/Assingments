import sys
import schedule
import time

def DisplayContents(file1):
    try:
        fobj = open(file1,"r")
        Data = fobj.read()

        if Data == "":
            print("File is empty")
        else:
            print(Data)
        fobj.close()
    except OSError as eobj:
        print("File cannot be opened")
        print(eobj)
    except PermissionError as pobj:
        print(pobj)
    except FileNotFoundError as eobj:
        print(eobj)

def main():
    schedule.every(1).minutes.do(DisplayContents,sys.argv[1])
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()