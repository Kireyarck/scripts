from random import randint
import os


os.system("PS1='> '")
os.system("clear")

# Códigos ANSI para cores
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"


print(f'{GREEN}		SCRIPT INICIALIZADO{GREEN}\n')


opc = int(input("Digite 1 para binarios \nDigite 2 Para Contagem Infinita\n\n"))

if opc == 1:
	while True:
		print(f'{GREEN}{randint(0,1)}{GREEN}',end="")
if opc == 2:
	nun = 0
	while True:
		print(f'{GREEN}{nun}{GREEN}',end="")
		nun += 1
else: 
	pass		





