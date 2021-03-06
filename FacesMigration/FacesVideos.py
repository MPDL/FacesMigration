import pyimeji
import ntpath
import logging
import csv
import os

from pyimeji.api import Imeji

imeji = Imeji()

# Faces small videos
#image_dir = "C:\Users\saquet\Pictures\Faces\MP4SmallVideos"
# Faces videos
image_dir = "C:\Users\saquet\Pictures\Faces\MP4videos"

def getCollection():
    print("Get collection")
    return imeji.create('collection', title='Faces collection')

def getFiles():
    print("Get Files")
    return os.listdir(image_dir)

def getEntryAsText(dict, key):
    return {"index":key, "text":dict[key]}

def getEntryAsNumber(dict, key):
    return {"index":key, "number":int(dict[key])}

def getMetadata(filename):
    reader = csv.DictReader(open(image_dir + "\\Faces-collection.csv"))
    filename = os.path.splitext(filename)[0]
    image_filename = filename[0:8]  + filename[10]  + "_a"
    #print filename + " -> " + image_filename
    for row in reader:
        if row["filename"] == image_filename:
            return [getEntryAsText(row, "emotion"),getEntryAsText(row, "age group"),getEntryAsText(row, "gender"),getEntryAsNumber(row, "age"),getEntryAsText(row, "person ID")]

def createItem(filename, collection):
    print "Create " + filename
    path = image_dir + "\\" + str(filename)
    item = imeji.create('item', collectionId=collection.id, _file=path, metadata=getMetadata(filename))

def createFacesCollection():
    collection = getCollection()
    files = getFiles()
    for f in files:
        createItem(f, collection)

class FacesMigration():
   createFacesCollection()