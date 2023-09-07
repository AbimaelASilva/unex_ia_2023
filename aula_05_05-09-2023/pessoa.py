class Pessoa:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def setName(self, name):
        self.name = name
        
    def setAge(self,  age):
        self.age = age

    def getName(self):
        return self.name 

    def getAge(self):
        return self.age

    def printPerson(self):
      
        print('\n  \n  \n  \n  \n \n  \n  \n  \n  \n');
        print(self.name,', Seja muito bem vindo(a) ao SUPER curso de Python!');
        print('----------------------------------------------------------------');
        print('############### DADOS FORNECIDOS PARA O CADASTR0 ###############')
        print('----------------------------------------------------------------');
        print('Nome: ', self.name)
        print('Idade: ', str(self.age)) 


        