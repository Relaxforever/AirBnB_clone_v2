#!/usr/bin/python3
""" Leave this place Nerevar, only death awaits """
from fabric.api import local, put, run
from datetime import datetime as dt
from os import path


def do_pack():
    """ this script will only bring destruction Nerevar """

    local("mkdir -p versions")
    current = dt.now()
    current = current.now()
    tgz = "web_static_{}.tgz".format(current.strftime("%Y%m%d%H%M%S"))
    working = local("tar -cavf versions/{} web_static".format(tgz))

    if working.failed:
        return None
    else:
        return tgz


def do_deploy(archive_path):
    """ distributes an archive to the web servers """
    if archive_path is None:
        return False
    noexten = path.splitext(archive_path)[0]
    try:
        put(archive_path, "tmp")
        run("mkdir -p /data/web_static/releases/{}/".format(noexten))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(archive_path, noexten))
        run("rm /tmp/{}".format(archive_path))
        run("mv /data/web_static/releases/{}/web_static/*  /data/web_static/releases/{}/".format(noexten, noexten))
        run("rm -rf /data/web_static/releases/{}/web_static".format(noexten))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(noexten))
        return True
    except:
        return False