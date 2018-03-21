import xml.etree.ElementTree as ET
import json

# URL: http://r-coreservice.mpdl.mpg.de:8080/ir/items?query=%22/properties/context/id%22=escidoc:40001&format=xml&maximumRecords=2052
xml = ET.parse("C:\Users\saquet\Pictures\Faces\eSciDoc-faces.xml")
# URL: https://qa-faces.mpdl.mpg.de/imeji/rest/collections/WJnSvIRC5oX4Aw4/items?offset=0&size=5000
json = json.load(open("C:\Users\saquet\Pictures\Faces\imeji-faces.json"))

imeji_dict={}
escidoc_dict={}

for item in json["results"]:
    imeji_dict[item["filename"]] = item["id"]


ns = {'escidocItem': 'http://www.escidoc.de/schemas/item/0.9',
      'zs': 'http://www.loc.gov/zing/srw/',
      'escidocComponents': 'http://www.escidoc.de/schemas/components/0.9'}

mapping = open('C:\Users\saquet\Pictures\Faces\mapping_filename_escidocid.txt','w')
for item in xml.findall('zs:records/zs:record/zs:recordData/escidocItem:item', ns):
    escidoc_id = item.get('{http://www.w3.org/1999/xlink}href').replace('/ir/item/', '')
    filename = item.find('escidocComponents:components/escidocComponents:component', ns).get('{http://www.w3.org/1999/xlink}title')[:11] + '.jpg'
    escidoc_dict[filename] = escidoc_id

imeji_path= "/imeji/collection/WJnSvIRC5oX4Aw4/item/"
faces_path= "/details/"

for escidoc in escidoc_dict.items():
    try:
        mapping.write("RedirectMatch " + faces_path + escidoc[1] + " " + imeji_path + imeji_dict[escidoc[0]] + "\n")
    except:
        print("Error for " + escidoc[0])

 # Map all album pages to the info page about albums
mapping.write("RedirectMatch /faces/album /static/albums.html \n")
# Map all other Faces url to the base url
mapping.write("RedirectMatch /faces/  /\n")
