import os
import sqlite3
import threading
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import date

#from contas import Contas
#from dados import Dados
from relatorio import Relatorio

from comandos_sql import CONTAS
from comandos_sql import URLS
from comandos_sql import ATUALIZAR_CAMINHOS
from comandos_sql import CAMINHOS_ATUALIZADOS

class Interface():
    ORIGEM = ["SRSSU", "SRSSU - APS", "Provisória", "SRSSU - APS (Investimento)"]
    RECURSO = ["Regular", "Emenda"]
    TIPO = ["Custeio", "Investimento"]
    BANCO = {"BRB": "070"}

    def __init__(self, tela, relatorio):
        self.relatorio = relatorio

        self.menu = Menu(tela)
        self.menu_configurações = Menu(self.menu)
        self.menu.add_cascade(
            label='Configurações', menu=self.menu_configurações)
        self.menu_configurações.add_separator()
        self.menu_configurações.add_command(
            label='Cadastro de fornecedores', command=self.abrir_janela_cadastro)
        self.menu_configurações.add_separator()
        self.menu_configurações.add_command(
            label='URLs', command=self.abrir_caminhos)

        self.frame_mestre = LabelFrame(tela, padx=0, pady=0)
        self.frame_mestre.pack(fill="both", expand=1, padx=10, pady=10)

        self.frame_1 = LabelFrame(self.frame_mestre, padx=0, pady=0)
        self.frame_1.pack(fill="both", padx=10, pady=0, ipady=0)

        self.frame_calendario = LabelFrame(self.frame_mestre, padx=0, pady=0)
        self.frame_calendario.pack(fill="both", padx=10, pady=0, ipady=0)

        self.frame_2 = LabelFrame(self.frame_mestre, padx=0, pady=0)
        self.frame_2.pack(fill="both", padx=10, pady=10)

        self.frame_3 = LabelFrame(self.frame_mestre, padx=0, pady=0)
        self.frame_3.pack(fill="both", expand=1, padx=10, pady=10)

        self.mycanvas = Canvas(self.frame_3, bg="black")
        self.mycanvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.rolagem = ttk.Scrollbar(self.frame_3, orient=VERTICAL, command=self.mycanvas.yview)
        self.rolagem.pack(side=RIGHT, fill=Y)

        self.mycanvas.config(yscrollcommand=self.rolagem.set)
        self.mycanvas.bind('<Configure>', lambda e: self.mycanvas)
        self.mycanvas.bind("<MouseWheel>", lambda event: self.mycanvas.yview_scroll(-int(event.delta / 60), "units"))

        self.frame_display = Frame(self.mycanvas, padx=0, pady=0)
        self.frame_display.pack(padx=0, pady=0)

        self.mycanvas.create_window((0, 0), window=self.frame_display, anchor="nw")

        self.local = StringVar()
        self.local.set(Interface.ORIGEM[0])

        self.conta_origem = OptionMenu(self.frame_1, self.local, *Interface.ORIGEM)
        self.conta_origem.grid(row=0, column=0)

        self.teste1 = Button(self.frame_2, text='Listar', command=self.exibir_pagamentos)
        self.teste1.grid(row=0, column=1)

        self.teste2 = Button(self.frame_2, text='Limpar', command=self.limpar_tela)
        self.teste2.grid(row=0, column=2)

        self.teste3 = Button(self.frame_2, text='Fornecedores', command=self.exibir_fornecedores)
        self.teste3.grid(row=0, column=3)

        self.teste3 = Button(self.frame_2, text='Contas', command=self.exibir_contas)
        self.teste3.grid(row=0, column=4)

        self.teste4 = Button(self.frame_2, text='Gerar pagamentos', command=self.imprimir_teds)
        self.teste4.grid(row=0, column=5)

        self.data_hoje = date.today()
        dia = int(self.data_hoje.strftime('%d'))
        mes = int(self.data_hoje.strftime('%m'))
        ano = int(self.data_hoje.strftime('%Y'))
        self.calendario = Calendar(self.frame_calendario, selectmode='day', year=ano, month=mes, day=dia, locale="pt_br")
        self.calendario.grid(row=0, column=0)

        btn_mostrar_data = Button(self.frame_calendario, text="Mostrar Data Selecionada", command=self.mostra_data)
        btn_mostrar_data.grid(row=1, column=0)

        # self.teste5 = Button(self.frame_2, text='pegar contas', command=self.relatorio.pegar_n_cotas)
        # self.teste5.grid(row=0, column=6)

    def mostra_data(self):
        data_selecionada = self.calendario.get_date()

        print(data_selecionada)
        print(f"dia: {data_selecionada[0:2]}")
        print(f"mês: {data_selecionada[3:5]}")
        print(f"ano: {data_selecionada[6:]}")

    def display(self, valor):
        self.mycanvas.create_text((360, 0), text=valor, fill="green", font=("Helvetica", 12, "bold"))

    def limpar_tela(self):
        self.mycanvas.delete("all")

    def atualizar_dados(self):
        origem = self.local.get()
        self.relatorio.pagamentos = self.relatorio.listar_pagamentos(self.relatorio.definir_fonte(origem))
        self.relatorio.empresas = self.relatorio.fornecedores(self.relatorio.definir_fonte(origem))

    def exibir_pagamentos(self):
        self.atualizar_dados()
        self.display(self.relatorio.formatar_relatorio(self.relatorio.pagamentos_formatados()))

    def exibir_fornecedores(self):
        self.display(self.relatorio.formatar_relatorio(self.relatorio.empresas.values()))

    def exibir_contas(self):
        self.display(self.relatorio.formatar_relatorio(self.relatorio.consultar_registros(CONTAS)))

    def imprimir_teds(self):
        origem = self.local.get()
        self.relatorio.gerar_teds(origem)

    def abrir_janela_cadastro(self):
        self.janela_de_cadastro = Toplevel()
        self.janela_de_cadastro.title('Lista de caminhos')
        self.janela_de_cadastro.resizable(True, True)

        self.frame_geral = LabelFrame(
            self.janela_de_cadastro, padx=50, pady=30
        )
        self.frame_geral.pack(padx=1, pady=1)


        self.frame_de_cadastro = LabelFrame(
            self.frame_geral, padx=10, pady=0
        )
        self.frame_de_cadastro.pack(padx=1, pady=1)

        self.frame_de_exclusao = LabelFrame(
            self.frame_geral, padx=10, pady=0
        )
        self.frame_de_exclusao.pack(padx=1, pady=1)

        self.frame_geral.pack(padx=1, pady=1)

        self.titulo_origem = Label(self.frame_de_cadastro, text="Origem")

        self.origem_bd = StringVar()
        self.origem_bd.set(Interface.ORIGEM[0])
        self.lista_origem_bd = OptionMenu(self.frame_de_cadastro, self.origem_bd, *Interface.ORIGEM)
        self.lista_origem_bd.config(width=15)

        self.titulo_recurso = Label(self.frame_de_cadastro, text="Recurso")

        self.recurso_bd = StringVar()
        self.recurso_bd.set(Interface.RECURSO[0])
        self.lista_recurso_bd = OptionMenu(self.frame_de_cadastro, self.recurso_bd, *Interface.RECURSO)
        self.lista_recurso_bd.config(width=15)

        self.titulo_tipo = Label(self.frame_de_cadastro, text="Tipo")
        self.tipo_bd = StringVar()
        self.tipo_bd.set(Interface.TIPO[0])
        self.lista_tipo_bd = OptionMenu(self.frame_de_cadastro, self.tipo_bd, *Interface.TIPO)
        self.lista_tipo_bd.config(width=15)

        self.titulo_banco = Label(self.frame_de_cadastro, text="Banco")

        self.bancos = []
        for banco in Interface.BANCO.keys():
            self.bancos.append(banco)
        self.banco_bd = StringVar()
        self.banco_bd.set("BRB")
        self.lista_banco_bd = OptionMenu(self.frame_de_cadastro, self.banco_bd, *self.bancos)
        self.lista_banco_bd.config(width=15)

        self.titulo_agencia = Label(self.frame_de_cadastro, text="Agência")

        self.n_agencia = Entry(
            self.frame_de_cadastro, width=10
        )

        self.titulo_conta = Label(self.frame_de_cadastro, text="Conta")

        self.n_conta = Entry(
            self.frame_de_cadastro, width=15
        )

        self.titulo_cnpj = Label(self.frame_de_cadastro, text="CNPJ")

        self.n_cnpj = Entry(
            self.frame_de_cadastro, width=20
        )

        self.botao_cadastro = Button(self.frame_de_cadastro, text="Cadastrar", command=self.submeter_conta)

        #configurações de grid

        self.titulo_origem.grid(row=0, column=1)
        self.titulo_recurso.grid(row=0, column=2)
        self.titulo_tipo.grid(row=0, column=3)
        self.titulo_banco.grid(row=0, column=4)
        self.titulo_agencia.grid(row=0, column=5)
        self.titulo_conta.grid(row=0, column=6)
        self.titulo_cnpj.grid(row=0, column=7)


        self.lista_origem_bd.grid(row=1, column=1)
        self.lista_recurso_bd.grid(row=1, column=2)
        self.lista_tipo_bd.grid(row=1, column=3)
        self.lista_banco_bd.grid(row=1, column=4)
        self.n_agencia.grid(row=1, column=5)
        self.n_conta.grid(row=1, column=6)
        self.n_cnpj.grid(row=1, column=7)

        self.botao_cadastro.grid(row=2, column=1, columnspan=7, pady=10, sticky=E)

        self.opcoes_de_exclusao = Label(self.frame_de_exclusao, text="Caso deseje excluir uma conta, utilize a opção abaixo:")

        self.v_contas = StringVar()

        self.atualizar_contas()

        # a = self.numero_contas()
        # self.v_contas.set('Selecione uma conta')
        # self.v_contas_bd = OptionMenu(self.frame_de_exclusao, self.v_contas, *a)
        # self.v_contas_bd.config(width=20)

        self.botao_excluir = Button(self.frame_de_exclusao, text="Excluir conta", command=self.excluir_conta)

        #self.opcoes_de_exclusao.grid(row=0, column=1, columnspan=2)
        self.v_contas_bd.grid(row=1, column=1, padx=30)
        self.botao_excluir.grid(row=1, column=2, padx=30)



    def atualizar_contas(self):
        if self.numero_contas() == []:
            a = ["Nenhuma conta cadastrada"]
        else:
            a = self.numero_contas()
        self.v_contas.set('Selecione uma conta')
        self.v_contas_bd = OptionMenu(self.frame_de_exclusao, self.v_contas, *a)
        self.v_contas_bd.config(width=20)
        self.v_contas_bd.grid(row=1, column=1, padx=30)

    def submeter_conta(self):
        self.relatorio.cadastrar_conta(self.origem_bd.get(), self.recurso_bd.get(), self.tipo_bd.get(), Interface.BANCO[self.banco_bd.get()], self.n_agencia.get(), self.n_conta.get(), self.n_cnpj.get())
        self.atualizar_contas()
        self.n_agencia.delete(0, END)
        self.n_conta.delete(0, END)
        self.n_cnpj.delete(0, END)


    def numero_contas(self):
        contas = list(self.relatorio.pegar_n_contas())
        return contas

    def excluir_conta(self):
        conta = self.v_contas.get()
        print(f"Esta é a {conta[1:-2]}")
        self.relatorio.deletar_conta(conta[1:-2])
        self.atualizar_contas()

    def altera_caminho(self, entrada, xlsx=False):
        if xlsx == True:
            caminho = filedialog.askopenfilename(
                initialdir=self.relatorio.caminho_do_arquivo(),
                filetypes=(('Arquivos', '*.xlsx'), ("Tudo", '*.*'))
            )
        else:
            caminho = filedialog.askdirectory(
                initialdir=self.relatorio.caminho_do_arquivo()
            )
        entrada.delete(0, 'end')
        entrada.insert(0, caminho)

    def atualizar_caminhos(self):
        pass
        resposta = messagebox.askyesno(
            ATUALIZAR_CAMINHOS[0], ATUALIZAR_CAMINHOS[1]
        )

        itens_para_atualizacao = [
            ['SRSSU',
             '1',
             self.caminho_srssu.get()],

            ['SRSSU - APS',
             '2',
             self.caminho_aps.get()],

            ['Provisória',
             '3',
             self.caminho_srssu_i.get()],

            ['SRSSU - APS (Investimento)',
             '4',
             self.caminho_aps_i.get()]
        ]

        if resposta:
            arquivo = self.relatorio.caminho_do_arquivo()
            with sqlite3.connect(f'{arquivo}/guias.db') as conexao:
                direcionador = conexao.cursor()
                for item in itens_para_atualizacao:
                    linha_update = (
                        f"UPDATE urls SET url = :nova_url WHERE variavel = '{item[0]}'"
                    )
                    print(f"0{item[0]} 1{item[1]} 2{item[2]}")
                    direcionador.execute(linha_update, {'nova_url': item[2]})
                conexao.commit()
            self.caminhos.destroy()
            messagebox.showinfo(
                CAMINHOS_ATUALIZADOS[0],
                (CAMINHOS_ATUALIZADOS[1])
            )
        else:
            self.caminhos.destroy()

    def abrir_caminhos(self):
        self.caminhos = Toplevel()
        self.urls = self.relatorio.consultar_registros(URLS)
        print(self.urls)
        self.caminhos.title('Caminhos')
        self.caminhos.resizable(False, False)
        self.frame_caminhos = LabelFrame(
            self.caminhos, padx=0, pady=0
        )
        self.frame_caminhos.pack(padx=1, pady=1)

        self.botao_xlsx = Button(
            self.frame_caminhos, text='SRSSU',
            command=lambda: self.altera_caminho(self.caminho_srssu, True),
            padx=0, pady=0, bg='green', fg='white',
            font=('Helvetica', 8, 'bold'), bd=1
        )
        self.caminho_srssu = Entry(self.frame_caminhos, width=70)

        self.botao_pasta_de_certidões = Button(
            self.frame_caminhos, text='SRSSU - APS',
            command=lambda: (
                self.altera_caminho(self.caminho_aps, True)),
            padx=0, pady=0, bg='green', fg='white',
            font=('Helvetica', 8, 'bold'), bd=1
        )
        self.caminho_aps = Entry(
            self.frame_caminhos, width=70
        )

        self.botao_log = Button(
            self.frame_caminhos, text='Provisória',
            command=lambda: self.altera_caminho(self.caminho_srssu_i, True), padx=0,
            pady=0, bg='green', fg='white', font=('Helvetica', 8, 'bold'),
            bd=1
        )
        self.caminho_srssu_i = Entry(self.frame_caminhos, width=70)

        self.certidões_para_pagamento = Button(
            self.frame_caminhos, text='SRSSU - APS (Investimento)',
            command=lambda: (
                self.altera_caminho(self.caminho_aps_i, True)
            ),
            padx=0, pady=0, bg='green', fg='white',
            font=('Helvetica', 8, 'bold'), bd=1
        )

        self.caminho_aps_i = Entry(
            self.frame_caminhos, width=70
        )

        self.gravar_alterações = Button(
            self.frame_caminhos, text='Gravar alterações',
            command=self.atualizar_caminhos, padx=10, pady=10, bg='green',
            fg='white', font=('Helvetica', 8, 'bold'), bd=1
        )

        self.botao_xlsx.grid(
            row=1, column=1, columnspan=1, padx=15, pady=10, ipadx=5,
            ipady=13, sticky=W + E
        )
        self.caminho_srssu.insert(0, self.urls[0][1])
        self.caminho_srssu.grid(row=1, column=2, padx=20)

        self.botao_pasta_de_certidões.grid(
            row=2, column=1, columnspan=1, padx=15, pady=10, ipadx=10,
            ipady=13, sticky=W + E
        )

        self.caminho_aps.insert(0, self.urls[1][1])
        self.caminho_aps.grid(row=2, column=2, padx=20)

        self.botao_log.grid(
            row=3, column=1, columnspan=1, padx=15, pady=10, ipadx=10,
            ipady=13, sticky=W + E
        )

        self.caminho_srssu_i.insert(0, self.urls[2][1])
        self.caminho_srssu_i.grid(row=3, column=2, padx=20)

        self.certidões_para_pagamento.grid(
            row=4, column=1, columnspan=1, padx=15, pady=10, ipadx=10,
            ipady=13, sticky=W + E
        )

        self.caminho_aps_i.insert(0, self.urls[3][1])
        self.caminho_aps_i.grid(row=4, column=2, padx=20)

        self.gravar_alterações.grid(
            row=6, column=2, columnspan=1, padx=15, pady=10, ipadx=10,
            ipady=13
        )



if __name__ == '__main__':
    rel = Relatorio()
    tela = Tk()
    tela.geometry("1100x600")
    tela.resizable(1, 1)
    objeto_tela = Interface(tela, rel)
    #tela.title()
    tela.config(menu=objeto_tela.menu)
    tela.mainloop()
