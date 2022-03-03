#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

# Should not change.
Suffix = "-1"

def setup():
    shelltools.system("pwd")
    # nice-dcv-viewer_2022.0.3929-1_amd64.ubuntu2004.deb
    shelltools.system("ar xf nice-dcv-viewer_2022.0.%s-1_amd64.ubuntu2004.deb" % (get.srcVERSION()))
    shelltools.system("tar xvf data.tar.xz")

def install():
    # pisitools.insinto("/", "opt")
    pisitools.insinto("/", "usr")
