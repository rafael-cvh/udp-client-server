from socket import *

# 1. Coloque aqui o IP do computador onde o servidor está rodando
#    Para descobrir: no Windows rode "ipconfig", no Linux/Mac rode "ip a" ou "ifconfig"
serverName = '192.168.X.X'  # ← ALTERE PARA O IP REAL DO SERVIDOR 10.24.31.141
serverPort = 12000 # sudo ufw allow 12000/udp

# 2. Cria o socket UDP no cliente
clientSocket = socket(AF_INET, SOCK_DGRAM)

# 3. Lê a mensagem do usuário pelo terminal
message = input('Digite uma mensagem: ')

# 4. Envia a mensagem codificada em bytes para o servidor
clientSocket.sendto(message.encode(), (serverName, serverPort))

# 5. Aguarda a resposta do servidor (até 2048 bytes)
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# 6. Exibe a resposta e encerra o socket
print('Resposta do servidor:', modifiedMessage.decode())
clientSocket.close()