PGDMP     "    &                y            jyiulykp "   11.10 (Ubuntu 11.10-1.pgdg20.04+1)    12.2     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    4134908    jyiulykp    DATABASE     z   CREATE DATABASE jyiulykp WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';
    DROP DATABASE jyiulykp;
                jyiulykp    false            �           0    0    DATABASE jyiulykp    ACL     ;   REVOKE CONNECT,TEMPORARY ON DATABASE jyiulykp FROM PUBLIC;
                   jyiulykp    false    4020            �            1259    4135725 
   log_acesso    TABLE       CREATE TABLE vetor_palavras.log_acesso (
    id_log_api integer NOT NULL,
    json_req json,
    dat_requisicao timestamp(0) without time zone DEFAULT now() NOT NULL,
    json_response json,
    num_status_code integer NOT NULL,
    dsc_ip character varying
);
 &   DROP TABLE vetor_palavras.log_acesso;
       vetor_palavras            jyiulykp    false            �            1259    4135723    log_chamadas_api_id_log_api_seq    SEQUENCE     �   CREATE SEQUENCE vetor_palavras.log_chamadas_api_id_log_api_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 >   DROP SEQUENCE vetor_palavras.log_chamadas_api_id_log_api_seq;
       vetor_palavras          jyiulykp    false    224            �           0    0    log_chamadas_api_id_log_api_seq    SEQUENCE OWNED BY     m   ALTER SEQUENCE vetor_palavras.log_chamadas_api_id_log_api_seq OWNED BY vetor_palavras.log_acesso.id_log_api;
          vetor_palavras          jyiulykp    false    223            .           2604    4135728    log_acesso id_log_api    DEFAULT     �   ALTER TABLE ONLY vetor_palavras.log_acesso ALTER COLUMN id_log_api SET DEFAULT nextval('vetor_palavras.log_chamadas_api_id_log_api_seq'::regclass);
 L   ALTER TABLE vetor_palavras.log_acesso ALTER COLUMN id_log_api DROP DEFAULT;
       vetor_palavras          jyiulykp    false    224    223    224            �          0    4135725 
   log_acesso 
   TABLE DATA           z   COPY vetor_palavras.log_acesso (id_log_api, json_req, dat_requisicao, json_response, num_status_code, dsc_ip) FROM stdin;
    vetor_palavras          jyiulykp    false    224            �           0    0    log_chamadas_api_id_log_api_seq    SEQUENCE SET     V   SELECT pg_catalog.setval('vetor_palavras.log_chamadas_api_id_log_api_seq', 29, true);
          vetor_palavras          jyiulykp    false    223            2           2606    4353314    log_acesso log_acesso_pk 
   CONSTRAINT     f   ALTER TABLE ONLY vetor_palavras.log_acesso
    ADD CONSTRAINT log_acesso_pk PRIMARY KEY (id_log_api);
 J   ALTER TABLE ONLY vetor_palavras.log_acesso DROP CONSTRAINT log_acesso_pk;
       vetor_palavras            jyiulykp    false    224            0           1259    4353315    log_acesso_id_log_api_idx    INDEX     ^   CREATE INDEX log_acesso_id_log_api_idx ON vetor_palavras.log_acesso USING btree (id_log_api);
 5   DROP INDEX vetor_palavras.log_acesso_id_log_api_idx;
       vetor_palavras            jyiulykp    false    224            �   k  x���n�8��N��⟽���6��~���VK�,R�[�JU��l�0c0��I�U�e~tb>��xƐŻ�O�<�z?? o/d��^����BfB]�</��|^PL�#���G��`�H���ET�ڎǥ����}�O�"�V&'�����Ę���R�d����P�#:q�W5�o/���"�d��uI�2TG�<�h��ݬ��#K_�����:T2m�����"ĸa\����B�|����M�~��c�C�]�����AזI�&�(7SN"����H&z�<��^7�n�d�����򷽯��n
