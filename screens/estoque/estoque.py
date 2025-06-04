from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('screens/estoque/estoque.kv') #Carrega o arquivo .kv

class Estoque(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)