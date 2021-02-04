from flask import Flask, request, jsonify, make_response, Response
from decouple import config

application = Flask('vetor_palavras')


@application.errorhandler(Exception)
def redirect_error(err):
    print(err)
    return server_error()


@application.route('/ops', methods=['GET'])
def server_error():
    return Response(json.dumps({
        'status': 'erro',
        'msg': 'Ocorreu um erro ao processar a requisicao, tente novamente mais tarde.'
    }), status=500)



@application.route('/api', methods=['POST'])
def home():
    dsc_tipo_retorno =  request.params.get('tipo_retorno')
    file_arquivos =     request.files.getlist('files[]')

    if not dsc_tipo_retorno:
        return Response(json.dumps({
            'status': 'erro',
            'msg': 'Favor informe o tipo de retorno desejado, chave:(tipo_retorno).'
        }), status=401)

    if not file_texto:
        return Response(json.dumps({
            'status': 'erro',
            'msg': 'Os arquivos não foram informados, chave:(files[]).'
        }), status=401)

    return 'deu certo'




if __name__ == "__main__":
    application.run(threaded=True, host="0.0.0.0")
