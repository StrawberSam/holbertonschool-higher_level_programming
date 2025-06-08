#!/usr/bin/python3

"""
Module for serializing and deserializing Python dictionaries to and
from XML files.

Functions:
- serialize_to_xml(dictionary, filename): Saves a dictionary to an XML file.
- deserialize_from_xml(filename): Loads a dictionary from an XML file.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the file to write the XML data to.

    The function creates an XML structure with a root <data> element,
    and each key-value pair in the dictionary is added as a child element.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = value

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.

    Args:
        filename (str): The name of the XML file to read from.

    Returns:
        dict: A dictionary with keys and values extracted from the
        XML elements.

    Note:
        All values are returned as strings.
        Type conversion is not handled automatically.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result_dict = {}
    for child in root:
        result_dict[child.tag] = child.text

    return result_dict
