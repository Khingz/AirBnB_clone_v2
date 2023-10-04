#!/usr/bin/python3
"""Comment"""
import datetime
from fabric.api import local, task


def do_pack():
    """Creates a tar file"""
    now = datetime.datetime.now()
    filen = "web_static_" + now.strftime('%Y%m%d%H%M%S')
    if local("mkdir -p versions").failed:
        return None

    result = local('tar -czvf versions/{}.tgz web_static'.format(filen))
    if result.succeeded:
        return "versions/{}.tgz".format(filen)
    return None
