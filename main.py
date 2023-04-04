from xml.etree import ElementTree
import time, glob, sys, re, os
import xml.dom.minidom


def pico_xml_parse():
    xml_path = os.path.expanduser('~\\Desktop\\temp_gamelist.xml')  # Expand user starts in the user's folder.
    # xml = ElementTree.parse(xml_path)

    # grab the name of all the files
    # carts = glob.glob(os.path.expanduser('~\\testgamelistforpico8\\*'))
    carts = glob.glob(os.path.expanduser('~\\Desktop\\new carts\\*'))

    # - Create new XML document with its root element
    doc = xml.dom.minidom.parseString("<gameList/>")
    root = doc.documentElement

    # -----------------------------------------------------
    for cart in carts:
        cart_name = os.path.basename(cart)

        game_name = re.sub(r'\.p8.png$', '', cart_name)  # (r=raw string) (a,b,c) replace a with b in string c

        # game_name = os.path.splitext(cart_name)
        game = doc.createElement('game')
        # - Add new element to root
        root.appendChild(game)

        # - Create path element with text
        path = doc.createElement('path')
        path_text = doc.createTextNode(f'./carts/{cart_name}')
        path.appendChild(path_text)
        game.appendChild(path)

        # - Create name element with text
        path = doc.createElement('name')
        path_text = doc.createTextNode(game_name)
        path.appendChild(path_text)
        game.appendChild(path)

        # - Create image element with text
        path = doc.createElement('image')
        path_text = doc.createTextNode(f'./carts/{cart_name}')
        path.appendChild(path_text)
        game.appendChild(path)

    # prettify the xml
    xml_str = root.toprettyxml(indent="\t")
    # write the xml to the file
    print(xml_str)
    with open(xml_path, "w") as f:
        f.write(xml_str)

    # -----------------------------------------------------


if __name__ == '__main__':
    pico_xml_parse()