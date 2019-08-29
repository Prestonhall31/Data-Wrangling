import xml.etree.cElementTree as ET
import pprint
from collections import defaultdict
import re
from pprint import pprint








lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')


d1 = defaultdict(int)
d2 = {'lower': {}, 'lower_colon': {}, 'problemchars': {}, 'other': {}}


# Count how many times each particular tag occurs
def key_count(d1, element):
    if element.tag == 'tag':
        d1[element.attrib['k']] += 1
    return d1


def process_map(filename):
    for _, element in ET.iterparse(filename):
        key_count(d1, element)
    return d1


# Sort 'k' attributes and their number of occurences by
#tag type('lower', 'lower_colon', 'problemchars' and 'other')
def sort_tags_d2(d1, d2):
    for key, value in d1.items():
        if lower.search(key):
            d2['lower'][key] = value
        elif lower_colon.search(key):
            d2['lower_colon'][key] = value
        elif problemchars.search(key):
            d2['problemchars'][key] = value
        else:
            d2['other'][key] = value
    return d2

# filter to see only the most common tags
def high_count_tags(d, threshold=150):
    l1 = []
    for key in d:
        if d[key] > threshold:
            l1.append((key, d[key]))
    l1.sort(key=lambda tup: tup[1], reverse= True)
    return l1



FILENAME = 'Beaverton.osm'

process_map(FILENAME)
#pprint.pprint(sort_tags_d2(d1,d2))
pprint(high_count_tags(d1))