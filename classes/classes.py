import json
from decimal import Decimal as desc
caminho = "orders/pedido.json"

class Agente():
    def __init__(self) -> None:
        pass

class Cliente():
    def __init__(self,codigo,nome,**kwargs):
        self.codigo = codigo
        self.nome = nome
        self.endereco = str
        self.instagram = str


class Item():
    def __init__(self,cod=str,nome=str,descr=str,valor=desc) -> None:
        self.codigo = cod
        self.nome = nome
        self.desc = descr
        self.valor = valor

a = Item("0101","Temaki","Coida japonesa etc e tal",35.90)
b = Item("0201","Hosomaki","Coida japonesa etc e tal",5.90)
c = Item("0301","Tekamaki","Coida japonesa etc e tal",22.75)
d = Item("0401","Niguiri","Coida japonesa etc e tal",18.50)
e = Item("0501","Uasabi","Coida japonesa etc e tal",19.90)

class Pedido():
    def __init__(self, codigo :str, cod_cliente:str, cod_atendente:str,itens =str,**kwargs):
        self.codigo = codigo
        self.cod_cliente = cod_cliente
        self.cod_atendente = cod_atendente
        self.total = 0



class Pedido_Itens():
    def __init__(self,cod_pedido=str,**kwargs):
        self.codigo = cod_pedido
        self.itens = []        

p1 = Pedido('P001','C001','F001')
p1_it = Pedido_Itens(p1.codigo)
p1_it.itens.append(a)

show =[]
show.append = p1.codigo

for i in p1,vars(p1):
    print(i)



#print(p1.__dict__)
# with open(caminho, "w") as arquivo:
#     json.dump(tb,arquivo,ensure_ascii=False,indent=0)


# with open(caminho,"r") as arquivo:
#     dados = json.load(arquivo)
#     p4 = Pedido(**dados[0])

# print(p4.__dict__)