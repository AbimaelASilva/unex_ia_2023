from pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, cnpjParam, name, age):
        super().__init__( name, age) #Constructor da superclasse -Pessoa
        self.CNPJ = cnpjParam
        
    def setCNPJ(self, cnpjParam):
        self.CNPJ = cnpjParam

    def getCNPJ(self):
        return self.CNPJ 
    
    def printPJ(self):
        self.printPerson()
        print('CNPJ: ', self.CNPJ);


        