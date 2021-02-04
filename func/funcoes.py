def le_arquivo(list_arquivos):
    import re

    list_conteudo = []
    list_nomes =    []

    for arquivo in list_arquivos:
        list_conteudo.append(arquivo.read())
        list_nomes.append(arquivo.filename)
    #retirando possiveis espaços duplos e colocando tudo em minusculo
    list_conteudo = map(lambda string: " ".join(string.split()).lower(), list_conteudo)
    dsc_conteudo_geral =    ''
    dict_arquivos =         {}

    for dsc_nome, dsc_conteudo in zip(list_nomes, list_conteudo)
        dict_arquivos[dsc_nome] = dsc_conteudo
        dsc_conteudo_geral += f'{dsc_conteudo_geral} {dsc_conteudo}'
    
    return {
        'arquivos':             dict_arquivos
        'list_vocabulario_un':  list(set(dsc_conteudo_geral.split(' ')))
    }   

