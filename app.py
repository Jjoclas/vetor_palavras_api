import json
from flask import Flask, request, jsonify, make_response, Response
from decouple import config
from func.log import log_acesso_banco

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
    log_acesso_banco(request, dict_retorno, num_status, request.remote_addr)
    return Response(json.dumps(dict_retorno), status=num_status)



@application.route('/api', methods=['POST'])
def api():
    dict_retorno =      {}
    num_status =        500 
    
    if not request.form and not request.files:
        dict_retorno = {
            'status': 'erro',
            'msg': 'Favor realize a requisicao como form-data.'
        }
        num_status=401


    dsc_tipo_retorno =  request.form.get('tipo_retorno')
    list_arquivos =     request.files.getlist('files[]') 

    if not dsc_tipo_retorno:
        dict_retorno = {
            'status': 'erro',
            'msg': 'Favor informe o tipo de retorno desejado, chave:(tipo_retorno).'
        }
        num_status=401

    if not list_arquivos:
        dict_retorno = {
            'status': 'erro',
            'msg': 'Os arquivos nao foram informados, chave:(files[]).'
        }
        num_status=401
    


    log_acesso_banco(request, dict_retorno, num_status, request.remote_addr)
    return Response(json.dumps(dict_retorno), status=num_status)




if __name__ == "__main__":
    application.debug = True
    application.run(threaded=True, host="0.0.0.0")
