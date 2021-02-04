import pytz
from decouple import config
from datetime import datetime


def log_erro(dsc_erro, sql=None, parametros=None):
    dsc_log_query = ''
    if sql:
        f"""
            Params. da query: {parametros}
            {sql}
        """
    horario_atual = datetime.now().astimezone(tz=pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%Y %H:%M:%S')

    conteudo_erro = f"""
    ----------------- {horario_atual} -----------------
    Desc. do Erro: {dsc_erro}
    {dsc_log_query}
    """
    try:
        with open(f"{config('LOG_ERRO')}log_erro.txt", 'a') as arquivo:
            arquivo.write(conteudo_erro)
    except Exception as e:
        print('Erro ao salvar log de erro.')
        print(e.__str__())

