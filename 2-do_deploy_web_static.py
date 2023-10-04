#!/usr/bin/python3
"""Comment"""
from fabric.api import sudo, env, put
import os.path

env.hosts = ['100.25.158.180', '100.26.253.232']


def do_deploy(archive_path):
    """Deploy a tar file"""
    if os.path.isfile(archive_path) is False:
        return False
    tgz_f = archive_path.split('/')[1]
    dir_name = tgz_f.split('.')[0]
    if put(archive_path, "/tmp/{}".format(tgz_f)).failed is True:
        return False
    if sudo("rm -rf /data/web_static/releases/{}/"
            .format(dir_name)).failed is True:
        return False
    if sudo("mkdir -p /data/web_static/releases/{}/"
            .format(dir_name)).failed is True:
        return False
    if sudo("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(tgz_f, dir_name)).failed is True:
        return False
    if sudo("rm /tmp/{}".format(tgz_f)).failed is True:
        return False
    if sudo("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/"
            .format(dir_name, dir_name)).failed is True:
        return False
    if sudo("rm -rf /data/web_static/releases/{}/web_static"
            .format(dir_name)).failed is True:
        return False
    if sudo("rm -rf /data/web_static/current").failed is True:
        return False
    if sudo("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(dir_name)).failed is True:
        return False
    return True
