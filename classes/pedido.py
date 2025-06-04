import json
caminho = "classes/pedidos.json"

class Pedido():
    def __init__(self,cod_cliente = str,endereco_entrega=str,celular=str):
        self.cod_cliente = cod_cliente #apenas esse código vai referenciar outras informações de clientes que sejam necessárias
        self.endereco_entrega = endereco_entrega
        self.estado = "iniciado"
        self.itens=[]
        self.total=0.0
        self.formas_de_pagamento=[0,0,0,0,0] #Dinheiro|Pix|Cart. Débito| Cart. Crédito|Cortesia
        #cada posição array representará uma forma de pagamento, ter valor indica a(s) forma(s) de pahamento utilzada
    def registrar(self):
        with open(caminho,"r") as arquivo:
            dados = json.load(arquivo)
        aux = []
        for i in dados:
            aux.append(i)        
        aux.append(self.__dict__)
        print(aux)
        with open(caminho, "w+") as arquivo:
            json.dump(aux,arquivo,ensure_ascii=False,indent=0)

f = Pedido("CL001",
            "Rua Dom Cornélio Vermans"
            )

f.registrar()