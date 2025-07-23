import customtkinter as ctk

# Criando e configurando a janela
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

janela = ctk.CTk()
janela.title('Conversor de moedas')
janela.geometry('500x490')

# Criando elementos
titulo = ctk.CTkLabel(janela, text='Conversor de moedas', font=('Arial', 25))

moeda_convertida = ctk.CTkLabel(janela, text='Moeda de origem:')
moeda_destino = ctk.CTkLabel(janela, text='Moeda de destino:')

moeda_convertida_campo = ctk.CTkOptionMenu(janela, values=['BRL', 'EUR', 'USD', 'BTC'])
moeda_destino_campo = ctk.CTkOptionMenu(janela, values=['BRL', 'EUR', 'USD', 'BTC'])

def converter_moeda():
    print("Converter moeda")


botao_conversao = ctk.CTkButton(janela, text='Converter', command=converter_moeda)

lista_moedas = ctk.CTkScrollableFrame(janela)

# Adicionando os elementos na janela
titulo.pack(padx=10, pady=10)

moeda_convertida.pack(padx=10, pady=8)
moeda_convertida_campo.pack(padx=10)

moeda_destino.pack(padx=10, pady=8)
moeda_destino_campo.pack(padx=10)

botao_conversao.pack(padx=10, pady=25)

lista_moedas.pack(padx=10)

# Rodando a janela
janela.mainloop()