import itertools as _itertools
import traceback as _traceback
import xml.etree.ElementTree as _ET
from xml.etree.ElementTree import ParseError as _xml_error

XML_PATH = './pspec.xml'

flatten = _itertools.chain.from_iterable


class XMLError(Exception):
    '''raise this when there's an Exception pulling configs'''
        

def get_subversion(xmlfile):
    tree = _ET.parse(xmlfile)
    root = tree.getroot()
    latest_version = max([item.attrib['release'] for item in root.findall('./History/Update')])
    return list(flatten([[child.text for child in item if child.tag == 'SubVersion'] for item in root.findall('./History/Update') if item.attrib['release'] == latest_version]))[0]
    
    

try:
    sub_version= get_subversion(XML_PATH)
except _xml_error as err:
    raise XMLError(f"Invalid format '{XML_PATH}': {err}")