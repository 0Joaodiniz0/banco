import colorama
from colorama import Fore,Style,Back
from tqdm import tqdm 
import time

colorama.init(autoreset = True)

operacao = 12
saldo = 0
extrato = []
usuario = ('João')
senha = ('zxcvbnm')

print('\n')
print(f'{Fore.RED}--------------{Fore.RESET}{Fore.BLUE}CADASTRO{Fore.RESET}{Fore.RED}--------------{Fore.RESET}'.center(30))
print('\n')
usuario1 = input(f"{Fore.LIGHTMAGENTA_EX}USUARIO{Fore.RESET}\n")
senha1 = input(f"{Fore.LIGHTMAGENTA_EX}SENHA{Fore.RESET}\n")
print('\n')
print('\n')

print(f'{Back.BLUE} CARREGANDO....... {Back.RESET}')
print('\n')

for i in tqdm(range(100)):
     time.sleep(0.1)
    

if usuario == usuario1 and senha == senha1 :
    print('\n')
    print(f'Bem vindo {usuario}')
    
    while operacao != 0:
        print('\n')
        print('1 - sacar\n'
            '2 - depositar\n'
            '3 - saldo\n'
            '4 - extrato\n'
            '0 - sair\n')
        
        operacao = int(input('Digite um numero: '))
        
        if operacao == 1:
            saque = float(input('quanto você deseja sacar: '))
            if saldo < saque:
                print('------------------------------------')
                print(f'{Fore.RED}SALDO INSULFICIENTE{Fore.RESET}' .center(43))
                print('------------------------------------')
            else:    
                print('------------------------------------')
                print(f'sacando {Fore.RED} R$ {saque:.2f}{Fore.RESET}')
                print('------------------------------------')
                print('\n')
                saldo -= saque
                extrato.append(f'{Fore.BLACK}Saque:{Fore.RESET} {Fore.RED}- R${saque}{Fore.RESET} ')

        elif operacao == 2:
            deposito =float(input('quanto você deseja depositar: '))
            print('-------------------------------------------')
            print(f'deposito de {Fore.BLUE} R$ {deposito:.2f}{Fore.RESET} efeutado com sucesso')
            print('-------------------------------------------')
            print('\n')
            saldo += deposito 
            extrato.append(f'{Fore.BLACK}Deposito:{Fore.RESET} {Fore.GREEN}+R${deposito} {Fore.RESET}')

        elif operacao == 3:
            print('-------------------------------------------')
            print (f'seu saldo é de {Fore.GREEN} R$ {saldo:.2f}{Fore.RESET}')
            print('-------------------------------------------')
            
        elif operacao == 4:
            print('------------------------------------')
            print('gerando seu extrato.......')
            print('------------------------------------\n\n')
            for item in extrato:
                print(item)
            print('')
            print(f'Seu saldo atual é: {Back.GREEN}{Fore.GREEN} R$ {saldo:.2f} {Style.RESET_ALL}')
                    
        elif operacao == 0:
            print('------------------------------------')
            print('saindo')
            print('------------------------------------') 

        else:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!') 
            print(f'...........{Fore.RED} ERRO FATAL{Fore.RESET}...........')
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('DIGITE OUTRO NÚMERO' .center(30))
            print('')

else:
    print('------------------------------------')
    print(f'{Fore.RED}USUARIO NÃO CADASTRADO{Fore.RESET}')
    print('------------------------------------')