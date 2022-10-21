import tabula
from IPython.display import display

# ==================================================
# Quando encontra uma tabela formatada corretamente
# ==================================================

# Ler as tabelas da pagina 11
lista_tabelas = tabula.read_pdf('ResultadoVale.pdf', pages="11")
print(len(lista_tabelas))

for tabela in lista_tabelas:
    display(tabela)

# =====================================================
# Quando não encontra uma tabela formatada corretamente
# =====================================================

lista_tabelas2 = tabula.read_pdf("ResultadoVale.pdf", pages="10")
print(len(lista_tabelas2))

# for tabela in lista_tabelas2:
#     display(tabela)

# Manipulando a primeira tabela encontrada
tabela = lista_tabelas2[0]

# Usar a primeira linha da tabela como coluna
tabela.columns = tabela.iloc[0]

# Separando os valores da ultima coluna em duas
tabela[[0, 1]] = tabela['Variação percentual'].str.split(' ', expand=True)

# Eliminando linhas que não serão utilizadas
tabela = tabela[1:9]

# Transformar os dados da primeira coluna como indice
tabela = tabela.set_index('R$ milhões')

# Usar a primeira linha da tabela como coluna
tabela.columns = tabela.iloc[0]

# Eliminando linhas que não serão utilizadas
tabela = tabela[1:]

# Eliminando a coluna duplicada
tabela = tabela.drop("1T21/4T20 1T21/1T20", axis=1)

display(tabela)

# =====================================================
# Caso não reconheceça a tabela
# Existem 2 parâmetros para testar: Lattice e Guess
# =====================================================

# Lattice
lista_df = tabula.read_pdf("ResultadoVale.pdf", pages="10", lattice=True)
display(lista_df[0])

print('*' * 10)

# Guess
lista_df = tabula.read_pdf("ResultadoVale.pdf", pages="10", guess=False)
display(lista_df[0])
