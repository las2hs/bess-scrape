import sys
import os
import xml.etree.ElementTree as ET

# Get the file name from the first command-line argument
file_name = sys.argv[1]

# Get the file name without the extension
file_base = os.path.splitext(file_name)[0]

# Read the contents of the file
with open(file_name, 'r') as f:
    contents = f.read()

# Split the contents into paragraphs
paragraphs = contents.split('\n')

# Create the root element
root = ET.Element('root')

# Add each paragraph as a <p> element with an 'n' attribute
for i, para in enumerate(paragraphs):
    p = ET.SubElement(root, 'p', {'n': str(i+1)})
    p.text = para.strip()

    # Add a newline after each <p> element
    if i != len(paragraphs) - 1:
        p.tail = '\n'

# Create the XML tree
tree = ET.ElementTree(root)

# Write the XML to a file with the same name as the input file, with "_TEI" added to the end
output_file_name = file_base + '_TEI.xml'
tree.write(output_file_name, encoding='utf-8', xml_declaration=True, method='xml')
