import pytz
from decouple import config
from datetime import datetime


def log_erro(dsc_erro, sql=None, list_parametros=None):
    dsc_log_query = ''
    if sql:
        f"""
            Params. da query: {list_parametros}
            {sql}
        """
    horario_atual = datetime.now().astimezone(tz=pytz.timezone(config('TIMEZONE'))).strftime('%d/%m/%Y %H:%M:%S')

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

def log_acesso_banco(json_request, response, status, dsc_ip):
    import json

    
    json_response = json.dumps(response)
    from db.conectar import executar_query
    sql="""
        insert into vetor_palavras.log_acesso 
        (json_req, json_response, num_status_code, dsc_ip)
        values (%s, %s, %s, %s)
    """
    tpl_dados, linhas_inseridas = executar_query(sql,True, [json_request, json_response, status, dsc_ip])
