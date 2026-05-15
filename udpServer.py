from socket import *

serverPort = 12000

# 1. Cria o socket UDP (AF_INET = IPv4, SOCK_DGRAM = UDP)
serverSocket = socket(AF_INET, SOCK_DGRAM)

# 2. Vincula o socket a TODAS as interfaces de rede da máquina, na porta 12000
serverSocket.bind(('', serverPort))

print("Servidor pronto para receber mensagens")

# 3. Loop infinito: servidor fica escutando para sempre
while True:
    # 4. Aguarda uma mensagem (até 2048 bytes) e captura o endereço do cliente
    message, clientAddress = serverSocket.recvfrom(2048)

    # 5. Decodifica os bytes recebidos, converte para maiúsculas
    modifiedMessage = message.decode().upper()

    print(f"Mensagem recebida de {clientAddress}: {message.decode()}")

    # 6. Envia a resposta de volta para o endereço do cliente
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)