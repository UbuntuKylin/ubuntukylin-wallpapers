#!/usr/bin/env python3
# coding=utf-8

import glob
#########################生成ubuntukylin/*.xml#####################################
PREAMBLE = """<background>
  <starttime>
    <year>2009</year>
    <month>08</month>
    <day>04</day>
    <hour>00</hour>
    <minute>00</minute>
    <second>00</second>
  </starttime>
<!-- This animation will start at midnight. -->
"""

ENTRY = """  <static>
    <duration>300</duration>
    <file>%(a)s</file>
  </static>
  <transition>
    <duration>5.0</duration>
    <from>%(a)s</from>
    <to>%(b)s</to>
  </transition>
"""

FOOTER = """</background>
"""
###################################################################################

##################################生成*.xml.in#####################################
#########需要修改17.04    zesty.xml
Y_PREFIX_XML_IN = """<?xml version="1.0"?>
<!DOCTYPE wallpapers SYSTEM "gnome-wp-list.dtd">
<wallpapers>
 <wallpaper deleted="false">
   <name>Ubuntu 17.10 Community Wallpapers</name>
   <filename>/usr/share/backgrounds/ubuntukylin/bionic.xml</filename>
   <options>zoom</options>
 </wallpaper>
"""

Y_BODY_XML_IN = """ <wallpaper>
     <_name>%(c)s</_name>
     <filename>%(d)s</filename>
     <options>zoom</options>
     <pcolor>#000000</pcolor>
     <scolor>#000000</scolor>
     <shade_type>solid</shade_type>
 </wallpaper>
"""
Y_FOOTER = """</wallpapers>
"""
###################################################################################

##################################修改PO#########################################
#####修改Y_PO中的artful
Y_PO = """#: ../bionic-ubuntukylin-wallpapers.xml.in.h:%(e)d
msgid "%(f)s"
msgstr ""

"""
#################################################################################

PATH='/usr/share/backgrounds/'
UNKNOWN_XML = open("bionic.xml", 'w+')
UNKNOWN_XML_IN = open("bionic.xml.in", 'w+')
UNKNOWN_POT = open("bionic.pot", 'w+')

def main():
    images = glob.glob('*.jpg')
    m = len(images)

    output = ''
    output += PREAMBLE
    y_output_xmlin = ''
    y_output_xmlin += Y_PREFIX_XML_IN
    y_output_po = ''
    for i in xrange(m):
        output += ENTRY % {'a': PATH + images[i], 'b': PATH + images[(i+1) % m]}
	y_imagename = images[i].capitalize().replace("-"," ",5)[:-4];
        y_output_xmlin += Y_BODY_XML_IN % {'c': y_imagename, 'd': PATH + images[(i) % m]}
	y_output_po += Y_PO % {'e': i+1, 'f': y_imagename}
    output += FOOTER
    y_output_xmlin += Y_FOOTER
    print >> UNKNOWN_XML, output
    print >> UNKNOWN_XML_IN, y_output_xmlin
    print >> UNKNOWN_POT, y_output_po

if __name__ == '__main__':
    main()
