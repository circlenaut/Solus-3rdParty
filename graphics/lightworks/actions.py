#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True

# Should not change.
Suffix = "-1"

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf lightworks_2021.2_r%s.deb" % (get.srcVERSION()))
    shelltools.system("tar xvf data.tar.xz")

def install():
    #pisitools.insinto("/", "opt")
    pisitools.insinto("/", "usr")