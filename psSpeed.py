import os

print('Selecione o sistema operacional:')
print('1 - Windows')
print('2 - Linux')

sistema_operacional = int(input('Digite o número: ')) 


# Verificando a opção do usuário
if sistema_operacional == 1:
    # Criando a variável
    ip_address_w = input("Digite o endereço IP do range, ex. 192.168.0.: ")    
    os.system(f'for /L %i in (1,1,255) do @ping -n 1 -w 200 {ip_address_w}%i > nul && echo {ip_address_w}%i está ativo.')
elif sistema_operacional == 2:
     ip_address_l = input("Digite o endereço IP da rede, ex. 192.168.0.1.: ")
     os.system(f'fping -ag {ip_address_l}/24 2> /dev/null')
else:
    print("Opção inválida!")
