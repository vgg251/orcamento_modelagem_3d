orcamento=[]
quantidade=int(input('Quantas peças? '))

def valor_geral():
    for i in range(quantidade):
        tempo=float(input(f'Tempo de impressão da {i+1}º peça (min): '))
        peso=float(input(f'Peso da peça {i+1}: '))
        preco=((tempo*5/60)+((peso*12)/100))
        resultado=round(preco,2)
        orcamento.append(resultado)
    return orcamento 
def valor_total():
    return (f'VALOR TOTAL R${(sum(orcamento))}')

tudo=valor_geral()
unico=valor_total()

print(f'{'='*31}\n     VALOR DAS PEÇAS EM R$     \n{'='*31}')

for i in range(len(orcamento)):
    print(f'Peça {i+1}: R${orcamento[i]}')

#print('='*31)
print(f'{'='*31}\n{unico}')
print(f'Quantidade de peças: {quantidade}')