import customtkinter as ctk
from cotacao import *

# Criando e configurando a janela
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

janela = ctk.CTk()
janela.title('Conversor de moedas')
janela.geometry('500x490')

# Lista de moedas
moedas = listar_moedas()

# Criando elementos
titulo = ctk.CTkLabel(janela, text='Conversor de moedas', font=('Arial', 25))

entrada_valor = ctk.CTkEntry(janela, placeholder_text='Digite o valor')

moeda_convertida = ctk.CTkLabel(janela, text='Moeda de origem:')
moeda_destino = ctk.CTkLabel(janela, text='Moeda de destino:')

moeda_convertida_campo = ctk.CTkOptionMenu(janela, values=moedas)
moeda_destino_campo = ctk.CTkOptionMenu(janela, values=moedas)

entrada_valor = ctk.CTkEntry(janela, placeholder_text='Digite o valor')
resultado_label = ctk.CTkLabel(janela, text='Resultado', font=('Arial', 16))

def realizar_conversao():
    try:
        valor = float(entrada_valor.get())
        origem = moeda_convertida_campo.get()
        destino = moeda_destino_campo.get()
        resultado = converter_moeda(valor, origem, destino)
        if resultado is not None:
            resultado_label.configure(text=f"{valor} {origem} = {resultado} {destino}")
        else:
            resultado_label.configure(text="Erro na conversão.")
    except ValueError:
        resultado_label.configure(text="Digite um valor numérico válido.")


botao_conversao = ctk.CTkButton(janela, text='Converter', command=realizar_conversao)

lista_moedas = ctk.CTkScrollableFrame(janela, height=150)

# Adicionando os elementos na janela
titulo.pack(padx=10, pady=10)

entrada_valor.pack(pady=10)

moeda_convertida.pack(padx=10, pady=8)
moeda_convertida_campo.pack(padx=10)

moeda_destino.pack(padx=10, pady=8)
moeda_destino_campo.pack(padx=10)

resultado_label.pack(pady=10)

botao_conversao.pack(padx=10, pady=25)

lista_moedas.pack(padx=10, pady=10)

for moeda in moedas:
    ctk.CTkLabel(lista_moedas, text=moeda).pack()

# Rodando a janela
janela.mainloop()