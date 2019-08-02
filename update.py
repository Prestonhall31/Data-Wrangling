import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "Beaverton.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons"]

mapping = { "Ave": "Avenue", "Ave.": "Avenue", "avenue": "Avenue", "ave": "Avenue", "Blvd": "Boulevard", 
           "Blvd.": "Boulevard", "Blvd,": "Boulevard", "Boulavard": "Boulevard", "Boulvard": "Boulevard", 
           "Ct": "Court", "Dr": "Drive", "Dr.": "Drive", "Hwy": "Highway", "Ln": "Lane", "Ln.": "Lane", 
           "Pl": "Place", "Plz": "Plaza", "Rd": "Road", "Rd.": "Road", "St": "Street", "St.": "Street", 
           "st": "Street", "street": "Street", "square": "Square", "parkway": "Parkway"}


def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def update(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    update_name(tag.attrib['v'], mapping)
    osm_file.close()
    return street_types


def string_case(s): # change string into titleCase except for UpperCase
    if s.isupper():
        return s
    else:
        return s.title()


def update_name(name, mapping):
    name = name.split(' ')
    for i in range(len(name)):
        if name[i] in mapping:
            name[i] = mapping[name[i]]
            name[i] = string_case(name[i])
        else:
            name[i] = string_case(name[i])
    
    name = ' '.join(name)

    return name


if __name__ == '__main__':
    update(OSMFILE)