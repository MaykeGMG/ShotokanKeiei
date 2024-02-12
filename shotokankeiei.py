import mysql.connector

while True:
    conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'M0rs3_DB_0I',
    database = 'shotokankeieidb'
    )
    cursor = conexao.cursor()
    try:
        def inserir_aluno():
        
            num_users = int(input('Quantos Alunos deseja cadastrar?\n  '))

            for c in range(num_users):
                dados = []
                dados.append(input('\nInforme o Nome do Aluno: '))
                dados.append(input('\nInforme o Email do Aluno: '))
                dados.append(input('\nInforme o Telefone do Aluno: '))
                dados.append(input('\nInforme a Idade do Aluno: '))
                dados.append(input('\nInforme o peso do Aluno: '))
                dados.append(input('\nInforme a Cor da Faixa do Aluno: '))
                dados.append(input('\nInforme a Data de Exame do Aluno: '))
                dados.append(input('\nInforme o Tempo de Treino do Aluno(em meses): '))

                comm_inserirA = f'''insert into aluno (nome, email, telefone, idade, peso, faixa, data_exame, tempo_treino) values("{dados[0]}","{dados[1]}","{dados[2]}","{dados[3]}","{dados[4]}","{dados[5]}","{dados[6]}","{dados[7]}")'''
                print('\nAluno Inserido!')
                cursor.execute(comm_inserirA)
                conexao.commit()
        
        def cadastrar_evento():

            dados = []
            dados.append(input('\nInforme o Nome do Evento: '))
            dados.append(input('\nInforme a data do Evento: '))

            comm_inserirE = f'''insert into evento (nome, data, alunos_inscritos) values("{dados[0]}","{dados[1]}")'''
            print('\nEvento Cadastrado!')
            cursor.execute(comm_inserirE)
            conexao.commit()

        # def deletar():
        
        #     id_cliente = int(input('Qual o ID do Cliente que deseja deletar?\n  '))
        #     comm_delete = f'''delete from cliente where id_cliente = {id_cliente}'''
        #     print('Cliente Deletado!')
        #     cursor.execute(comm_delete)
        #     conexao.commit()

        def atualizar_aluno():
        
            new_atributo = input('O que deseja modificar (nome/email/telefone/idade/peso/faixa/tempo_treino):\n →')
            modificar = input(f'Insira o novo valor no {new_atributo}: ')
            id_aluno = int(input('Informe o ID do Aluno: '))
            comm_atualizar = f'''update aluno set {new_atributo} = "{modificar}" where id = {id_aluno}'''
            cursor.execute(f'''select nome from aluno where id_aluno = {id_aluno}''')
            resultado_nome = cursor.fetchall()
            print(f'o atributo {new_atributo} do Aluno {resultado_nome} foi Atualizado!')
            cursor.execute(comm_atualizar)
            conexao.commit()

        def buscar_id():
        
            id = int(input('Informe o ID do Aluno: '))
            comm_busca = f'''select * from aluno
            where id = {id}'''
            cursor.execute(comm_busca)
            resultado = cursor.fetchall()
            for linha in resultado:
                print('-' * 50)
                print(f' ID: {linha[0]} \n Nome: {linha[1]} \n Telefone: {linha[2]} \n Email: {linha[3]} \n Idade: {linha[6]} \n Peso: {linha[7]} \n Faixa: {linha[4]} \n Data do Exame: {linha[5]} \n Tempo de Treino: {linha[8]} meses')
                print('-' * 50)

        def buscar_nome():
        
            comm_busca = '''select * from aluno
            where nome like %s'''
            buscar = input('Insira o nome do aluno que busca: ')
            cursor.execute(comm_busca, [buscar+'%',])
            resultado = cursor.fetchall()
            for linha in resultado:
                print('-' * 50)
                print(f' ID: {linha[0]} \n Nome: {linha[1]} \n Telefone: {linha[2]} \n Email: {linha[3]} \n Idade: {linha[6]} \n Peso: {linha[7]} \n Faixa: {linha[4]} \n Data do Exame: {linha[5]} \n Tempo de Treino: {linha[8]} meses')
                print('-' * 50)

        while True:
            print('-' * 50)
            print(''' 1 - Inserir Aluno \n 2 - Atualizar Aluno \n 3 - Buscar Aluno por Nome \n 4 - Buscar Aluno por ID \n 5 - Cadastrar Evento \n 0 - Sair''')
            print('-' * 50)
            opcao = int(input('Escolha a opção: '))
            if opcao == 1:
                inserir_aluno()
            elif opcao == 2:
                atualizar_aluno()
            elif opcao == 3:
                buscar_nome()
            elif opcao == 4:
                buscar_id()
            # elif opcao == 5:
            #     deletar()
            elif opcao == 0:
            
                print('Sessão Encerrada!')
                print('-'*50)
                break
    except EOFError:
        continue
    except ValueError:
    
        print('\n ERROR - Você informou um valor não permitido!')

    cursor.close()
    conexao.close()
    break