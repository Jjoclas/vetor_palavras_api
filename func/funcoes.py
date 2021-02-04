def prepara_arquivo(list_arquivos):
    import re
    import nltk
    from nltk.corpus import stopwords
    from string import punctuation
    
    list_conteudo = []
    list_nomes =    []

    for arquivo in list_arquivos:
        #lendo o arquivo e transformando em lower case e removendo pontuações
        list_conteudo.append(str(arquivo.read().decode('utf-8').lower()).translate(str.maketrans('', '', punctuation)))
        stop_words = set(stopwords.words('portuguese'))
        list_nomes.append(arquivo.filename)

    #retirando stop words
    list_conteudo =         list(map(lambda string: [palavra for palavra in string.split(' ') if palavra not in stop_words], list_conteudo))
    dsc_conteudo_geral =    ''
    dict_arquivos =         {}

    for dsc_nome, lista_palavras in zip(list_nomes, list_conteudo):
        
        
        dict_arquivos[dsc_nome] = lista_palavras
        dsc_conteudo_geral += f"{dsc_conteudo_geral} {' '.join(lista_palavras)}"
    
    return {
        'arquivos':             dict_arquivos,
        'list_vocabulario_un':  list(set(filter(bool, dsc_conteudo_geral.split(' '))))
    }   

def monta_vetor(list_arquivos, n_gram):
    dict_arquivos = prepara_arquivo(list_arquivos)
    
    list_vocabulario =  dict_arquivos.get('list_vocabulario_un')
    print(list_vocabulario)
    arquivos =          dict_arquivos.get('arquivos', {})
    if n_gram > 1:
        list_vocabulario = [' '.join(list_vocabulario[i:i+n_gram]) for i, item in enumerate(list_vocabulario)]

    dict_vetores_arquivos = {}

    for nome_arquivo in arquivos:
        dict_vetores_arquivos[nome_arquivo] = [arquivos[nome_arquivo].count(palavra) for palavra in list_vocabulario] 

    return {
        'vocabulario': list_vocabulario,
        'vetores' : dict_vetores_arquivos
    }