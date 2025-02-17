#!/usr/bin/python3
"""
modulo
"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    
    tree = ET.ElementTree(root)
    tree.write(filename, xml_declaration=True)

def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        return {child.tag: child.text for child in root}
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except ET.ParseError:
        print(f"Error: Failed to parse XML from '{filename}'.")
        return None
