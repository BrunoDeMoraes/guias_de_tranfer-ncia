from typing import Dict
# import dados_da_view
# import transfer_controller
from src.models.repository.dados_de_conta import DadosDeContas
from src.models.repository.dados_de_fornecedores import DadosDeFornecedores
from src.models.repository.dados_de_pagamento_repository import DadosDePagamentoRepository


def transfer_constructor(entrada: Dict):

    contas = DadosDeContas()
    data_pagameto = entrada['data']
    fornecedores = DadosDeFornecedores()
    origem = entrada['origem']
    pagamementos = DadosDePagamentoRepository()






    if pagamentos:
        return 'DEU CERTO!!!'
    else:
        return 'Deu merda!!!'


    # enviar_dados_pra_view((self, pagamentos, empresa, conta, origem, data_pagamento))






