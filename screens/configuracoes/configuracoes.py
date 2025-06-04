from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('screens/configuracoes/configuracoes.kv') #Carrega o arquivo .kv

class Configuracoes(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)