import unittest
from func.funcoes import monta_vetor

class Verifica_monta_vetor(unittest.TestCase):
    def test_monta_vetor(self):
        _input_n_gram = 1
        _input_dict_arquivos = {
                    'arquivos': {
                        'texto1.txt': ['falar', 'fácil', 'mostreme', 'código'],
                        'texto2.txt': ['fácil', 'escrever', 'código', 'difícil', 'escrever', 'código', 'funcione']},
                        'list_vocabulario_un': ['falar', 'fácil', 'mostreme', 'código', 'falar', 'fácil', 'mostreme', 'código', 'fácil', 'escrever', 'código', 'difícil', 'escrever', 'código', 'funcione']
                }
        _output = {
            "vocabulario": ["falar","fácil","mostreme","código","falar","fácil","mostreme","código","fácil","escrever","código","difícil","escrever","código","funcione"],
            "vetores": {
                "texto1.txt": [1,1,1,1,1,1,1,1,1,0,1,0,0,1,0],
                "texto2.txt": [0,1,0,2,0,1,0,2,1,2,2,1,2,2,1]}
        }
        response = monta_vetor(_input_dict_arquivos, _input_n_gram)


        self.assertEqual(_output, response)