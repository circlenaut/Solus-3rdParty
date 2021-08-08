#!/usr/bin/python

# Change with each release
srcSubVersion = 1623937013

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True

# Should not change.
Suffix = "-1"

SUBVERSION = 1628120042

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf code_%s-%s_amd64.deb" % (get.srcVERSION(), str(SUBVERSION)))
    shelltools.system("tar xvf data.tar.xz")

def install():
    pisitools.insinto("/", "usr")
