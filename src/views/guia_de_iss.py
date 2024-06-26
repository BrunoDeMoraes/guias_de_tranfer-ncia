from src.views.coordenadas.coordenadas_iss import *
from src.views.guia import Guia

from typing import Dict


class GuiaDeISS(Guia):
    def __init__(self, dados: Dict, logo):
        super().__init__(dados, logo)

    def gerar_guia(self):
        for i in range(0, 2):
            self.inserir_logo(LOGO)
            self.gerar_linhas(LINHAS_ESTRUTURA, self.contador)
            self.gerar_retangulos(RETANGULOS, self.contador)
            self.inserir_strings('Times-Roman', 6, TIMES6, self.contador)
            self.inserir_strings('Times-Roman', 7, TIMES7, self.contador)
            self.inserir_strings('Times-Roman', 7, TIMES7DATA, self.contador, self.dados)
            self.inserir_strings('Times-Roman', 8, TIMES8, self.contador)
            self.inserir_strings('Times-Bold', 8, TIMESB8, self.contador)
            self.inserir_strings('Times-Bold', 7, TIMESB8HISTORICO, self.contador, self.dados)
            self.inserir_strings('Times-Bold', 9, TIMESB9, self.contador)
            self.inserir_strings('Times-Bold', 9, TIMESB8CONTA, self.contador, self.dados['Conta_origem'])
            #self.inserir_strings('Times-Bold', 8, TIMESB8FORNECEDOR, self.contador, self.dados['Dados_empresa'])
            self.inserir_strings('Times-Bold', 9, TIMESBVALORTOTAL, self.contador, self.dados)
            self.inserir_strings('Times-Bold', 12, TIMESB12, self.contador, self.dados['Conta_origem'])
            #self.gerar_linhas_texto_alinhado('Times-Bold', 7, TIMESB7NOMEEMPRESA, 'Nome_empresa', 3)
            self.gerar_linhas_texto_alinhado('Times-Bold', 9, TIMESB7EXTENSO, 'Total_extenso', 4)
            self.contador += 80
        self.contador = 0
        self.gerar_retangulos(RETANGULOSTITULO, self.contador)
        self.gerar_linhas(LINHASTPGAMENTO, self.contador)
        self.inserir_strings('Times-Bold', 7, TIMESB9PAGAMENTO, self.contador)
        self.gerar_area_de_pagamentos(LINHAS_PAGAMENTOS, RETANGULO_PAGAMENTO, TIMES8_PAGAMENTOS)
        self.inserir_pontilhado(PONTILHADO)
        self.cnv.save()


if __name__ == "__main__":
    teste = GuiaDeISS()
    teste.gerar_guia()