#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

# Should not change.
Suffix = "-1"

def setup():
    shelltools.system("pwd")
    # Inspect-0.8.0-linux-amd64.deb
    shelltools.system("ar xf Inspect-%s-linux-amd64.deb" % (get.srcVERSION()))
    shelltools.system("tar xvf data.tar.xz")

def install():
    pisitools.insinto("/", "opt")
    pisitools.insinto("/", "usr")
