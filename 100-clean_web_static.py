#!/usr/bin/python3
"""Clean up old archives and releases in the web_static deployment."""
import os
from fabric.api import env, run, sudo, lcd, local, cd

env.hosts = ["54.83.130.108", "100.26.20.141"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_clean(number=0):
    """
    Clean up old archives and releases in the web_static deployment.

    Args:
        number (int): The number of archives and releases to keep.
            If not provided or 0, it keeps 1 archive and release.
    """
    nbr = 1 if int(number) == 0 else int(number)
    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(nbr)]
    with lcd("versions"):
        [local("rm ./{}".format(file)) for file in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [file for file in archives if "web_static_" in file]
        [archives.pop() for i in range(nbr)]
        [sudo("rm -rf ./{}".format(file)) for file in archives]
