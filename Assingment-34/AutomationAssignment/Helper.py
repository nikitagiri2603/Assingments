import os
import logging


def CreateDirectory(dirname):
    try:
        if not os.path.exists(dirname):
            os.mkdir(dirname)
            return True
        return True
    except Exception:
        return False


def CreateLogger(logfile):

    logging.basicConfig(
        filename=logfile,
        level=logging.INFO,
        format="%(asctime)s : %(message)s"
    )