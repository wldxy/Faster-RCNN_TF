import xml.etree.ElementTree as ET
import os

os.chdir("Ann")
os.chdir("n02876657")

for i in os.listdir("."):
    
    tree = ET.parse(i)
    objs = tree.findall('object')

    for ix, obj in enumerate(objs):
        bbox = obj.find('bndbox')
        # Make pixel indexes 0-based
        x1 = float(bbox.find('xmin').text)
        y1 = float(bbox.find('ymin').text)
        x2 = float(bbox.find('xmax').text)
        y2 = float(bbox.find('ymax').text)
        print x1, y1, x2, y2