from tkinter import W
from urllib import request,parse
import json


class StructureLycée:

    def __init__(self,controleur):
        self.controleur=controleur
        

    def recupererListeBatiment (self):          #méthode permettant de récupérer la liste des bâtiments de l'établissement
  
        listeBatiment = request.urlopen("http://127.0.1.1/requeteBDD_batiment.php").read()          
        m_in = str(listeBatiment.decode("utf8","ignore"))  
        #print(m_in)
        resultatjson=json.loads(m_in) #decode json data
        #print(resultatjson)
        batiments = []
        for bat in resultatjson["batiments"] :
            #print(bat['NomBatiment'])
            batiments.append(bat["NomBatiment"])
        
        return batiments

    def recupererListeEtage (self, batimentChoisi):


        choixBatiment= parse.urlencode({"NomBatiment":batimentChoisi})
        listeEtage = request.urlopen("http://127.0.1.1/requeteBDD_etage.php/get?{}".format(choixBatiment)).read()
        m_in = str(listeEtage.decode("utf8","ignore"))
        resultatjson=json.loads(m_in) #decode json data
        #print(resultatjson)
        etages = []
        for eta in resultatjson["etages"] :
    
            etages.append(eta["NumEtage"])
        
        #print (etages)
        return etages


    def recupererListeSalle (self, etageChoisi):

        choixEtage= parse.urlencode({"NumEtage":etageChoisi})
        listeSalle = request.urlopen("http://127.0.1.1/requeteBDD_salle.php/get?{}".format(choixEtage)).read()
        m_in = str(listeSalle.decode("utf8","ignore"))
        resultatjson=json.loads(m_in) #decode json data
        #print(resultatjson)
        salles = []
        for sal in resultatjson["salles"] :
    
            salles.append(sal["NumSalle"])
        
        #print (salles)
        return salles