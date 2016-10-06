from distutils.core import setup
from DistUtilsExtra.command import *
import glob
import re
import os

# look/set what version we have
changelog = "debian/changelog"
if os.path.exists(changelog):
    head=open(changelog).readline()
    match = re.compile(".*\((.*)\).*").match(head)
    if match:
        version = match.group(1)

setup(
    name = 'ubuntukylin-wallpapers',
    version = version,
    data_files=[('share/backgrounds', glob.glob('*.png')+glob.glob('*.jpg')),
		('share/backgrounds/ubuntukylin', glob.glob('ubuntukylin/*.xml')),
		('share/glib-2.0/schemas',glob.glob('*.override')),
               ],
    cmdclass = { "build" : build_extra.build_extra,
                 "build_i18n" :  build_i18n.build_i18n }
)

