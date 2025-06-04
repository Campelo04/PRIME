from kivy.uix.screenmanager import Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder
from pymongo import MongoClient
import requests
API_URL = "http://127.0.0.1:8000/clientes/"
Builder.load_file('screens/clientes/clientes.kv') #Carrega o arquivo .kv

class FormCliente(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def novo_cliente(self,nome,cpf,endereco,telefone):
        API_URL = "http://127.0.0.1:8000/clientes/"
        try:
            response = requests.post(API_URL, json={"nome": nome, "cpf": cpf, "endereco": endereco, "telefone": telefone})
        except:
            return "Falha na cominicação.\nVerifique o seu funcionamento da API."
        return response.json()
    def limpar():
        from screens.clientes.clientes import Clientes
        Clientes.LimparQuadro()



class Clientes(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    def FormularioCliente(self):
        self.ids.quadro.add_widget(FormCliente())
    def LimparQuadro(self):
        self.ids.quadro.clear_widgets()
    @classmethod
    def limpar(cls):
        cls.LimparQuadro()



#conect_string = "mongodb://localhost:27017/"

class My_connection(MongoClient):
    def __init__(self, conect_string):
        self.cliente = self(conect_string) #Cliente acessa conexão indicada pela string
        self.db_connection = self.cliente["DGtech"] #Conexão é direcionada ao banco de dados existente
        print(self.db_connection)
        
    def collection(self,collection):
        self.collection = self.db_connection.get_collection(collection) 
        print(collection)

    

#My_connection.collection("Clientes")

c = Clientes()