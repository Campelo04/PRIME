from pymongo import MongoClient

conet_string = "mongodb://localhost:27017/"  #string de conexão 
cliente = MongoClient(conet_string) #Cliente acessa conexão indicada pela string
db_connection = cliente["DGtech"] #Conexão é direcionada ao banco de dados existente

print(db_connection) #Mostra se a conexão foi bem sucedida

#Conecta à uma collection dentr do banco de dados indicado previamente
collection = db_connection.get_collection("Cardapio") 
print(collection) 
aux =""

categoria = ""
cod_categoria = ""
nome = ""
valor = ""
desc = ""

cont =0
CATEGORIAS =[]
with open("E:\DGTech_Hayatoo_3.0\Data\Menu\HAYATOO.csv","r") as arquivo:
    for i in arquivo:
        print(i)
        for j in i:
            #print(j)
            if j != ";":# salva os caracters entre os separadores ";"
                aux+=j
            elif j == ";": #usa o contador para transferir o dado do auxiliar para a variavel correta
                match cont:
                    case 0:
                        categoria = aux
                        #if len(CATEGORIAS) == 0 or categoria != CATEGORIAS[len(CATEGORIAS)-1]: CATEGORIAS.append(categoria)
                        aux = ""
                    case 1:
                        cod_categoria = aux
                        aux =""
                    case 2:
                        if len(aux)==1:
                            aux = "0"+aux
                            cod_categoria = cod_categoria+aux
                        else:
                            cod_categoria = cod_categoria+aux
                        aux = ""
                    case 3:
                        nome = aux
                        aux = ""
                cont+=1
        if j != ";" and cont >=4:
            valor = aux[0:len(aux)-1]
            print(f"\n\nAqui está o valor: {valor}")
        print(f"Categoria: {categoria}\nCódigo da Categoria: {cod_categoria}\nNome: {nome}\nValor: {valor}\n")
        collection.insert_one({
            "categoria":f"{categoria}",
            "id":f"{cod_categoria}",
            "nome":f"{nome}",
            "valor":f"{valor}"
        })
        #zera todas as variaveis para que os dados de um novo item sejam salvos
        aux = ""
        categoria = ""
        cod_categoria = ""
        nome = ""
        valor = ""
        desc = ""
        cont = 0

# collection = db_connection.get_collection("Categorias")
# for i in range(len(CATEGORIAS)-1):
#     collection.insert_one({
#                 f"{i+10}":CATEGORIAS[i]
#             })
# print(CATEGORIAS)
            
        


        