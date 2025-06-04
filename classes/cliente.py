import json
caminho = "classes/clientes.json"

class Cliente():
    def __init__(self,nome = str,endereco=str,celular=str):
        self.nome = nome
        self.sobrenome = ""
        self.apelido = ""
        self.cpf = ""
        self.nivel = 1
        self.endereco = endereco
        self.celular = celular
        self.senha = ""
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

f = Cliente("Fulano",
            #"da Silva",
            #"Fula",
            #"6876657446533", #CPF - os pontos e trasso serão acrescenados na formatação de exibição
            #1,
            "Rua JE, QD 2, Lt 30",
            9442343547,
            #987
            )

f.registrar()