from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from classes.funcionarios import Funcionario
import json
caminho = "classes/funcionarios.json"

Builder.load_file('screens/funcionarios/funcionarios.kv') #Carrega o arquivo .kv

class Btn_Func(Button,BoxLayout):
    def __init__(self,pessoa = Funcionario, **kwargs):
        self.pessoa = pessoa
        super().__init__(**kwargs)
        #-->> Possibilita modificar o alinhamento do texto no Objeto
        self.bind(size=self.setter('text_size')) 
        self.color = 0,0,0

class FormFunc(BoxLayout):
    def __init__(self,pessoa = Funcionario, **kwargs):
        self.pessoa = pessoa
        super().__init__(**kwargs)

class Funcionarios(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        with open(caminho,"r") as arquivo:
            self.dados = json.load(arquivo)
        self.aux = []
    def cadastrar_funcionario(self):
        print("\n CADASTROOOOO!! \n")
        self.ids.func_list.add_widget(FormFunc())
    def show(self):
        try:
            self.ids.func_list.clear_widgets()
        except:
            print("A lista está vazia")
        for i in self.dados:
            p = Funcionario(**i)
            self.aux.append(i)
            self.ids.func_list.add_widget(FormFunc(p))        
        self.aux.append(self.__dict__)
        print(self.aux)