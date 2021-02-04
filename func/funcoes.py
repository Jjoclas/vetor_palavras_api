def prepara_arquivo(list_arquivos):
    import re
    import nltk
    from nltk.corpus import stopwords
    from string import punctuation
    
    list_conteudo = []
    list_nomes =    []

    for arquivo in list_arquivos:
        list_conteudo.append(str(arquivo.read().decode('utf-8')))
        stop_words = set(stopwords.words('portuguese') + list(punctuation))
        list_nomes.append(arquivo.filename)

    #retirando possiveis espaços duplos e colocando tudo em minusculo
    list_conteudo =         list(map(lambda string: " ".join(string.split()).lower(), list_conteudo))
    dsc_conteudo_geral =    ''
    dict_arquivos =         {}

    for dsc_nome, dsc_conteudo in zip(list_nomes, list_conteudo):
        
        #retirando stop words.
        list_sem_stop_word = [palavra for palavra in dsc_conteudo if palavra not in stop_words]
        
        dict_arquivos[dsc_nome] = list_sem_stop_word
        dsc_conteudo_geral += f"{dsc_conteudo_geral} {' '.join(list_sem_stop_word)}"
    
    return {
        'arquivos':             dict_arquivos,
        'list_vocabulario_un':  list(set(dsc_conteudo_geral.split(' ')))
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
        dict_vetores_arquivos[nome_arquivo] = [list_vocabulario.count(palavra) for palavra in arquivos[nome_arquivo]] 

    return {
        'vocabulario': list_vocabulario,
        'vetores' : dict_vetores_arquivos
    }