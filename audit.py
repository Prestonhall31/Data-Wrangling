#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "small-sample.osm"

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons", "Way", "Terrace", "Loop", "Highway", "Circle"]

''' Audit Street names '''
def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

def count_street_type(street_type_count, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        street_type_count[street_type] +=1
    else:
        street_type_count[street_name] +=1


def group_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        street_types[street_type].add(street_name)
    else:
    	street_types[street_name].add(street_name)


def sort_values(street_type_count):
	sorted_counts = []
	d_view = [(v,k) for k,v in street_type_count.items()]
	d_view.sort(reverse=True) # natively sort tuples by first element
	for v,k in d_view:
		sorted_counts.append("%s: %d" % (k,v))
	return sorted_counts


''' Audit postcode '''
postcode_re = re.compile(r'^\d{5}$')


expected = ['97005', '97007', '97975','97977', '97225','97006', '97008', '97076', '97223', '97229']


def audit_postcode(bad_postcodes, postcode):
	m = postcode_re.search(postcode)
	if m:
		postcode = m.group()
		if postcode not in expected:
			bad_postcodes[postcode] +=1
	else:
		bad_postcodes[postcode] +=1


def is_postcode(elem):
	return (elem.attrib['k'] == 'addr:postcode')


''' Audit phone numbers '''
phone_re = re.compile(r'^\+49\s\d{3}\s\d{6,8}$')


def audit_phone(phone_types, number):
	good_format = phone_re.search(number)
	if not good_format:
		phone_types.add(number)


def is_phone_number(elem):
	return (elem.attrib['k'] == 'phone')


# Iterates through the Street values and returns the words that are not in the expected list
def audit(osmfile):
    osm_file = open(osmfile, "r")

    phone_types = set()
    bad_postcodes = defaultdict(int)
    street_type_count = defaultdict(int)
    street_types = defaultdict(set)
    
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                	count_street_type(street_type_count, tag.attrib['v'])
                	group_street_type(street_types, tag.attrib['v'])
                if is_phone_number(tag):
                	audit_phone(phone_types,tag.attrib['v'])
                if is_postcode(tag):
                	audit_postcode(bad_postcodes, tag.attrib['v'])
    osm_file.close()

    street_type_count = sort_values(street_type_count)

    return phone_types, street_type_count, street_types, bad_postcodes



if __name__ == "__main__":
    pprint.pprint(audit(OSMFILE))

'''
# perform all of the above audits on the file

def audit(osmfile):
    osm_file = open(osmfile, "r")

    phone_types = set()
    bad_postcodes = defaultdict(int)
    street_type_count = defaultdict(int)
    street_types = defaultdict(set)
    
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                	count_street_type(street_type_count, tag.attrib['v'])
                	group_street_type(street_types, tag.attrib['v'])
                if is_phone_number(tag):
                	audit_phone(phone_types,tag.attrib['v'])
                if is_postcode(tag):
                	audit_postcode(bad_postcodes, tag.attrib['v'])
    osm_file.close()

    street_type_count = sort_values(street_type_count)

    return phone_types, street_type_count, street_types, bad_postcodes
'''