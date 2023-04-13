from matplotlib.font_manager import json_dump
import paho.mqtt.client as mqttclient

import json


class ReferencerCapteur:

    def __init__(self,controleur):
        self.controleur=controleur
        self.connected = False
        self.init_mqtt()
        

    def init_mqtt(self):
        try:
            self.client_mqtt=mqttclient.Client("",clean_session=True)
            self.client_mqtt.on_connect= self.onConnectMQTT
            self.client_mqtt.on_disconnect= self.onDisConnectMQTT
            self.client_mqtt.username_pw_set("test",password="test")
            self.client_mqtt.connect("127.0.0.1")
            self.client_mqtt.loop_start()
        except:
            print("Erreur Connect MQTT")

    def onConnectMQTT(self,client, userdata, flags, rc):
        print("***Connexion MQTT PUBLISH***")
        self.connected = True
        
    
    
    def onDisConnectMQTT(self,client, userdata, message):
        print("**DECO MQTT***",message)
        self.connected =False


    def creerReference(self,batiment,etage,salle,idCapteur):
        reference = batiment + etage + salle
        payload = {"from": "" , "to" : ""}

        payload ["from"]= idCapteur
        payload ["to"]= reference
        payload_json = json.dumps(payload)

        try:
            self.client_mqtt.publish("zigbee2mqtt/bridge/request/device/rename", payload_json, retain=True)
            self.controleur.retour_reference(reference)
            print("***MESSAGE MQTT PUBLIEE***")
        except:
            print("***ERREUR MESSAGE MQTT ***")
        
        