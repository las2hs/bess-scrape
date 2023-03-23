import csv
import os
import xml.etree.ElementTree as ET
import sys

# Read the input file path from the command line argument
input_file = sys.argv[1]
output_file = os.path.splitext(input_file)[0] + ".xml"

# Create the root element of the XML tree
root = ET.Element("root")

# Read the input TSV file and create elements for each row
with open(input_file, "r", encoding="utf-8", newline="") as tsvfile:
    reader = csv.reader(tsvfile, delimiter="\t")
    for row in reader:
        # Create an element for the first item in the row
        element = ET.SubElement(root, row[0])
        element.text = "\n\t\t"
        element.tail = "\n\t"
        # Create a "textUnitReference" element and fill it with the second item in the row
        text_unit_ref = ET.SubElement(element, "textUnitReference")
        text_unit_ref.text = row[1]
        text_unit_ref.tail = "\n\t\t"
        # Create a "type" element and fill it with the remaining items in the row starting from index 2
        for item in row[2:]:
            if item: 
                type_elem = ET.SubElement(element, "type")
                type_elem.text = item
                type_elem.tail = "\n\t\t"

# Write the XML tree to a file
tree = ET.ElementTree(root)
tree.write(output_file, encoding="utf-8", xml_declaration=True)
