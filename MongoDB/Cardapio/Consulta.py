from pymongo import MongoClient

conet_string = "mongodb://localhost:27017/"  #string de conexão 
cliente = MongoClient(conet_string) #Cliente acessa conexão indicada pela string
db_connection = cliente["DGtech"] #Conexão é direcionada ao banco de dados existente
print(db_connection) #Mostra se a conexão foi bem sucedida
#Conecta à uma collection dentr do banco de dados indicado previamente
collection = db_connection.get_collection("Cardapio") 
print(collection) 
campo = "categoria"
valor = "Entrada"
search_filter = {f"{campo}":f"{valor}"} #Descreve o que será buscado dentro da conexão
response = collection.find(search_filter) #É a resposta da busca realizada
print(response) #'response' é apenas un cursor que indica onde a informação se encotra
for i in response: print(i)