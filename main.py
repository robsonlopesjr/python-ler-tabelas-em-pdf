import tabula
from IPython.display import display

# Ler as tabelas da pagina 11
lista_tabelas = tabula.read_pdf('ResultadoVale.pdf', pages="11")

# print(len(lista_tabelas))

for tabela in lista_tabelas:
    display(tabela)
