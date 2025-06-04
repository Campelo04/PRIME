from pymongo import MongoClient

class Cardapio():
    def __init__(self,**kwargs):
        self.conet_string = "mongodb://localhost:27017/"  #string de conexão 
        self.cliente = MongoClient(self.conet_string) #Cliente acessa conexão indicada pela string
        self.db_connection = self.cliente["DGtech"] #Conexão é direcionada ao banco de dados existente
        print(self.db_connection) #Mostra se a conexão foi bem sucedida
        self.collection = self.db_connection.get_collection("Cardapio")
    def buscar(self):
        self.campo = campo
        self.valor = valor
        search_filter = {f"{campo}":f"{valor}"} #Descreve o que será buscado dentro da conexão
        response = self.collection.find(search_filter) #É a resposta da busca realizada
        print(response) #'response' é apenas un cursor que indica onde a informação se encotra
        for i in response: print(i)

C = Cardapio
C.buscar()