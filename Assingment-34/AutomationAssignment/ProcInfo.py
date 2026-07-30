import sys
import logging

from ProcessModule import *


logging.basicConfig(
    filename="Process.log",
    level=logging.INFO,
    format="%(asctime)s : %(message)s"
)


def main():

    if len(sys.argv) == 1:

        DisplayProcess()

    elif len(sys.argv) == 2:

        SearchProcess(sys.argv[1])

    else:

        logging.info(
            "Invalid Arguments"
        )


if __name__ == "__main__":

    main()