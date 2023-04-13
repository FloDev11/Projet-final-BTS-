import paho.mqtt.client as mqttclient

import json


class ModeleGestionCapteur:

    def __init__(self,controleur):
        self.controleur=controleur
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
        print("***Connexion MQTT***")
        
        self.client_mqtt.subscribe([("zigbee2mqtt/bridge/event",2)])
        self.client_mqtt.on_message=self.onMessageMQTT
    
    
    def onDisConnectMQTT(self,client, userdata, message):
        print("**DECO MQTT***",message)
    

    
    def onMessageMQTT(self,client, userdata, msg):
        print("***MQTT MESSAGE***")
        #print(msg.payload)
        try: 
            m_decode=str(msg.payload.decode("utf-8","ignore"))
            m_in=json.loads(m_decode) #decode json data
    
            #print(m_in)
            type=m_in["type"]
            if type=="device_joined":
                #print(type)
                id=m_in["data"]["ieee_address"]
                #print(id)
                self.identifiantCapteur=id
                self.controleur.nouveau_capteur(self.identifiantCapteur)
                self.controleur.recuperer_IDCapteur(self.identifiantCapteur)
                

        except:
            print("Accueil ERREUR MESSAGE MQTT")