TABELAS = (
    'CREATE TABLE contas (origem text, recurso text, tipo text, banco text, agencia text, numero text, cnpj texto)',
    'CREATE TABLE urls (variavel text, url text)'
)

CONTAS = ('SELECT * FROM contas')

URLS = ('SELECT * FROM urls')

CONSULTA_TABELAS = "SELECT name FROM sqlite_master WHERE type='table';"