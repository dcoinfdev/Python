class Pessoa:

    #Construtor 
    def __init__(self, nome):
        self._nome = nome

    #Obtendo Valores
    def get_nome(self):
        print(".:: Obtendo nome ::.")
        return self._nome
    
    #Definido Novos Valores
    def set_nome(self, n):
        print(".:: Validando Nome ::.")
        if n == str:
            print("Nome inválido: ", n)
        else:
            print(".:: Novo nome ::.")
            self._nome = n

    #Deletando Valores.
    def del_nome(self):
        print("Até logo")
        del self._nome

    #Criando propriedades.
    n = property(get_nome, set_nome, del_nome)

#Consumindo a classe.
a = Pessoa(nome= any)
a.n = input("Insira um nome: ")
print(a.n)
del a.n