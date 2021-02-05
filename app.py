import json
from flask import Flask, request, jsonify, make_response, Response
from decouple import config
from func.log import log_acesso_banco
from func.funcoes import monta_retorno

application = Flask('vetor_palavras')


@application.errorhandler(Exception)
def redirect_error(err):
    from func.log import log_erro
    if config('STAGE') == 'DEV':
        raise Exception
    log_erro(err.__str__())
    return server_error()


@application.route('/ops', methods=['GET'])
def server_error():
    dict_retorno =  {
        'status': 'erro',
        'msg': 'Ocorreu um erro ao processar a requisicao, tente novamente mais tarde.'
    }
    num_status = 500

    return monta_retorno(request, dict_retorno, num_status, request.remote_addr)


@application.route('/api', methods=['POST'])
def api():
    from func.funcoes import monta_vetor, prepara_arquivo

    dict_retorno =      {}
    num_status =        200 
    
    if not request.form and not request.files:
        dict_retorno = {
            'status': 'erro',
            'msg': 'Favor realize a requisicao como form-data.'
        }
        num_status=401


    num_gram =          request.form.get('n_gram', 1)
    list_arquivos =     request.files.getlist('files[]') 

    if isinstance(num_gram, str) and num_gram.isnumeric():
        num_gram = int(num_gram)
        
    if not num_gram:
        dict_retorno = {
            'status': 'erro',
            'msg': 'Favor informe o numero de palavras por posicao do vetor, chave:(n_gram).'
        }
        num_status=401

    if not list_arquivos:
        dict_retorno = {
            'status': 'erro',
            'msg': 'Os arquivos nao foram informados, chave:(files[]).'
        }
        num_status=401
    dict_arquivos = prepara_arquivo(list_arquivos)
    dict_retorno =  monta_vetor(dict_arquivos, num_gram)

    return monta_retorno(request, dict_retorno, num_status, request.remote_addr)




if __name__ == "__main__":
    application.debug = True
    application.run(threaded=True, host="0.0.0.0")
