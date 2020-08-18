#!/usr/bin/python3
"""module"""
from datetime import datetime
from fabric.api import *
from os.path import isdir


def do_pack():
    """ Write a Fabric script that generates a .tgz archive from the
    contents of the web_static """
    date = datetime.now()
    archive = "versions/web_static_{}{}{}{}{}{}.tgz"\
              .format(date.year, date.month, date.day, date.hour,
                      date.minute, date.second)
    if isdir("versions") is False:
        local("mkdir versions")
    print("Packing web_static to {}".format(archive))
    result = local("tar -vczf {} web_static".format(archive))
    if result.succeeded:
        return (archive)
    else:
        return None
