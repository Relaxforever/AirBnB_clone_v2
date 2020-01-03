#!/usr/bin/python3
""" Leave this place Nerevar, only death awaits """
from fabric.api import local
from datetime import datetime as dt


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
