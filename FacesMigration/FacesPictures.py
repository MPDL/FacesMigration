import pyimeji
import ntpath
import logging
import csv
import os

from pyimeji.api import Imeji

imeji = Imeji()
# Faces pictures
image_dir = "C:\Users\saquet\Pictures\high_resolution"
# Faces small videos

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
    for row in reader:
        if row["filename"] == filename:
            return [getEntryAsText(row, "emotion"),getEntryAsText(row, "age group"),getEntryAsText(row, "gender"),getEntryAsNumber(row, "age"),getEntryAsText(row, "picture group"),getEntryAsText(row, "person ID")]

def createItem(filename, collection):
    print "Create " + filename
    path = image_dir + "\\" + str(filename)
    item = imeji.create('item', collectionId=collection.id, _file=path, metadata=getMetadata(filename))

def createFacesCollection():
    collection = getCollection()
    files = getFiles()
    for f in files:
        createItem(f, collection)

def createPublicFacesCollection():
    collection = getCollection()
    files = getFiles()
    public = ["004", "066", "079", "116", "168", "140"]
    for f in files:
        if f.split("_")[0] in public:
            createItem(f, collection)

class FacesMigration():
   #createPublicFacesCollection()
   createFacesCollection()