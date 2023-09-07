from pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, cpfParam, name, age):
        super().__init__(name,age) #Constructor da superclasse -Pessoa       
        self.CPF = cpfParam
        

    def setCPF(self, cpfParam):
        self.CPF = cpfParam

    def getCPF(self):
        return self.CPF 

    def printPF(self):
        self.printPerson()
        print('CNPJ: ', self.CPF);
        