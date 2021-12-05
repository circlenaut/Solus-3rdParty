#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

# Should not change.
Suffix = "-1"

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf nordvpn_%s-1_amd64.deb" % (get.srcVERSION()))
    shelltools.system("tar xvf data.tar.gz")

def install():
    pisitools.insinto("/", "etc")
    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "var")