
# Lista dos nomes dos funcionarios com os turnos e veiculo 
Funcionarios = ['Vitoria', 'Bruna', 'Alice', 'Jessica', 'Marcos', 'Henrique', 'Kamilly']
turno_dia = ['Vitoria', 'Alice', 'Marcos', 'Henrique']
turno_noite = ['Bruna', 'Jessica', 'Kamilly']
tem_carro = ['Bruna', 'Alice']

# Filtrando funcionario do turno dia e com carro 
lista1 = set(tem_carro).intersection(turno_dia)
print(lista1)

#Filtrando funcionario do turno noite e com carro 
lista2 = set(tem_carro).intersection(turno_noite)
print(lista2)

#Filtrando funcionario que não tem carro 
lista3 = set(Funcionarios).difference(tem_carro)
print(lista3)















    


