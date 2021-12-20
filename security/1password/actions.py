#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

# Should not change.
Suffix = "-1"

target_version = "1password-%s.x64" % get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("tar xvf 1password-%s.x64.tar.gz" % get.srcVERSION())

def install():
    pisitools.insinto("/opt/1Password/", "1password-%s.x64/*" % get.srcVERSION() )
    pisitools.insinto("/usr/share/applications/", "1password-%s.x64/resources/1password.desktop" % get.srcVERSION() )
    pisitools.insinto("/usr/share/icons/hicolor/", "1password-%s.x64/resources/icons/hicolor/*" % get.srcVERSION() )
