import hashlib
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder #Faz referencia ao arquivo .kv 
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
caminho = "classes/funcionarios.json"
from classes.funcionarios import Funcionario
import json
import time
from  classes.connection_db import My_connection


Builder.load_file('screens/login/login.kv') #Carrega o arquivo .kv

class Btn(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #-->> Possibilita modificar o alinhamento do texto no Objeto
        self.bind(size=self.setter('text_size')) 
        Window.bind(mouse_pos=self.on_mouseover)
        self.original = .35,0,0
        self.color_original = 1,1,1
    def on_mouseover(self, window, pos):
        if self.collide_point(*pos):
            self.background_color=1,.9,.9
            self.color=self.original
            self.bold=True
        else:
            self.background_color=self.original
            self.color=self.color_original
            self.bold=False

class Btn_yey(Btn):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image = "Images/closed_yey.png"
    def on_press(self):
        self.image = "Images/yey.png"
    def on_release(self):
        self.image = "Images/closed_yey.png"

class InfoTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.bind(size=self.setter('text_size'))
        Window.bind(mouse_pos=self.on_mouseover)
        self.aux = self.height
    def on_mouseover(self, window, pos):
        if self.collide_point(*pos):
            self.height =35
            self.size_hint_x =1.01
        else:
            self.size_hint_y =None
            self.height =33
            self.size_hint_x =1

class MensageLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(size=self.setter('text_size'))
    def destaque(self):
        self.color = 1,0,0,1
    def normal(self):
        self.color = 1,1,1,1
        
            
            
class InfoLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(size=self.setter('text_size'))
        Window.bind(mouse_pos=self.on_mouseover)
        self.original = 0,0,.3
        self.color_original = 0,0,.6
    def on_mouseover(self, window, pos):
        if self.collide_point(*pos):
            self.background_color=1,.9,.9
            self.color=self.original
            self.bold=True
        else:
            self.background_color=self.original
            self.color=self.color_original
            self.bold=False

class Login(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def bloquear(self):
        self.ids.senha_login.text = ""
        self.ids.resp_login.color = 0,0,.6
        self.ids.resp_login.text = f"Olá. Informe sua senha."
        self.manager.current = "login"
        
    def autenticar(self,user:str,password:str):
        funcionarios = []
        All_Hash = []
        with open(caminho,"r") as arquivo:
            dados = json.load(arquivo)
        for i in dados:
            funcionarios.append(Funcionario(**i))
            A = Funcionario(**i)
            print(f"Funcionário: {A.nome,A.senha}")
            All_Hash.append(A.senha)
        print(f"tabela de funcionários {A}")
        self.user = user
        self.password = password
        entrada =self.password+self.user
        # Calcula o hash SHA-256  
        hash_object = hashlib.sha256(entrada.encode())  
        print(f"\n\n Hash_object {hash_object} \n\n")
        hash_hex = hash_object.hexdigest()
        print(f"\n\n Hash_hex {hash_hex} \n\n")
        auth = False
        for i in All_Hash:
            if hash_hex== i: #"3b611308a72430139aad5183241d0a098daab9da8f08880153455caf4982fd0f":
                print("SUCCESS!! AU-TEN-TI-COOOUU!!!")
                self.ids.resp_login.text = f"Olá. Welcome!"
                self.ids.resp_login.color = 0,1,0
                self.manager.current = "gestao"
                auth = True
                break
            else:
                self.ids.resp_login.text = "Erro. Revise as informações de entrada."
                self.ids.resp_login.color = 1,.6,0
                self.ids.resp_login.destaque()
                print("FALHOU!")
        return auth
        #user_a = "Gabriel"
        #password_a = "123"
        #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        # 
        # print (self.user)
        # print("\n\n")
        # print(funcionarios)
        # 
        #     if self.user == i.nome and self.password == str(i.senha):
        #         print("AUTENTICOU")
        #         
        #         self.manager.current = "gestao"
        #         break
        #     else:
        #         
        # return auth
    #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    def check_password(self):
        if self.ids.senha_login.password:
            self.ids.senha_login.password = False
        else:
            self.ids.senha_login.password = True
    

