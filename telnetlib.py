import getpass
import telnetlib

HOST = "192.168.122.71" # variável recebe endereço IP do R1
user = input("Enter your telnet Username: ") # customizando o texto padrão (opcional)  
password = getpass.getpass()

tn = telnetlib.Telnet(HOST) # usando a biblioteca telnetlib para "telnetting" o IP contido em "HOST"

tn.read_until(b"Username: ") # mudar do padrão "login" para "Username"
tn.write(user.encode('ascii') + b"\n") # insere o usuário digitado na variável "user" 
if password:
	tn.read_until(b"Password: ") # vai esperar a senha da variável "Password"
	tn.write(password.encode('ascii') + b"\n") # escreve senha contida na variável "Password"

tn.write(b"enable\n") # "escreve" o comando enable no router
tn.write(b"cisco\n") # "escreve" a senha de enable configurada antes
tn.write(b"conf t\n") # "escreve" o comando que acessa o modo de configuração global
tn.write(b"int loop0\n") # "escreve" o comando que adiciona uma interface de loopback 0
tn.write(b"ip add 1.1.1.1 255.255.255.255\n")  # "escreve" o comando que seta o ip na interface loopback 0
tn.write(b"end\n") # "escreve" o comando que finaliza a configuração  
tn.write(b"exit\n") # "escreve" o comando que encerra a conexão telnet

print(tn.read_all().decode('ascii'))
