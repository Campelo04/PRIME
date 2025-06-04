from kivy.app import App
from kivy import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen,FadeTransition
from pynput.keyboard import Key, Controller
keyboard = Controller()
from screens.login.login import Login
from screens.pedidos.pedidos import Pedidos
from screens.gestao.gestao import Gestao
from screens.clientes.clientes import Clientes
from screens.clientes.clientes import FormCliente
from screens.relatorios.relatorios import Relatorios
from screens.funcionarios.funcionarios import Funcionarios
from screens.estoque.estoque import Estoque
from screens.configuracoes.configuracoes import Configuracoes

Config.set('input', 'mouse', 'mouse,disable_multitouch') #quando se usa o botão auxiliar do mouse surge uma bolinha vermelha a cada click, está linha desabilita isso
Config.set('kivy','exit_on_escape','0') #Desabilita o fechamento do programda pela tecla "ESC"

#from kivy.lang import Builder #Faz referencia ao arquivo .kv 

#Builder.load_file('main.kv') #Carrega o arquivo .kv

class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def LimparQuadro(self):
        self.ids.quadro.clear_widgets()

class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        self.transition = FadeTransition(duration=2)
        super().__init__(**kwargs)
    
class Main(App):
    def build(self):
        self.title = "Dias Gomes tecnologia - PDV"
        self.dg_font_size_text = "12"
        self.dg_font_size_subtitle = 14
        self.dg_font_size_title = 16
        self.background_full = "#b5c5c5"
        self.black_1 = "#0f0f0f"
        with keyboard.pressed(Key.cmd_l):
            keyboard.press(Key.left)
            keyboard.release(Key.left)
        return MyBoxLayout()

Main().run()

