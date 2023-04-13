from kivy.uix.screenmanager import Screen
from kivy.clock import mainthread

class AssocierCapteur(Screen):
    def __init__(self,controleur,**kwargs):    
        super().__init__(**kwargs)
        self.controleur=controleur

    def on_retour(self):
        self.controleur.retour_gestioncapteur()

    def on_validation_reference(self):
        self.controleur.validation_reference()
        self.controleur.recuperer_donnees(self.ids.batiment.text,self.ids.etage.text,self.ids.salle.text,self.ids.messageChoix.values)

       

    @mainthread  
    def listeBatiment(self,batiments):
        self.ids.batiment.values= batiments

    def listeEtage(self, etages):
        self.ids.etage.values= etages

    def listeSalle(self, salles):
        self.ids.salle.values= salles

    def on_retour_batiment(self):
       
        self.controleur.choix_batiment(self.ids.batiment.text)

    def on_retour_etage(self):
       
        self.controleur.choix_etage(self.ids.etage.text)

    def on_retour_salle(self):
       
        self.controleur.choix_salle(self.ids.salle.text)

    def afficher_message(self):
        self.ids.messageChoix.text="La sélection des choix est terminé,\nmodifier le si erreur, sinon valider en appuyant\nsur le bouton en bas à droite."

    def recuperer_ID(self, id):
        self.ids.messageChoix.values=id
        