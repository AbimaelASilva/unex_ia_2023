#imports
from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica


print('###### CADASTRO ######');

name = input('Informe seu nome:')
age = int(input('Informe sua idade:'))

typePerson = 0

#Loop para forçar o infome do tipo correto
while (typePerson < 1 or typePerson>2):
    print('DIGITE [1] PARA PESSOA FÍSICA E [2] PARA PERSSOA JURÍDICA:')
    typePerson = int(input())


docNumber = input('Informe o número do documento:')

#Teste que verifica tipo de pessoa
if(typePerson==1):
   pessoaFisica = PessoaFisica(docNumber,name,age)
   pessoaFisica.printPF()
else:
    pessoaJuridica = PessoaFisica(docNumber,name,age)
    pessoaJuridica.printPF()



