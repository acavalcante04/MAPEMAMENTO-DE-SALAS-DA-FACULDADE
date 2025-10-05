# Dicionário que guarda os blocos registrados.
# Cada chave será a letra do bloco (ex: 'A', 'B') e o valor será uma lista
# com os andares já registrados para aquele bloco (ex: ['Térreo', '1º Andar']).
blocos = {}  # dicionário vazio para armazenar os blocos

# Função responsável por solicitar e registrar um novo bloco no dicionário `blocos`.
# Espera que o usuário informe um ID no formato: <número><letra>, por exemplo "1A" ou "2B".
def inserir_bloco():
    # Lê do usuário o identificador do bloco. O valor esperado contém um dígito
    # inicial representando o andar seguido da(s) letra(s) do bloco.
    bloco_id = input('insira o id do bloco (ex: 1A, 1B, 2B): ')

    # Extrai o primeiro caractere do ID e converte para inteiro para obter o número do andar.
    # Observação: se o usuário digitar algo inválido (não numérico na primeira posição),
    # esta linha lançará um ValueError — o código atual não trata essa exceção.
    andar_num = int(bloco_id[0])  # pega o primeiro caractere do id do bloco (que deve ser um numero) e define como andar_num

    # Extrai todo o restante do ID a partir do segundo caractere para obter a(s) letra(s) do bloco.
    # Em seguida, normaliza para maiúsculas para manter chave consistente no dicionário.
    letra = str(bloco_id[1:]).upper()  # pega o segundo elemento do bloco e define como a letra (maiuscula) de identificação do bloco
    
    # Converte o número do andar para uma descrição legível:
    # - Se o número for 1, entende-se que é o "Térreo".
    # - Para números >= 2, subtrai 1 e formata como "Xº Andar" (o código considera andar 1 = térreo).
    if andar_num == 1:  # se andar for igual a 1, definir como térreo
        andar = 'Térreo'
    else:  # se não for 1, definir como o número do andar menos 1 (porque o térreo é o primeiro andar)
        andar = f'{andar_num - 1}º Andar'

    # Se a letra do bloco ainda não existe como chave no dicionário `blocos`,
    # cria-se a chave com uma lista vazia que representará os andares daquele bloco.
    if letra not in blocos:
        blocos[letra] = []

    # Verifica se o andar extraído já está presente na lista de andares do bloco.
    # - Se não estiver presente, adiciona o andar à lista.
    # - Se já estiver presente, informa ao usuário que não é necessário re-adicionar.
    if andar not in blocos[letra]:  # se o andar não estiver na lista do bloco
        blocos[letra].append(andar)  # adiciona o andar na lista do bloco

        # Mensagem de confirmação para o usuário. Mantém duas mensagens diferentes
        # dependendo se foi o térreo (andar_num == 1) ou um andar superior.
        if andar_num == 1:
            print(f'Bloco {letra} adicionado com sicesso.')
        elif andar_num >= 2:
            print(f'Bloco {letra} adicionado com sicesso, {andar} atribuido ao bloco {letra}.')
    else:
        # Caso o andar já exista na lista do bloco, apenas informa que o registro já existe.
        print(f'O andar {andar} já está registrado no bloco {letra}.')

# Função que percorre o dicionário `blocos` e imprime cada bloco com sua lista de andares.
def listar_blocos():  # função para listar os blocos e seus andares
    # Se não houver nenhum bloco cadastrado (dicionário vazio), informa ao usuário.
    if not blocos:  # se o dicionario blocos estiver vazio vai mostrar que nenhum bloco cadastrado
        print('Nenhum bloco cadastrado.')
    else:  # se tiver blocos cadastrados vai listar os blocos e seus andares
        print('Blocos cadastrados e seus andares:')

    # Itera sobre cada par (letra, andares) no dicionário `blocos`.
    # `letra` é a chave (ex: 'A') e `andares` é a lista de andares associada.
    for letra, andares in blocos.items():  # para cada letra (chave) e seus andares (valores) no dicionario blocos 
        # Converte cada elemento da lista de andares para string (caso não sejam strings)
        # e junta todos eles em uma única string separada por vírgulas para exibição amigável.
        andares_str = ', '.join(map(str, andares))  # converte cada andar para string e junta com vírgula
        print(f'Bloco {letra}: Andares {andares_str}')

# Loop principal do programa que apresenta um menu simples ao usuário.
# O loop se mantém ativo até que o usuário escolha a opção de sair (3).
while True:
    # Exibe o menu de opções: inserir bloco, listar blocos ou sair do programa.
    print('\n--- Menu de Blocos ---')
    print('1. Inserir bloco')
    print('2. Listar blocos')
    print('3. Sair')
    escolha = input('Escolha uma opção (1-3): ')

    # Roteia a escolha do usuário para a função correspondente.
    if escolha == '1':
        inserir_bloco()
    elif escolha == '2':
        listar_blocos()
    elif escolha == '3':
        # Mensagem de saída e interrupção do loop principal.
        print('Saindo do programa. Até mais!')
        break
    else:
        # Caso o usuário digite uma opção inválida (fora de 1-3), informa e reinicia o menu.
        print('Opção inválida. Tente novamente.')
