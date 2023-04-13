from kivy.app import App

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from Controleur.controleur import Controleur
from Vue.gestioncapteur import GestionCapteur
from Vue.associercapteur import AssocierCapteur
from Vue.referencercapteur import ReferenceCapteur

class GestionCapteurApp(App):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)


	def build(self):

		self.screenManager= ScreenManager(transition=FadeTransition()) 		#Gestion des écrans avec ScreenManager
		self.controleur = Controleur(self.screenManager)					#appel le controleur

		self.ihm_gestioncapteur = GestionCapteur(self.controleur,name='gestioncapteur')			#appel la classe vue de GestionCapteur
		self.screenManager.add_widget(self.ihm_gestioncapteur)									#ajoute l'écran de gestioncapteur au screenmanager
		self.ihm_associercapteur = AssocierCapteur(self.controleur,name='associercapteur')		#appel la classe vue de AssocierCapteur
		self.screenManager.add_widget(self.ihm_associercapteur)									#ajoute l'écran de associercapteur au screenmanager
		self.ihm_referencecapteur = ReferenceCapteur(self.controleur,name='referencecapteur')			#appel la classe vue de GestionCapteur
		self.screenManager.add_widget(self.ihm_referencecapteur)									#ajoute l'écran de gestioncapteur au screenmanager

		self.controleur.set_ihm_gestioncapteur(self.ihm_gestioncapteur)			#lié le controleur de l'application à la vue gestioncapteur
		self.controleur.set_ihm_associercapteur(self.ihm_associercapteur)		#lié le controleur de l'application à la vue associercaapteur
		self.controleur.set_ihm_referencecapteur(self.ihm_referencecapteur)

		return self.screenManager


GestionCapteurApp().run()		#lancer l'application