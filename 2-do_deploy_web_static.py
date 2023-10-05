#!/usr/bin/python3
"""Comment"""
from fabric.api import env
from fabric.api import put
from fabric.api import run
import os.path

env.hosts = ['100.25.158.180', '100.26.253.232']


def do_deploy(archive_path):
    """Deploy a tar file"""
    if os.path.isfile(archive_path) is False:
        return False
    f = archive_path.split("/")[-1]
    f_dir = f.split(".")[0]

    if put(archive_path, "/tmp/{}".format(f)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(f_dir)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(f_dir)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(f, f_dir)).failed is True:
        return False
    if run("rm /tmp/{}".format(f)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(
               f_dir,
               f_dir)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(f_dir)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(f_dir)).failed is True:
        return False
    return True
