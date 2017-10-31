import aiml
import os
import sys
import io
import itertools as IT
import xml.etree.ElementTree as ET
print("Debug mode active...")
PY2 = sys.version_info[0] == 2
StringIO = io.BytesIO if PY2 else io.StringIO
with open('smallTalk.xml', 'r') as myfile:
    data=myfile.read() #.replace('\n', '')
def myfromstring(content):
    try:
        tree = ET.fromstring(content)
        print "No errors"
    except ET.ParseError as err:
        print "You have an error"
myfromstring(data)

