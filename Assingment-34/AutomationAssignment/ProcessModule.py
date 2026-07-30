import psutil
import logging


def GetProcessInfo():

    ProcessList = []

    try:

        for process in psutil.process_iter():

            try:

                info = process.as_dict(attrs=[
                    'pid',
                    'name',
                    'username'
                ])

                ProcessList.append(info)

            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess
            ):
                pass

    except Exception as e:
        logging.error(str(e))

    return ProcessList


def DisplayProcess():

    ProcessList = GetProcessInfo()

    for process in ProcessList:

        logging.info(
            f"PID : {process['pid']}  "
            f"Name : {process['name']}  "
            f"User : {process['username']}"
        )


def SearchProcess(ProcessName):

    flag = False

    ProcessList = GetProcessInfo()

    for process in ProcessList:

        if process['name']:

            if process['name'].lower() == ProcessName.lower():

                logging.info(
                    f"PID : {process['pid']} "
                    f"Name : {process['name']} "
                    f"User : {process['username']}"
                )

                flag = True

    if flag == False:
        logging.info("Process not running.")