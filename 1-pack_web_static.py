#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive\n

From the contents of the web_static folder.
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Generate a .tgz archive from the contents the web_static folder."""

    if not os.path.exists("versions"):
        os.makedirs("versions")

    now = datetime.now()
    archive_path = "versions/web_static-{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second)

    result = local("tar -cvzf {} web_static".format(archive_path))

    if result.failed:
        return None
    else:
        return archive_path
