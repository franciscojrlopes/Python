import json
import time

def adicionar_item(compras, item, quantidade):
    compras[item] = quantidade

def remover_item(compras, item):
    if item in compras:
        del compras[item]
def visualizar_compras(compras):
    for item, quantidade in compras.items():
        print(f'{item}: {quantidade}')
print()
print('Pressione enter para continuar!')
input()

def salvar_compras(compras, nome_do_arquivo):
        with open(nome_do_arquivo, 'w') as arquivo:
            json.dump(compras, arquivo)

def carregar_compras(compras, nome_do_arquivo):
        with open(nome_do_arquivo, 'r') as arquivo:
             return json.load(arquivo)

def gerenciar_compras(compras, nome_arquivo=None): # Menu intermediário........... recebe compras.........
    while True:
         print('1 Adicionar item')
         print("2 Remover item")
         print("3 Visualizar lista")
         print("4 Salvar e sair")
         print("5 Sair sem salvar")
            # condicionais:
         escolha = input("Escolha uma opção: ")
         if escolha == '1':              
              item = input('Digite o nome do item: ')
              quantidade = float(input('Digite a quantidade: '))
              adicionar_item(compras, item, quantidade)

         elif escolha == '2':
              item = input('Digite o nome do item: ')
              remover_item(compras, item)
              
         elif escolha == '3':
              visualizar_compras(compras)
         
         elif escolha == '4':
              if nome_arquivo is None:
                 nome_arquivo = input('Digite o nome do arquivo pra salvar:   ')
              if not nome_arquivo.endswith('.json'):
                   nome_arquivo += '.json'
              salvar_compras(compras, nome_arquivo)
              break
         elif escolha == '5': # sair sem salvar break........
              break
         
         else:
             print('Opção inválida!')
             time.sleep(1)
def main():     # Menu principal........... compras entrou no if de escolha.......

    while True:
        print('1. Criar uma nova lista de compras')
        print('2. Carregar uma lista existente')
        print('3. Sair')
        escolha = input('Escolha uma opção: ')
        if escolha == '1': # escolha 1 vai criar o dicionário vazio...........
            compras = {}
            gerenciar_compras(compras)
        elif escolha == '2':
            pass
        elif escolha == '3':
            break
        else:
             print('Opção inválida!')
             time.sleep(1)
if __name__ == '__main__':
    main()


    