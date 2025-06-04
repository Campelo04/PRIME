from kivy.uix.screenmanager import Screen
from kivy.lang import Builder #Faz referencia ao arquivo .kv 
from decimal import Decimal
dec = Decimal()
Builder.load_file('screens/gestao/gestao.kv') #Carrega o arquivo .kv
class Gestao(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)