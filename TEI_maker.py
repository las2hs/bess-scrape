import sys
import xml.etree.ElementTree as ET

# Get the file name from the first command-line argument
file_name = sys.argv[1]

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

# Write the XML to standard output with each p element on its own line
tree.write('output.xml', encoding='utf-8', xml_declaration=True, method='xml')
