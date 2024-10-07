# DDFarm
Automação de farm no ddtank 337

Projeto de Farm de CF e Instâncias Únicas no DDTank
Este projeto é um script automatizado desenvolvido para farmar instâncias únicas no jogo DDTank. Ele utiliza ferramentas de reconhecimento de imagem e automação de teclado para navegar e executar ações no jogo automaticamente.

Requisitos
Para executar este script, você precisará dos seguintes softwares e bibliotecas:

Python 3.10+: Certifique-se de que o Python esteja corretamente instalado e configurado no seu sistema.
Link: https://www.python.org/downloads/

Bibliotecas Python:

pyautogui: Para automação do teclado e mouse.
opencv-python: Para reconhecimento de imagem e manipulação da tela.
numpy: Para manipulação de arrays e imagens.
Instale as dependências com o seguinte comando no CMD:

pip install pyautogui opencv-python numpy
Imagem de Referência: As imagens usadas para reconhecimento (como botões de instância, habilidades, etc.) precisam estar disponíveis no caminho especificado no script. Garanta que as imagens estejam na pasta imagens no diretório correto.

Como Funciona
O script faz capturas de tela em tempo real e compara com as imagens de referência fornecidas. Quando encontra um item correspondente (botões, ícones ou outros elementos do jogo), ele simula cliques e pressiona teclas para executar as ações correspondentes.
*****OBSERVAÇÃO*****
Para que o bot rode é necessario entrar em uma sala de instancia(esse será o ponto de partida), após isso inicie o bot.

Funcionalidades principais:
Reconhecimento de botões e menus.
Ajuste automático do ângulo do disparo para 20.
Clicando em habilidades, ataques, e realizando ações específicas.
Farm automático em instâncias únicas.
Como Usar
Garanta que o jogo DDTank esteja aberto e posicionado corretamente para que o script possa reconhecer os elementos na tela.

******Certifique-se de que as imagens de referência estejam configuradas corretamente no caminho especificado no script.**********
mude todos os caminhos conforme o caminho da pasta imagens que baixou junto com os arquivos de execução, exemplo:
imagem=r'D:\Scripts\bot ddt\imagens\escolhe_instancia.png'   troque o caminho para o caminho novo  ----> imagem=r'C:\EXEMPLO\bot ddt\imagens\escolhe_instancia.png'
****OBSERVAÇÃO***
Não altere os nomes das variaveis de imagem.

Execute o script com o seguinte comando no CMD:

python bot_ddt.py
O bot começará a rodar automaticamente, repetindo o processo de farm nas instâncias. Ele irá localizar os botões, ajustar o ângulo e realizar o ataque.

Condição de parada:
Para parar a execução do bot use o comando ctrl + c.

Estrutura do Projeto
bot_ddt.py: Arquivo principal do script.
imagens/: Diretório que contém todas as imagens usadas para reconhecimento no script.