ݼ�wx�Py;'�{��A7R7G�E_����^����_�������A�xż��2J�F^;2���J����Y�n���H���k��V+��:絮�ZLi(|�����B�n�H꫙�-��<���+]���Wu�,ND�W��E�89>Tj]��%Q=�����1��]�+�I.v���րd �.��Y�����<�Z�d��ze���^DM�M=ڰj�����0^؟�%��n��@[@���ϨhＫ��n"��A�^nm�B�:�:LȟEH-����P��Oh�(upt^�\,LNM~M�.tZ������p*7n\(�%��� J���j�ɥ����}�$w�#�]G5��:u��X&Q�U�0����;R`X�E4�5'@}SfP<P�~�z�8q���M��5�'��������9S�u!ҪM�Ph#�k`uO��R�����BJ^�2E���)E��\yQ�$+�<�#�
�e��U/����q�C����I/4j�&�`�g�w�?P\�M�������B�h0�	��`�����L_'&�s�gxA�T�_�O��G׉H�|G���q$V��Y/�q�.w�h�8�ն��� 4 ��hp�lV%I��4�^@�������Jo�ks�~�,^g�>?���T�&)P��2�0@^��N)��,��ވ���C�v�v*�]7-��7-l�7nT�u�H� ���PZ��:>e�d�QEF(ÐlS� 8�D<0�As��팵��g�f0���ޣ���, #���攼�_�{�W�n��9�h|��}]��n��^TM�5�Ї�� z� ��Z.�����[          �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    4134908    jyiulykp    DATABASE     z   CREATE DATABASE jyiulykp WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';
    DROP DATABASE jyiulykp;
                jyiulykp    false            �           0    0    DATABASE jyiulykp    ACL     ;   REVOKE CONNECT,TEMPORARY ON DATABASE jyiulykp FROM PUBLIC;
                   jyiulykp    false    4020            �            1259    4135725 
   log_acesso    TABLE       CREATE TABLE vetor_palavras.log_acesso (
    id_log_api integer NOT NULL,
    json_req json,
    dat_requisicao timestamp(0) without time zone DEFAULT now() NOT NULL,
    json_response json,
    num_status_code integer NOT NULL,
    dsc_ip character varying
);
 &   DROP TABLE vetor_palavras.log_acesso;
       vetor_palavras            jyiulykp    false            �            1259    4135723    log_chamadas_api_id_log_api_seq    SEQUENCE     �   CREATE SEQUENCE vetor_palavras.log_chamadas_api_id_log_api_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 >   DROP SEQUENCE vetor_palavras.log_chamadas_api_id_log_api_seq;
       vetor_palavras          jyiulykp    false    224            �           0    0    log_chamadas_api_id_log_api_seq    SEQUENCE OWNED BY     m   ALTER SEQUENCE vetor_palavras.log_chamadas_api_id_log_api_seq OWNED BY vetor_palavras.log_acesso.id_log_api;
          vetor_palavras          jyiulykp    false    223            .           2604    4135728    log_acesso id_log_api    DEFAULT     �   ALTER TABLE ONLY vetor_palavras.log_acesso ALTER COLUMN id_log_api SET DEFAULT nextval('vetor_palavras.log_chamadas_api_id_log_api_seq'::regclass);
 L   ALTER TABLE vetor_palavras.log_acesso ALTER COLUMN id_log_api DROP DEFAULT;
       vetor_palavras          jyiulykp    false    224    223    224            �          0    4135725 
   log_acesso 
   TABLE DATA           z   COPY vetor_palavras.log_acesso (id_log_api, json_req, dat_requisicao, json_response, num_status_code, dsc_ip) FROM stdin;
    vetor_palavras          jyiulykp    false    224   �       �           0    0    log_chamadas_api_id_log_api_seq    SEQUENCE SET     V   SELECT pg_catalog.setval('vetor_palavras.log_chamadas_api_id_log_api_seq', 29, true);
          vetor_palavras          jyiulykp    false    223            2           2606    4353314    log_acesso log_acesso_pk 
   CONSTRAINT     f   ALTER TABLE ONLY vetor_palavras.log_acesso
    ADD CONSTRAINT log_acesso_pk PRIMARY KEY (id_log_api);
 J   ALTER TABLE ONLY vetor_palavras.log_acesso DROP CONSTRAINT log_acesso_pk;
       vetor_palavras            jyiulykp    false    224            0           1259    4353315    log_acesso_id_log_api_idx    INDEX     ^   CREATE INDEX log_acesso_id_log_api_idx ON vetor_palavras.log_acesso USING btree (id_log_api);
 5   DROP INDEX vetor_palavras.log_acesso_id_log_api_idx;
       vetor_palavras            jyiulykp    false    224           