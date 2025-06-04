from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('screens/relatorios/relatorios.kv') #Carrega o arquivo .kv

class Relatorios(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)