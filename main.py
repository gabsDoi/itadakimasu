import os
import time

restaurantes_cadastrados = []

def nome_do_app():
    '''Defini o título do app'''
    print('''
- - - Itadakimasu - - -
          ''')

def opcoes():
    '''Mostra o nome das opções'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizando_app():
    '''Finaliza o app'''
    os.system('cls')
    print('Encerrando o app...')
    time.sleep(1)
    os.system('cls')

def opcao_invalida():
    '''Mostra uma mensagem de erro caso algo der errado no código'''
    os.system('cls')
    print('Opção inválida! Digite novamente\n')
    main()

def exibir_subtitulo(texto):
    '''Exibe os subtítulos de cada opção escolhida'''
    os.system('cls')
    linha = '-' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print

def voltar_ao_menu_principal():
    '''Volta para o menu principal'''
    input('\nDigite uma tecla para voltar ao menu principal: ')
    os.system('cls')
    main()

def cadastrar_restaurante():
    '''Cadastra um novo restaurante
    
        Inputs:
        - nome_restaurante
        - tipo_restaurante

        Outputs:
        - print()
    
    '''
    exibir_subtitulo('Cadastrar restaurante')
    nome_restaurante = input('\nNome do restaurante: ')
    tipo_restaurante = input('\nTipo do restaurante: ')
    dados_do_restaurante = {'nome':nome_restaurante, 'tipo':tipo_restaurante, 'validação':False}
    restaurantes_cadastrados.append(dados_do_restaurante)
    if dados_do_restaurante in restaurantes_cadastrados:
        print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso')
        voltar_ao_menu_principal()
    else:
        print('Não foi possível cadastrar seu restaurante! Tente novamente\n')
        main()

def listar_restaurantes():
    '''Lista os restaurantes cadastrados'''
    exibir_subtitulo('Restaurantes listados')
    if restaurantes_cadastrados == []:
        print('Não há restaurantes cadastrados!\n')
    else:
        print(f'{'Nome'.ljust(22)} {'Tipo'.ljust(22)} Status')
        for restaurante in restaurantes_cadastrados:
            nome = restaurante['nome']
            tipo = restaurante['tipo']
            validacao = 'ativado' if restaurante['validação'] else 'desativado'
            print(f'| {nome.ljust(20)} | {tipo.ljust(20)} | {validacao}')
    voltar_ao_menu_principal()

def ativar_ou_desativar_restaurante():
    '''Ativa ou desativa os restaurantes
    
        Inputs:
        - pesquisar_restaurante

        Outputs:
        - mensagem
    
    '''
    exibir_subtitulo('Ativar/Desativar Restaurante')
    pesquisar_restaurante = input('Digite o nome do restaurante que deseja ativar/desativar: ')
    restaurante_encontrado = False

    for restaurante in restaurantes_cadastrados:
        if pesquisar_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['validação'] = not restaurante['validação']
            mensagem = f'O restaurante {pesquisar_restaurante} foi ativado com sucesso' if restaurante['validação'] else f'O restaurante {pesquisar_restaurante} foi desativado com sucesso'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    
    voltar_ao_menu_principal()

def escolher_opcao():
    '''Apresenta as funções de cada opção
    
        Inputs:
        - opcao_escolhida
    
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            ativar_ou_desativar_restaurante()
        elif opcao_escolhida == 4:
            finalizando_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    nome_do_app()
    opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()