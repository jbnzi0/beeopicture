import os
import xml.etree.ElementTree as ET

dir = "Annotations"
annotation_file = os.path.join(dir, "%s.xml" % "05689")
objects = ET.parse(annotation_file).findall("object")

print(objects)