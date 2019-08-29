#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Parse the XML file and count the numbers of unique tag
"""

import xml.etree.cElementTree as ET
import pprint


OSMFILE = "Beaverton.osm"

# Counts the unique amount of tags in the file
def count_tags(filename):
    tags = {}
    for event, elem in ET.iterparse(filename):
        if elem.tag in tags: 
            tags[elem.tag] += 1
        else:
            tags[elem.tag] = 1
    return tags
    
if __name__ == "__main__":
    pprint.pprint(count_tags(OSMFILE))

