import pyautogui
import time
import cv2
import numpy as np

# Função para localizar a imagem e clicar nela
def encontrar_e_clicar(imagem=r'D:\Scripts\bot ddt\imagens\escolhe_instancia.png', precisao=0.8, espera=1):
    # Captura a tela
    screenshot = pyautogui.screenshot()
    
    # Converte a captura da tela para um formato que o OpenCV entende (escala de cinza)
    tela = np.array(screenshot)
    tela = cv2.cvtColor(tela, cv2.COLOR_RGB2GRAY)  # Converte para escala de cinza
    
    # Carrega a imagem de referência
    referencia = cv2.imread(imagem, cv2.IMREAD_GRAYSCALE)  # Também carrega a imagem em escala de cinza
    
    if referencia is None:
        print(f"Erro: a imagem {imagem} não foi encontrada.")
        return False, None  # Retorna um valor padrão se a imagem não for encontrada
    
    # Procura a imagem na tela
    resultado = cv2.matchTemplate(tela, referencia, cv2.TM_CCOEFF_NORMED)
    
    # Localiza os pontos onde a imagem foi encontrada com precisão acima do limiar
    local = np.where(resultado >= precisao)

    # Se encontrar, faz o clique
    if len(local[0]) > 0:
        for pt in zip(*local[::-1]):
            pyautogui.click(pt[0], pt[1])  # Clique nas coordenadas
            time.sleep(espera)
            return True, local  # Retorna True e as coordenadas localizadas
    
    return False, None  # Retorna False se a imagem não for encontrada

# Função para ajustar o ângulo até 20
def ajustar_angulo_para_20(angulo_desejado=20):
    # Pressionar a tecla 'down' várias vezes para garantir que o ângulo está no mínimo
    for _ in range(50):
        pyautogui.press('down')
        time.sleep(0.02)  # Pequena pausa para cada pressionamento
        
    # Agora, pressionar 'up' até chegar a 20
 #   for _ in range(angulo_desejado):
 #       pyautogui.press('up')
 #       time.sleep(0.02)  # Pequena pausa para cada pressionamento
 #   
 #   pyautogui.press('right')  
 #  time.sleep(0.5)  

# Função para segurar a barra de espaço e carregar a força
def carregar_forca():
    pyautogui.keyDown('space')  # Pressiona espaço
    time.sleep(6)  # Segura por 'duracao' segundos para carregar força
    pyautogui.keyUp('space')  # Solta espaço para atirar

# Loop para o bot continuar executando
while True:
    # Aqui você adiciona as imagens e ações que o bot deve seguir
    found, _ = encontrar_e_clicar(r'D:\Scripts\bot ddt\imagens\escolhe_instancia.png')
    if found:
        print("Abrindo menu de instâncias.")
        time.sleep(1)  # Tempo para completar a instância

    found, _ = encontrar_e_clicar(r'D:\Scripts\bot ddt\imagens\instancia_unica_botton.png', precisao=0.7)
    if found:
        print("Mudando para instâncias Únicas.")
        time.sleep(1)

    found, _ = encontrar_e_clicar(r'D:\Scripts\bot ddt\imagens\guerreiro_2.png')
    if found:
        print("Guerreiro Trial 2 ativado.")
        time.sleep(2)

    found, _ = encontrar_e_clicar(r'D:\Scripts\bot ddt\imagens\dif_normal.png')
    if found:
        print("Dificuldade normal.")
        time.sleep(1)

    found, _ = encontrar_e_clicar(r'D:\Scripts\bot ddt\imagens\sim.png')
    if found:
        print("Ok.")
        time.sleep(1)

    found, _ = encontrar_e_clicar(r'D:\Scripts\bot ddt\imagens\inicio_botton.png', precisao=0.7)
    if found:
        print("Iniciando.")
        time.sleep(2)

    found, _ = encontrar_e_clicar(r'D:\Scripts\bot ddt\imagens\habilidade_pet.png')
    if found:
        print("Ataque do pet.")
        time.sleep(3)


    found, _ = encontrar_e_clicar(r'D:\Scripts\bot ddt\imagens\pow.png')
    if found:
        print("POW!!!!.")
        encontrar_e_clicar(r'D:\Scripts\bot ddt\imagens\+1.png')
        print("+1.")
        encontrar_e_clicar(r'D:\Scripts\bot ddt\imagens\+3.png')
        print("+3")
        encontrar_e_clicar(r'D:\Scripts\bot ddt\imagens\50.png', precisao=0.7)
        print("50%")
        encontrar_e_clicar(r'D:\Scripts\bot ddt\imagens\50.png', precisao=0.7)
        print("50%")
        carregar_forca()  # Chamada da função
        print("Atirando")
        time.sleep(1)

    found, _ = encontrar_e_clicar(r'D:\Scripts\bot ddt\imagens\+1.png')
    if found:
        print("+1.")
        encontrar_e_clicar(r'D:\Scripts\bot ddt\imagens\+2.png')
        print("Tridente")
        encontrar_e_clicar(r'D:\Scripts\bot ddt\imagens\50.png', precisao=0.7)
        print("50%")
        carregar_forca()  # Chamada da função
        print("Atirando")
        time.sleep(1)
    
    found, _ = encontrar_e_clicar(r'D:\Scripts\bot ddt\imagens\carta.png')
    if found:
        print("recolhido carta 1.")
        encontrar_e_clicar(r'D:\Scripts\bot ddt\imagens\carta.png')
        print("recolhido carta 2.")
        time.sleep(2)

    ajustar_angulo_para_20()

    # Pausa entre cada ciclo do loop
    time.sleep(1)
