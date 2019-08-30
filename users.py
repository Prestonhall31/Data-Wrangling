#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
"""
This script will return the different amount of unique users
that have contributed to the map. 
"""

XMLFILE = "Beaverton.osm"

def get_user(element):
    uid = ''
    if element.tag == "node" or element.tag == "way" or element.tag == "relation":
        uid = element.get('uid')
    return uid

def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        if get_user(element):
            users.add(get_user(element))
            users.discard('')
        pass
    return len(users)

if __name__ == "__main__":
    pprint.pprint(process_map(XMLFILE))
