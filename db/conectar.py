import psycopg2
from psycopg2 import pool
from decouple import config
from func.log_erro import log_erro

num_limite_conexoes =       config('LIMITE_CONEXOES')
list_conexoes_disponiveis = [num for num in range(num_limite_conexoes)]
list_conexoes_utilizadas =  []

user = config('DATABASE_URL').split("//")[1].split(":")[0]
password = config('DATABASE_URL').split("//")[1].split(":")[1].split("@")[0]
host = config('DATABASE_URL').split("//")[1].split(":")[1].split("@")[1]
database = config('DATABASE_URL').split("//")[1].split(":")[2].split("/")[1]

def cria_connection_pool():
    global conn_pool
    global conn
    try:
        conn_pool = psycopg2.pool.ThreadedConnectionPool(1, num_limite_conexoes, config('DATABASE_URL'))
        conn = conn_pool.getconn()
        conn.set_client_encoding('UTF8')
        conn.autocommit = True
    except psycopg2.Error as e:
        log_erro(e.pgerror)

# Inicializa o pool de conexões ao inciar o servidor
cria_connection_pool()


def executar_query(sql, commit=False, parametros_sql=[], **kwargs):
    global conn_pool
    global list_conexoes_disponiveis
    global list_conexoes_utilizadas

    if not conn_pool:
        cria_connection_pool()
    
    num_chave_conexao = None

    # Checa disponibilidade das conexões
    if list_conexoes_disponiveis:
        num_chave_conexao = list_conexoes_disponiveis.pop()
        list_conexoes_utilizadas.append(num_chave_conexao)
    else:
        list_conexoes_utilizadas.append(list_conexoes_utilizadas.pop(0))
        list_conexoes_utilizadas.append(list_conexoes_utilizadas[0])
        num_chave_conexao = list_conexoes_utilizadas[0]
      
    conn_local = conn_pool.getconn(num_chave_conexao)

    if conn_local.get_transaction_status() == 0: # 0 = conexão nova; 2 = Conexão já criada; 3 = Conexão com erro
        conn_local.set_client_encoding('UTF8')
    try:
        cursor = conn_local.cursor()
        
        #Utilizado para facilitar o desenvolvimento da aplicação;( Printa a query que foi executada com os parâmetros. )
        if 'debug' in kwargs:
            print(cursor.mogrify(sql, parametros_sql).decode('UTF-8'))

        cursor.execute("SET TIME ZONE '" + config('TIMEZONE') + "'")
        cursor.execute(sql, parametros_sql)
        conn_local.commit()
    
    except Exception as exe:
        if not conn_local.closed: # == 0 Conexao aberta; != 0 Conexao fechada ou com erro
            conn_local.rollback()

        log_erro(sql, parametros_sql, exe.__str__())

        raise Exception
    
    list_conexoes_utilizadas.remove(num_chave_conexao)
    
    if num_chave_conexao not in list_conexoes_utilizadas:
        list_conexoes_disponiveis.append(num_chave_conexao)

    num_rowcount = cursor.rowcount
    try:
        tpl_dados = cursor.fetchall()

    except psycopg2.ProgrammingError:
        tpl_dados = ()
    cursor.close()

    return {
        'dados':        tpl_dados,
        'num_linhas':   num_rowcount
    }

    
