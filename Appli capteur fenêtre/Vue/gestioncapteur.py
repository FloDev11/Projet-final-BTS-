from kivy.uix.screenmanager import Screen
from kivy.clock import mainthread

class GestionCapteur(Screen):

        def __init__(self,controleur,**kwargs):    
                super().__init__(**kwargs)
                self.controleur=controleur


        def on_change_ecran(self):
                self.controleur.change_ecran()

        @mainthread  
        def afficher_ID(self,id):
                self.ids.idCapteur.text="Nouveau capteur détecté : ID = "+id