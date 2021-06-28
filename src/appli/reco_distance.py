from imutils import paths
import numpy as np
import imutils
import cv2
import sqlite3
import matplotlib.pyplot as plt
DATABASE = "../../bdd/project.db"

def getdb():
    #get information from database
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db
def getdirection():
    #trouve la direction vers laquelle l'appareil est pointé
    return 0
def gps():
    #retourne les infos du gps (direction distance pour chaque etape etc) type liste
    return [-1,0]
def findcanny(image):
    gray=cv2.cvtColor(image,cv2.COLOR_BG2GRAY)
    gray=cv2.GaussianBlur(gray,cv2.COLOR_BG2GRAY)
    edged=cv2.Canny(gray,35,125)
    cnts=cv2.findContours(edged.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    cnts=cv2.imutils.grab_contours(cnts)
    #trouver l'horizon???
    return edged	
def roadmarkerfind(image):
    """prend en argument une image et retourne les marqueurs l'inclinaison estimée à partir des données fournies par un fichier csv .xls contenant les données régularisé des marqueurs de route d'un pays.
    """
    return findcanny(image)
def squarify():
    #va peut etre s'appeler triangify si on utilise dans le futur des triangles au lieux des carre, mais vectorise l'image et la decoupe en plusieurs parties et surimpose les couches
    return
def markertoemptyspaceratio(image,country=None,city=None,street=None):
    #prend en argument une image et un pays/ville/rue permet de déterminer a partir des ratios des marqueur le type de marqueur present
    if country:
        db=getdb()
    return
def reco_distance(image):
    #prend en argument une image sous format png ou autre et retourne la distance entre la caméra et l'objet déterminé
    LGPS=gps()
    direction=getdirection()
    if LGPS[0]==direction:
        marker=roadmarkerfind(image)
    return



