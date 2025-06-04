from typing import Any, Sequence, Type
from bson.codec_options import TypeRegistry
from pymongo import MongoClient

conet_string = "mongodb://localhost:27017/"

class My_connection(MongoClient):
    def __init__(self,conet_string):
        self.cliente = self(conet_string) #Cliente acessa conexão indicada pela string
        self.db_connection = self.cliente["DGtech"] #Conexão é direcionada ao banco de dados existente
        print(self.db_connection)
        
'''
    def collection(self,collection):
        self.collection = self.db_connection.get_collection(collection) 
        print(collection)
    def adicionar(self,collection_in,text):# TESTADA - OK
        collection = self.db_connection.get_collection(collection_in)
        collection.insert_one(
            text
        )
    def buscar(self,collecion,text,campo, valor):# TESTADA - OK
        search_filter = {f"{campo}":f"{valor}"} #Descreve o que será buscado dentro da conexão
        if campo =="" and valor=="":
            response = self.collection.find() #É a resposta da busca realizada
        else:
            response = self.collection.find(search_filter) #É a resposta da busca realizada

        #print(response) #'response' é apenas un cursor que indica onde a informação se encotra
        return response
    def editar(self,collection_in,old_text=dict,new_text=dict): # TESTADA - OK
        collection = self.db_connection.get_collection(collection_in)
        resultado = collection.update_one(  
            old_text,  # Filtro para encontrar o documento  
            {'$set': new_text}  # Atualiza o campo  
        )
    def renomear_campo(self,collection_in, old, new): # TESTADA - OK
        collection = self.db_connection.get_collection(collection_in)
        collection.update_many({old:{"$exists":True}},{'$rename': {old: new}})
'''