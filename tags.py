"""
Count multiple patterns in the tags
"""

import xml.etree.cElementTree as ET
import pprint
import re

from collections import defaultdict

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

OSMFILE = "Beaverton.osm"

# 
def key_type(element, keys):
    '''
    This function utilizes regex to pull all the tags in the file and 
    count the occurences of types of tags to estimate how many different 
    types of tags there are and how many potectial problems there could be
    Args:
        element(string): element in the file. 
        keys(dictionary): Dictionary used to keep count of elements.
    Returns:
        Dictionary: the keys
    '''
    if element.tag == "tag":
        for tag in element.iter('tag'):
            k = tag.get('k')
            if lower.search(element.attrib['k']):
                keys['lower'] = keys['lower'] + 1
            elif lower_colon.search(element.attrib['k']):
                keys['lower_colon'] = keys['lower_colon'] + 1
            elif problemchars.search(element.attrib['k']):
                keys['problemchars'] = keys['problemchars'] + 1
            else:
                keys['other'] = keys['other'] + 1
                
    return keys

# Counts the different tags in the file. 
def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys

if __name__ == "__main__":
    pprint.pprint(process_map(OSMFILE))
