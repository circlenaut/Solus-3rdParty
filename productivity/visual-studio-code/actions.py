#!/usr/bin/python

import os as _os
import sys as _sys
import itertools as _itertools
import traceback as _traceback
import xml.etree.ElementTree as _ET
from xml.etree.ElementTree import ParseError as _xml_error

#print(_os.getcwd())
#print(_sys.path[0])
#root_path = _os.path.dirname(_os.getcwd())
#print(root_path)


XML_PATH = './pspec.xml'

XML_FILE = 'metadata.xml'

flatten = _itertools.chain.from_iterable


class XMLError(Exception):
    '''raise this when there's an Exception pulling configs'''
        

def get_subversion(xmlfile):
    tree = _ET.parse(xmlfile)
    root = tree.getroot()
    print(root)
    latest_version = max([item.attrib['release'] for item in root.findall('./Package/History/Update')])
    #latest_version = [item.tag for item in root.findall('./Package/History/Update')]
    print(latest_version)
    test = [[child.tag for child in item] for item in root.findall('./Package/History/Update')]
    print(test)
    return list(flatten([[child.text for child in item if child.tag == 'SubVersion'] for item in root.findall('./Package/History/Update') if item.attrib['release'] == latest_version]))[0]

from pisi.actionsapi import get, pisitools, shelltools


NoStrip = ["/usr"]
IgnoreAutodep = True

# Should not change.
Suffix = "-1"

# Change with each release
SUBVERSION = 1646927742

def test_cmd(cmd):
    xml_path = _os.path.join(cmd, 'metadata.xml')
    print(xml_path)
    sub_version= get_subversion(xml_path)
    print(sub_version)
    try:
        sub_version= get_subversion(xml_path)
        print(sub_version)
    except _xml_error as err:
        raise XMLError("Invalid format '{}': {}".format(xml_path, err))
    return sub_version
#    return xml_path


# Created For Solus Operating System    
    
    return 

def setup():
    shelltools.system("pwd")
#    print('dir: '.format(get.pkgDIR()))
#    shelltools.system(get.pkgDIR)
#    shelltools.system("pkg_dir" % (get.pkgDIR))
    shelltools.system("ar xf code_%s-%s_amd64.deb" % (get.srcVERSION(), str(SUBVERSION)))
#    shelltools.system("ar xf code_%s-%s" % (get.srcVERSION(), test_cmd(get.pkgDIR())))
    shelltools.system("tar xvf data.tar.xz")

def install():
    pisitools.insinto("/", "usr")
