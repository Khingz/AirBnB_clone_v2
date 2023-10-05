#!/usr/bin/python3
"""Comment"""
import os
from fabric.api import *

env.hosts = ['100.25.158.180', '100.26.253.232']


def do_clean(number=0):
    """Function comment"""
    number = int(number)
    if (number) == 0:
        number = 1

    files = sorted(os.listdir("versions"))
    print(files)
    for _ in range(number):
        files.pop()

    with lcd("versions"):
        for f in files:
            local("rm ./{}".format(f))

    with cd("/data/web_static/releases"):
        files = run("ls -tr").split()
        filtered_files = []
        for f in files:
            if "web_static_" in f:
                filtered_files.append(f)
        for _ in range(number):
            filtered_files.pop()
        for f in filtered_files:
            run("rm -rf ./{}".format(f))
