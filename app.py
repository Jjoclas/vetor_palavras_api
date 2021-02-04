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
    dsc_tipo_retorno = request.json.get('tipo_retorno')
    file_texto       = request.files.get('files')
    print(file_texto)
    print(dict(request.files))
    return 'deu certo'




if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production application.
    application.debug = True
    application.config['JSON_SORT_KEYS'] = False
    application.config['JSON_AS_ASCII'] = False
    application.run(threaded=True, host="0.0.0.0")
