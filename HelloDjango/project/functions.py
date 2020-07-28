import os
from uuid import uuid4


def path_and_rename(path, prefix):
    def wrapper(filename):
        ext = filename.split(".")[-1]
        # get filename
        filename = "{}.{}.{}".format(prefix, uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(path, filename)
        return wrapper
