import os
import sys
import datetime

from Helper import *
from ProcessModule import *
from MailModule import *


def main():

    if len(sys.argv) < 2:

        print(
            "Usage : ProcInfoLog.py DirectoryName Email(Optional)"
        )

        return

    dirname = sys.argv[1]

    if CreateDirectory(dirname) == False:

        return

    filename = "ProcessLog_" + datetime.datetime.now().strftime(
        "%d_%m_%Y_%H_%M_%S"
    ) + ".log"

    filepath = os.path.join(
        dirname,
        filename
    )

    CreateLogger(filepath)

    DisplayProcess()

    if len(sys.argv) == 3:

        receiver = sys.argv[2]

        if SendMail(receiver, filepath):

            print("Mail Sent Successfully")

        else:

            print("Unable to Send Mail")


if __name__ == "__main__":
    main()