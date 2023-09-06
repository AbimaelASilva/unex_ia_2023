from pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, cnpjParam):
        self.CNPJ = cnpjParam
        
    def setCNPJ(self, cnpjParam):
        self.CNPJ = cnpjParam

    def getCNPJ(self):
        return self.CNPJ 


        