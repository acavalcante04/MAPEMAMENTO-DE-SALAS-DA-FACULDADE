# Importa o dicionário "blocos" e a função "inserir_bloco" do módulo estudos.blocos_un
# O dicionário "blocos" armazena todos os blocos já cadastrados
# A função "inserir_bloco" é usada para adicionar um novo bloco caso ele ainda não exista
from blocos_un import blocos, inserir_bloco

# Cria um dicionário vazio para armazenar informações gerais de todas as salas registradas
# Esse dicionário funciona como um controle independente dos blocos/andares
salas = {}

def inserir_sala():
    """
    Função responsável por inserir uma sala no sistema.
    Ela pede ao usuário o ID da sala e o nome, identifica a que bloco e andar a sala pertence,
    e então atualiza tanto o dicionário geral de salas quanto a estrutura de blocos.
    """

    # Solicita ao usuário o ID da sala (formato esperado: número do andar + letra do bloco + número da sala)
    # Exemplo: "1A01" = 1º andar, bloco A, sala 01
    salas_id = input('insira o id da sala (ex: 1a01, 2b05): ')
    
    # Solicita ao usuário o nome da sala (descrição mais clara do ambiente)
    salas_name = input('insira o nome da sala (ex: Laboratório de Informática, Sala de Reuniões): ')
    
    # Extrai o número do andar a partir do primeiro caractere do ID (sempre um dígito)
    andar_num = int(salas_id[0])
    
    # Extrai a letra do bloco a partir do segundo caractere do ID e converte para maiúscula
    letra = str(salas_id[1]).upper()
    
    # Extrai o número da sala (todos os caracteres restantes do ID após andar e bloco)
    numero_sala = salas_id[2:]

    # Verifica se o ID da sala já está cadastrado no dicionário geral "salas"
    # Se já existir, a função apenas avisa e encerra sem adicionar novamente
    if salas_id in salas:
        print(f'Sala {salas_id} já existe.')
        return
    
    # Se o bloco já existir no dicionário "blocos"
    if letra in blocos:
        
        # Caso o andar já exista dentro do bloco especificado
        if andar_num in blocos[letra]:
            # Adiciona o número da sala na lista de salas daquele andar
            blocos[letra][andar_num]['salas'].append(numero_sala)
            
            # Cria um dicionário para a sala dentro do andar, armazenando seu nome
            blocos[letra][andar_num][numero_sala] = {'nome': salas_name}
        
        # Caso o andar ainda não exista no bloco
        elif andar_num not in blocos[letra]:
            print(f'Andar {andar_num} não encontrado no bloco {letra}.')
        
        # Caso contrário, cria um novo andar no bloco e já inicializa com a sala
        else:
            blocos[letra][andar_num] = {'salas': [numero_sala]}
    
    # Se o bloco ainda não existir no dicionário "blocos"
    else:
        print(f'Bloco {letra} não encontrado.')
        
        # Chama a função para inserir um novo bloco
        inserir_bloco()
        
        # Depois de criar o bloco, chama novamente a função de inserção de sala
        # para tentar adicionar a sala agora que o bloco existe
        inserir_sala()
    
    # Registra a sala também no dicionário geral "salas"
    # Aqui são armazenados: bloco, andar e número da sala
    salas[salas_id] = {
        'bloco': letra,
        'andar': andar_num,
        'numero_sala': numero_sala,
        'nome_sala': salas_name
    }
    
    print(f'Sala {salas_id} inserida com sucesso.')

def listar_salas():
    """
    Função responsável por listar todas as salas cadastradas no dicionário geral "salas".
    Exibe ID, bloco, andar, número e nome de cada sala.
    """
    
    # Se nenhuma sala foi registrada ainda, exibe uma mensagem
    if not salas:
        print('Nenhuma sala cadastrada.')
        return
    
    # Caso haja salas cadastradas, percorre o dicionário e exibe seus detalhes
    print('Salas cadastradas:')
    for sala_id, detalhes in salas.items():
        print(f"ID: {sala_id}, Bloco: {detalhes['bloco']}, Andar: {detalhes['andar']}, Número da Sala: {detalhes['numero_sala']}, Nome: {detalhes['nome_sala']}")
