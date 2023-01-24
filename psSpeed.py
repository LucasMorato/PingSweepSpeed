# importar pacotes necessários
import socket
import subprocess
import os

print('Selecione o sistema operacional:')
print('1 - Windows')
print('2 - Linux')

sistema_operacional = int(input('Digite o número: ')) 

# Verificando a opção do usuário
if sistema_operacional == 1:
    if os.name == 'posix':
        print('Selecione a opcao Linux. Fechando.')
        exit(0)
    else:
        pass
    # definir nome do host
    hostname = socket.gethostname()

    # definir endereços IPV4, IPV6
    ipv4 = socket.gethostbyname(hostname)
    command = "ipconfig"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    ipv6 = ""

    for line in process.stdout.readlines():
        if "IPv6" in line.decode("utf-8"):
            ipv6 = line.decode("utf-8").split(" : ")[1].strip()

    # imprimir IPV4 e IPV6
    print("IPV4 deste host '{0}' é {1}".format(hostname, ipv4))
    print("IPV6 deste host '{0}' é {1}".format(hostname, ipv6))
    
    # Criando a variável
    ip_address_w = input(f"\nDigite o endereço IP da rede, ex. {ipv4.rsplit('.', 1)[0]}.1: ")    
    os.system(f'for /L %i in (1,1,255) do @ping -n 1 -w 200 {ip_address_w}%i > nul && echo {ip_address_w}%i está ativo.')
elif sistema_operacional == 2:
    if os.name == 'nt':
        print('Selecione a opcao Windows. Fechando...')
        exit(0)
    else:
        pass
    # executa o comando ifconfig e salva o resultado em uma variável
    output = subprocess.check_output(['ifconfig'])

    # Converte o resultado para uma string
    output = output.decode()

    # Procura pelo IPv4 e IPv6
    ipv4 = output.split('inet')[1].split()[0]
    ipv6 = output.split('inet6')[1].split()[0]

    # Mostra o resultado
    print('IPv4:', ipv4)
    print('IPv6:', ipv6)

    ip_address_l = input(f"\nDigite o endereço IP da rede, ex. {ipv4.rsplit('.', 1)[0]}.1: ")
    os.system(f'fping -ag {ip_address_l}/24 2> /dev/null')
else:
    print("Opção inválida!")
