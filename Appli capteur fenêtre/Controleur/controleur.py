from Vue.gestioncapteur import GestionCapteur
from Vue.associercapteur import AssocierCapteur
from Vue.referencercapteur import ReferenceCapteur
from Modele.gestioncapteur import ModeleGestionCapteur
from Modele.associercapteur import StructureLycée
from Modele.referencercapteur import ReferencerCapteur
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

class Controleur:
   
    def __init__(self,screenManager):
        
        self.screenManager=screenManager
        self.gestion_gestioncapteur=ModeleGestionCapteur(self)
        self.gestion_associercapteur=StructureLycée(self)
        self.gestion_referencercapteur=ReferencerCapteur(self)

    def set_ihm_gestioncapteur(self,ihm_gestioncapteur):
        self.ihm_gestioncapteur=ihm_gestioncapteur

    def set_ihm_associercapteur(self,ihm_associercapteur):
        self.ihm_associercapteur=ihm_associercapteur

    def set_ihm_referencecapteur(self,ihm_referencecapteur):
        self.ihm_referencecapteur=ihm_referencecapteur

    
    def retour_gestioncapteur(self):
        self.screenManager.current="gestioncapteur"

    def nouveau_capteur(self,id):
        self.ihm_gestioncapteur.afficher_ID(id)
        



    def change_ecran(self):
        self.screenManager.current="associercapteur"
        batiments = self.gestion_associercapteur.recupererListeBatiment()
        self.ihm_associercapteur.listeBatiment(batiments)
       
    def choix_batiment(self,batiment):

        #print(batiment)
        #todo
        etages = self.gestion_associercapteur.recupererListeEtage(batiment)  #appel modele pour récuperer etage
        self.ihm_associercapteur.listeEtage(etages)# complete spinner etage   
     

    def choix_etage(self, etage):

        salles = self.gestion_associercapteur.recupererListeSalle(etage)  #appel modele pour récuperer salle
        self.ihm_associercapteur.listeSalle(salles)   # complete spinner etage 

    def choix_salle(self, salle):
        self.ihm_associercapteur.afficher_message()
        



    def validation_reference(self):
        self.screenManager.current="referencecapteur"

    def recuperer_IDCapteur(self,id):
        self.ihm_associercapteur.recuperer_ID(id)

    def recuperer_donnees(self,batiment,etage,salle,idCapteur):
        print(batiment,etage,salle,idCapteur)
        self.gestion_referencercapteur.creerReference(batiment,etage,salle,idCapteur)

    def retour_reference(self,reference) :
        self.ihm_referencecapteur.afficher_Reference(reference)
        