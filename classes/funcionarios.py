import json
caminho = "classes/funcionarios.json"

class Funcionario():
    def __init__(self,nome = str,
                 sobrenome =str(""),
                 apelido=str(""),
                 cpf =str(""),
                 funcao=str(""),
                 nivel=int(0),
                 endereco=str(""),
                 celular=int(0),
                 senha=str("")): 
        self.nome = nome
        self.sobrenome = sobrenome
        self.apelido = apelido
        self.cpf = cpf
        self.funcao = funcao
        self.nivel = nivel
        self.endereco = endereco
        self.celular = celular
        self.senha = senha
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

# f = Funcionario("Gabriel",
#                 "Campelo Gomes",
#                 "Campelo",
#                 "09809809898", #CPF - os pontos e trasso serão acrescenados na formatação de exibição
#                 "Garcon",
#                 1,
#                 "Rua A, QD 20, Lt 6",
#                 9498098098,
#                 123
#                 )
if __name__=="funcionario":
    f2 = Funcionario("Amanda",
                    "Vasconcelos Dias",
                    "Mãe da tatá",
                    "132312313123", #os pontos e trasso serão acrescenados na formatação de exibição
                    "Rua A, QD 20, Lt 6",
                    857567567567,
                    345
                    )
    #f.registrar()
    f2.registrar()