class Pessoa:

    #Construtor 
    def __init__(self, nome):
        self._nome = nome

    #Obtendo Valores
    def get_nome(self):
        print("Obtendo Nome")
        return self._nome
    
    #Definido Novos Valores
    def set_nome(self, n):
        print("Novo nome: " + n)
        self._nome = n

    #Deletando Valores.
    def del_nome(self):
        print("Até logo")
        del self._nome

    #Criando propriedades.
    n = property(get_nome, set_nome, del_nome)

#Consumindo a classe.
a = Pessoa("Gislaine Oliveira")
print("Nome atual: " + a.n)
a.n = "Isabelle Schimdt"
del a.n