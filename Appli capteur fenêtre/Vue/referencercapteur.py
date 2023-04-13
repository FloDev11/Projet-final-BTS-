from kivy.uix.screenmanager import Screen
from kivy.clock import mainthread

class ReferenceCapteur(Screen):

    def __init__(self,controleur,**kwargs):    
        super().__init__(**kwargs)
        self.controleur=controleur

    def on_retour(self):
        self.controleur.retour_gestioncapteur()

    
    @mainthread

    def afficher_Reference(self,reference) :
        self.ids.reference.text = "La référence du nouveau capteur est "+reference