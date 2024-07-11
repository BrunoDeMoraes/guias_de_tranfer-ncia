LOGO = (0, 276, 85, 18)

LINHAS_ESTRUTURA = [
    (8, 273, 196, 273), #primeira linha superior
    (102, 268, 102, 220),  #Linha central
    (196, 268, 196, 220),  #linha direita
    (8, 268, 8, 220),  #linha esquerda
    (24, 268, 24, 264),  # divisão linha 1.1
    (44, 268, 44, 264),  # divisão linha 1.2
    (80, 268, 80, 264),  # divisão linha 1.3
    (118, 268, 118, 264),  # divisão linha 1.4
    (142, 268, 142, 264),  # divisão linha 1.5
    (168, 268, 168, 264),  #divisão linha 1.6
    (8, 264, 196, 264),  #linha horizontal 1 258
    (80, 264, 80, 254),  #linha vertical telefone
    (8, 254, 196, 254),  #linha horizontal 2 248
    (8, 250, 196, 250), #linha horizontal 3 238
    (8, 240, 102, 240),  #meia linha horizontal 1
    (8, 235, 102, 235),  #linha horizontal 4
    (8, 230, 196, 230),  #linha horizontal 4.5
    (8, 225, 196, 225),  #linha horizontal 5
    (8, 220, 196, 220),  #linha horizontal 6
    (8, 214, 8, 219),  #linha vertical id esquerda
    (75, 214, 75, 219),  #linha vertica id direita
    (8, 214, 75, 214),  #linha horizontal id
    (8, 199, 196, 199),  #linha horizontal assinatura
    (102, 207, 102, 199),  #linha vertical assinatura
]

LINHASTPGAMENTO = [
    (60, 86, 60, 91),
    (85, 86, 85, 91),
    (110, 86, 110, 91),
    (135, 86, 135, 91),
    (160, 86, 160, 91)
]

LINHAS_PAGAMENTOS = [
    (60, 81, 60, 86),
    (85, 81, 85, 86),
    (110, 81, 110, 86),
    (135, 81, 135, 86),
    (160, 81, 160, 86)
]

RETANGULOS = [
    (126, 281, 72, 7),
    (40, 226, 3, 3),
    (70, 226, 3, 3),
    (40, 221, 3, 3),
    (70, 221, 3, 3),
    (140, 226, 3, 3),
    (170, 226, 3, 3),
    (170, 226, 3, 3),
    (140, 221, 3, 3),
    (170, 221, 3, 3),
    (21, 236, 3, 3),
    (66, 236, 3, 3),
]

RETANGULOSTITULO =[
    (12, 86, 180, 5)
]

RETANGULO_PAGAMENTO = [
    (12, 81, 180, 5)
]


# Strings
TIMES6 = [
    (25, 237, "00001 - Pagamento de ipostos, tributos e taxas"),
    (70, 237, "00005 - Pagamentos de fornecedores")
]


TIMES7 = [
    (10, 265, "Banco"),
    (26, 265, "Agência"),
    (46, 265, "Conta"),
    (104, 265, "Banco"),
    (120, 265, "Agência"),
    (144, 265, "Conta"),
    (170, 265, "Valor"),
    (10, 261, "Nome do(s) Remetente(s)"),
    (104, 261, "Nome do(s) Destinatário(s)"),
    (10, 251, "CNPJ/CPF(s)"),
    (104, 251, "CNPJ/CPF(s)"),
    (104, 247, "Valor por Extenso"),
    (10, 247, "Endereço"),
    (82, 261, "Telefone(s)"),
    (10, 227, "Tipo Pessoa Debitada"),
    (10, 222, "Tipo Conta Debitada"),
    (104, 227, "Tipo Pessoa Creditada"),
    (104, 222, "Tipo Conta Creditada"),
    (10, 237, "Finalidade"),
    (10, 232, "Histórico"),
    (10, 217, "Nº Identificação Depósito"),
    (76, 216, (
        "Preencher somente nas transferências "
        "de recursos para deposito judicial"
    )
     ),
    (10, 211, (
        "Autorizo o Banco a DEBITAR em minha Conta"
        " de Depósitos, nesta Agência, o valor da "
        "presente transferência de fundos."
    )
     ),
    (17, 201, (
        "Luiz Antônio Roriz Bueno - "
        "Diretor Administrativo - Ma"
        "trícula: 1.659.430-4"
    )
     ),
    (114, 201, (
        "Willy Pereira da Silva Filho - "
        "Superintendente - Matrícula 1.680.762-6"
    )
     )
]

TIMES7DATA = [(155, 217, 'Data_impressão')]

TIMESB7NOMEEMPRESA = (104, 258)

TIMESB7EXTENSO = (104, 242)

TIMES8 = [
    (45, 226, "Pesssoa Física"),
    (75, 226, "Pesssoa Jurídica"),
    (45, 221, "Conta Corrente"),
    (75, 221, "Conta Poupança"),
    (145, 226, "Pesssoa Física"),
    (175, 226, "Pesssoa Jurídica"),
    (145, 221, "Conta Corrente"),
    (175, 221, "Conta Poupança")
]

TIMESB8 = [
    (9, 275, "ISPB -00.000.208"),
    (71, 227, "\u2713"),
    (41, 222, "\u2713"),
    (171, 227, "\u2713"),
    (141, 222, "\u2713"),
    (67, 237, "\u2713"),
    (10, 242, (
        "Área especial nº 01, Lote Único - "
        "Setor Central Gama/DF. CEP: 72.405-901"
    )
     ),
    (82, 256, "(61) 3449-7105")  #telefone
]

TIMES8_PAGAMENTOS = [
    (14, 82, 4), #CNPJ
    (69, 82, 0), #cotação
    (91, 82, 2), #empresa
    (113, 82, 8), #valor bruto
    (163, 82, 3), #valor liquido
    (138, 82, -1) #ISS+IR
]

TIMESB8CONTA = [
    (17, 265, 3),  # banco
    (35, 265, 4), #agência
    (53, 265, 5), #conta
    (10, 256, 0),  #origem
    (25, 251, 6),  #CNPJ - regional
]

TIMESB8FORNECEDOR = [
    (111, 265, 6),  #banco
    (129, 265, 7), #agência
    (151, 265, 8), #conta
    (119, 251, 4)  #CNPJ - fornecedor
]


TIMESBVALORTOTAL = [(176, 265, 'Valor_total')]  #valor

TIMESB8ALINHADO = [
    (104, 258, 'Nome_empresa')
]

TIMESB8HISTORICO = [(21, 231, 'Empresa')]

TIMESB9 = [
    (115, 275, 'Transferência Eletrônica Disponível - TED -"E"'),
    (10, 269, 'Instituição Financeira Remetente'),
    (104, 269, 'Instituição Financeira Destinatária'),
    (82, 269, "Uso do Banco"),
    (84, 196, 'Assinatura do Remetente')
]

TIMESB9PAGAMENTO = [
    (35, 87, "SEI"),
    (68, 87, "Cotação"),
    (93, 87, "DANFE"),
    (116, 87, "Valor total"),
    (141, 87, "IRRF / ISS"),
    (168, 87, "Valor líquido")
]

TIMESB12 = [
    (127, 283, 0),
    (181, 283, 1)

]

PONTILHADO = (8, 192, 196, 192)
#cnv.drawString(self.mm(146), self.mm(283 - contador), f"{conta[1]} - {conta[2]}")