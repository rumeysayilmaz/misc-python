import os
import os.path
from pathlib import Path


def home_dir():
    """returns the location of home directory of current logged-in user for cross platforms"""
    return str(Path.home())


def error(msg):
    raise Exception(msg)


def fullpath(path):
    return os.path.abspath(os.path.expanduser(path))


def parentdir(path):
    """parentdir(path), Returns the parent directory of a path."""
    path = fullpath(path)
    dir = os.path.dirname(path)
    ext = os.path.splitext(path)[1]
    file = os.path.basename(path)[0:-len(ext)] if len(ext) != 0 else os.path.basename(path)
    # if isfile
    if len(ext) != 0:
        return os.path.abspath(os.path.join(os.path.abspath(os.path.join(path, os.pardir)), os.pardir))
    else:
        return os.path.abspath(os.path.join(path, os.pardir))


if __name__ == '__main__':
    command = "ls"
    # os.system(command)
    cur_dir = os.getcwd()
    home = home_dir()
    change_to_home = os.system(home)
    # print(change_to_home)
    # list_home_dir = os.system(change_to_home)


    d = os.getcwd()
    e = os.listdir(d)
    print(e)
