#!/usr/bin/python3
"""Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives"""
import os
from fabric.api import *
env.hosts = ['35.196.67.80', '34.73.69.148']


def do_clean(number=0):
    """
    Write a Fabric script (based on the file 3-deploy_web_static.py)
    that deletes out-of-date files, using the function do_clean
    """
    number = 1 if int(number) == 0 else int(number)

    files = sorted(os.listdir("versions"))
    [files.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in files]

    with cd("/data/web_static/releases"):
        files = run("ls -tr").split()
        files = [a for a in files if "web_static_" in a]
        [files.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in files]
