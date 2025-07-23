import customtkinter as ctk
from cotacao import *

# Criando e configurando a janela
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

janela = ctk.CTk()
janela.title('Conversor de moedas')
janela.geometry('500x490')

# Lista de moedas
moedas_dict = listar_moedas()         # dicionário {código: nome}
moedas = list(moedas_dict.keys())     # lista de códigos para os menus

# Título
titulo = ctk.CTkLabel(janela, text='Conversor de moedas', font=('Arial', 25))

# Entrada do valor a ser convertido
entrada_valor = ctk.CTkEntry(janela, placeholder_text='Digite o valor')

# Texto que vai indicar a Moeda de origem
moeda_convertida = ctk.CTkLabel(janela, text='Moeda de origem:')
# Texto que vai indicar a Moeda final
moeda_destino = ctk.CTkLabel(janela, text='Moeda de destino:')

# Menu de opções de moedas de origem
moeda_convertida_campo = ctk.CTkOptionMenu(janela, values=moedas)
# Menu de opções de moedas de destino/final
moeda_destino_campo = ctk.CTkOptionMenu(janela, values=moedas)

# Texto que vai indicar onde o resultado vai aparecer
resultado_label = ctk.CTkLabel(janela, text='Resultado', font=('Arial', 16))

# Função que vai ser chamada pelo botão "CONVERTER"
def realizar_conversao():
    try:
        valor = float(entrada_valor.get()) # Vai indicar a entrada como "FLOAT" - O get retorna uma string
        origem = moeda_convertida_campo.get() # Retorna o valor da moeda escolhida
        destino = moeda_destino_campo.get() # Retorna o valor da moeda escolhida
        resultado = converter_moeda(valor, origem, destino)
        if resultado is not None:
            resultado_label.configure(text=f"{valor} {origem} = {resultado} {destino}")
        else:
            resultado_label.configure(text="Erro na conversão.")
    except ValueError:
        resultado_label.configure(text="Digite um valor numérico válido.")

# Botão que vai realizar a conversão
botao_conversao = ctk.CTkButton(janela, text='Converter', command=realizar_conversao)

# Frame que vai conter todas as moedas
lista_moedas = ctk.CTkScrollableFrame(janela, height=150)

# Adicionando os elementos na janela
# ".pack" realiza o posicionamento das estruturas uma em cima da outra, de cima para baixo
titulo.pack(padx=10, pady=10)

entrada_valor.pack(pady=10)

moeda_convertida.pack(padx=10, pady=8)
moeda_convertida_campo.pack(padx=10)

moeda_destino.pack(padx=10, pady=8)
moeda_destino_campo.pack(padx=10)

resultado_label.pack(pady=10)

botao_conversao.pack(padx=10, pady=25)

lista_moedas.pack(padx=10, pady=10)

# Laço de repetição que vai mostrar todas as moedas presentes dentro
for codigo, nome in moedas_dict.items():
    texto = f"{codigo} - {nome}"
    ctk.CTkLabel(lista_moedas, text=texto, font=("Arial", 15)).pack(anchor="w")

# Rodando a janela
janela.mainloop()