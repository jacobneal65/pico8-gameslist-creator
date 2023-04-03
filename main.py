from xml.etree import ElementTree
import time, glob, sys, re, os


def pico_xml_parse():
    print("begin xml parse:")
    xml_path = os.path.expanduser('~\\Desktop\\gamelist.xml') #Expand user starts in the user's folder.
    xml = ElementTree.parse(xml_path)
    for game in xml.findall('game'):
        image = game.findtext('image')



if __name__ == '__main__':
    pico_xml_parse()

# <?xml version="1.0"?>
# <game>
# 		<path>./carts/ascent-0.p8.png</path>
# 		<name>Ascent</name>
# 		<image>./carts/ascent-0.p8.png</image>
# 		<desc>Crashed on a desolate but mysterious planet you find yourself eye to eye with an ancient civilisation.
# 			Explore the planet, find powerful upgrades, and uncover its secrets.
#
# 			CONTROLS
# 			move keys
# 			jump o
# 			special moves x
# 		</desc>
# 		<genre>Platformer</genre>
# 		<lang>en</lang>
# </game>


