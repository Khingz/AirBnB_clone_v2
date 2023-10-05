#!/usr/bin/python3
"""Comment"""
from fabric.api import run, env, put, local
import os.path
import datetime

env.hosts = ['100.25.158.180', '100.26.253.232']


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


def do_deploy(archive_path):
    """Deploy a tar file"""
    if os.path.isfile(archive_path) is False:
        return False
    tgz_f = archive_path.split('/')[-1]
    dir_name = tgz_f.split('.')[0]
    if put(archive_path, "/tmp/{}".format(tgz_f)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/"
            .format(dir_name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/"
            .format(dir_name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(tgz_f, dir_name)).failed is True:
        return False
    if run("rm /tmp/{}".format(tgz_f)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/"
            .format(dir_name, dir_name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static"
            .format(dir_name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(dir_name)).failed is True:
        return False
    return True


def deploy():
    """Full deployment"""
    pack = do_pack()
    if pack is None:
        return False
    return do_deploy(pack)
