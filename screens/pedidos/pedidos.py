from kivy.lang import Builder #Faz referencia ao arquivo .kv 
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.spinner import Spinner,SpinnerOption
from kivy.uix.dropdown import DropDown
import requests
from datetime import datetime

API_URL = "http://127.0.0.1:8000/clientes/"

Builder.load_file("screens/pedidos/pedidos.kv") #Carrega o arquivo .kv

class Pedido():
    def __init__(self, id, codigo, id_cliente, id_funcionario, itens, origem="", valor="", abertura="", fechamento="", estado="", obs="", **kwargs):
        self.id = id
        self.codigo = codigo 
        self.id_cliente = id_cliente 
        self.id_funcionario = id_funcionario
        self.itens = itens
        self.origem = origem
        self.valor = valor 
        self.abertura = abertura
        self.fechamento = fechamento
        self.estado = estado
        self.obs = obs


class Produto():
    def __init__(self, id, codigo, categoria, nome, valor, descr="", **kwargs):
        self.id = id 
        self.codigo = codigo
        self.categoria = categoria
        self.nome = nome
        self.valor = valor
        self.descr = descr

class Btn(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #-->> Possibilita modificar o alinhamento do texto no Objeto
        self.bind(size=self.setter('text_size')) 
        Window.bind(mouse_pos=self.on_mouseover)
        self.original = .35,0,0
        self.color_original = 1,1,1
    def on_mouseover(self, window,*pos):
        if self.collide_point(*pos):
            self.background_color=1,.9,.9
            self.color=self.original
            self.bold=True
            print(f"{self.collide_point} \n soma {self.collide_point+[0,100]}")
        else:
            self.background_color=self.original
            self.color=self.color_original
            self.bold=False

class Btn_Item(Button,BoxLayout): #,
    def __init__(self, categoria, id, nome, valor,**kwargs):
        self.categoria = categoria
        self.id = id
        self.nome = nome
        self.valor = valor
        super().__init__(**kwargs)
        #-->> Possibilita modificar o alinhamento do texto no Objeto
        self.bind(size=self.setter('text_size')) 
        self.color = 0,0,0
    def printar_id(self, id):
        self.id = id
        print(f"Aqui o ID, doido! {self.id}")
    def editar_pedido(self, pedido_id, codigo, id_cliente, id_funcionario, itens, origem, valor, obs):
        API_URL = "http://127.0.0.1:8000/pedidos/"
        try:    
            response = requests.put(f"{API_URL}{pedido_id}", json={"codigo":codigo, "id_cliente": id_cliente, "id_funcionario":id_funcionario, "itens":itens, "origem":origem, "valor":valor, "obs":obs})
        except:
            return "Falha na cominicação.\nVerifique o seu funcionamento da API."
        return response.json()
    
class Btn_Pedido(Button,BoxLayout):
    def __init__(self, id, codigo, id_cliente, id_funcionario, itens, origem, valor, abertura, fechamento, estado, obs, **kwargs):
        self.id = id
        self.codigo = codigo 
        self.id_cliente = id_cliente 
        self.id_funcionario = id_funcionario
        self.itens = itens
        self.origem = origem
        self.valor = valor 
        self.abertura = abertura
        self.fechamento = fechamento
        self.estado = estado
        self.obs = obs
        super().__init__(**kwargs)
        #-->> Possibilita modificar o alinhamento do texto no Objeto
        self.bind(size=self.setter('text_size')) 
        self.color = 0,0,0
    def minha_cor(self,estado):
        match estado:
            case "Finalizado":
                return "#10ff10"
            case "Entregue/servido":
                return "#00BFFF"
            case "Em produção":
                return "#FF8C00"
            case _:
                return "#d5d5d5"
            

    def printar_id(self, id):
        self.id = id
        print(f"Aqui o ID, doido! {self.id}")
    def obter_pedido(self,pedido_id=""):
        print(f"\n\nID DO PEDIDO AQUI, MISÉEEERA! {pedido_id} \n\n")
        API_URL = "http://127.0.0.1:8000/pedidos/"
        try:
            print("BATEU NO TRY DE OBTENÇÃO")
            response = requests.get(f"{API_URL}{pedido_id}")
        except:
            return "Falha na comunicação.\nVerifique o seu funcionamento da API."
        return response.json()
    
    def editar_pedido(self, pedido_id, 
                    codigo, 
                    id_cliente, 
                    id_funcionario, 
                    itens, 
                    origem, 
                    valor,
                    abertura,
                    fechamento,
                    estado, 
                    obs):
        API_URL = "http://127.0.0.1:8000/pedidos/"
        try:    
            response = requests.put(f"{API_URL}{pedido_id}", json={"codigo":codigo, 
                                                                    "id_cliente": id_cliente, 
                                                                    "id_funcionario":id_funcionario, 
                                                                    "itens":itens, 
                                                                    "origem":origem, 
                                                                    "valor":valor,
                                                                    "abertura": abertura,
                                                                    "fechamento": fechamento, 
                                                                    "estado":estado, 
                                                                    "obs":obs})
        except:
            return "Falha na cominicação.\nVerifique o seu funcionamento da API."
        return response.json() 
    def editar_origem(self,pedido_id,origem):
        p = Pedido(**self.obter_pedido(pedido_id))
        p.origem = origem
        self.editar_pedido(p.id,p.codigo,p.id_cliente,p.id_funcionario,p.itens,p.origem,p.valor,p.abertura,p.fechamento,p.estado,p.obs)
    def editar_campo(self,pedido_id,campo,conteudo):
        p = Pedido(**self.obter_pedido(pedido_id))
        match campo:
            case "codigo":
                p.codigo = conteudo
            case "id_cliente":
                p.id_cliente = conteudo
            case "abertura":
                p.abertura = conteudo
            case "fechamento":
                p.fechamento = conteudo
            case "estado":
                p.estado = conteudo
            case "valor":
                p.valor = conteudo
            case "origem":
                p.origem = conteudo
        self.editar_pedido(p.id,p.codigo,p.id_cliente,p.id_funcionario,p.itens,p.origem,p.valor,p.abertura,p.fechamento,p.estado,p.obs)
    def deletar(self,pedido_id):
        API_URL = "http://127.0.0.1:8000/pedidos/"
        try:
            response = requests.delete(f"{API_URL}{pedido_id}")
        except:
            return "Falha na comnicação.\nVerifique o seu funcionamento da API."
        return response.json()

class Box_List(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Label_Itens(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(size=self.setter('text_size')) 
        self.color =0,0,0

class ScrollBox(BoxLayout):
    def __init__(self, **kwargs):
        #self.bind(minimum_height=self.setter('height'))
        super().__init__(**kwargs)

class SpinnerOptions(SpinnerOption):
    def __init__(self, **kwargs):
        super(SpinnerOptions, self).__init__(**kwargs)
        self.bind(size=self.setter('text_size')) 
        self.background_normal = ''
        self.background_color = [.8, .8, .8, 1]    # blue colour
        self.color = 0,0,0
        self.height = 30
        self.halign = "left"
        self.padding = 10,0,0,0
        self.font_size = 12

class SpinnerDropdown(DropDown):
    def __init__(self, **kwargs):
        super(SpinnerDropdown, self).__init__(**kwargs)
        self.auto_width = False
        self.width = 150
        self.font_size = 12
        #self.bind(size=self.setter('text_size'))
class MyFooterLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
class MySpinner(Spinner):
    def __init__(self, **kwargs):
        super(MySpinner, self).__init__(**kwargs)
        self.font_size = 12
        self.dropdown_cls = SpinnerDropdown
        self.option_cls = SpinnerOptions
        self.halign = "left"
        self.padding = 10,0,0,0
        self.bind(size=self.setter('text_size'))
  
     
class Pedidos(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    def gerar_codigo(self):
        timestamp = str(datetime.now())
        print(f"Carimbo de tempo: {timestamp}")
        return timestamp
    def criar_pedido(self, codigo=f"0000", 
                    id_cliente="Anônimo",
                    id_funcionario="Geral",
                    itens="nulo",
                    origem="desconhecida",
                    valor="00,00",
                    abertura=f"{datetime.today()}",
                    fechamento="XX:XX",
                    estado="Criado", 
                    obs="Insira informações para a validação"):
        API_URL = "http://127.0.0.1:8000/pedidos/"
        print("\n\n A URL FOI REQUISITADA \n\n")
        try:
            response = requests.post(API_URL, json={"codigo":codigo, 
                                                    "id_cliente": id_cliente, 
                                                    "id_funcionario":id_funcionario, 
                                                    "itens":itens, 
                                                    "origem":origem, 
                                                    "valor":valor, 
                                                    "abertura": abertura,
                                                    "fechamento": fechamento, 
                                                    "estado":estado, 
                                                    "obs":obs
                                                    })
            print("\n\n TRY RESPONSE DO MAIN \n\n")
        except:
            return "Falha na comunicação.\nVerifique o funcionamento da API."
        print("\n\n A RESPOSTA SERÁ ENVIADA \n\n")
        return response.json()
        
    def limpar(self):
        self.ids.itens_cardapio.clear_widgets()
        self.ids.lista_pedidos.clear_widgets()
    def carregar_cardapio(self,produto_id):
        API_URL = "http://127.0.0.1:8000/produtos/"
        try:
            response = requests.get(f"{API_URL}{produto_id}")
        except:
            return "Falha na comunicação.\nVerifique o seu funcionamento da API."
        print(str(response.json()))
        for i in response.json():
            print("# PRODUTOS AQUI")
            p = Produto(**i)
            print(f'{p.categoria},{p.codigo},{p.nome},{p.valor}')
        #     self.ids.itens_cardapio.add_widget(Btn_Item(p.categoria,p.codigo,p.nome,p.valor))
# ITENS
    def obter_itens(self,pedido_id=""):
        print(f"\n\nID DO PEDIDO AQUI, MISÉEEERA! {pedido_id} \n\n")
        API_URL = "http://127.0.0.1:8000/produtos/"
        try:
            print("BATEU NO TRY DE OBTENÇÃO")
            response = requests.get(f"{API_URL}{pedido_id}")
        except:
            return "Falha na comunicação.\nVerifique o seu funcionamento da API."
        return response.json()
# ITENS
    def carregar_pedidos(self,pedido_id):
        API_URL = "http://127.0.0.1:8000/pedidos/"
        print("#  ENTROU NO CARREGAMENTO DE PEDIDOS")
        try:
            print("#  ENTROU NO 'TRY' CARREGAMENTO DE PEDIDOS")
            response = requests.get(f"{API_URL}{pedido_id}")
        except:
            return "Falha na cominicação.\nVerifique o seu funcionamento da API."
        for i in response.json():
            p = Pedido(**i)
            print("# PEDIDOS AQUI")
            #for j in vars(p):
            #    print(j)
            self.ids.lista_pedidos.add_widget(Btn_Pedido(p.id,p.codigo,p.id_cliente,p.id_funcionario,p.itens,p.origem,p.valor,p.abertura,p.fechamento,p.estado,p.obs))    