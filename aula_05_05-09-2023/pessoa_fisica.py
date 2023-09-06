from pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, cpfParam):
        self.CPF = cpfParam
        

    def setCPF(self, cpfParam):
        self.CPF = cpfParam

    def getCPF(self):
        return self.CPF 


        