import tkinter as tk
from tkinter import messagebox, scrolledtext
import subprocess
import threading
from PIL import Image, ImageTk

# Função para executar script com interface separada
def executar_script(script_path, script_name):
    # Cria uma nova janela para a execução do script
    janela_script = tk.Toplevel()
    janela_script.title(f"Execução: {script_name}")
    janela_script.geometry("500x400")

    # Função que será executada na thread para rodar o script e capturar o log
    def rodar_script():
        log_path = f"{script_name}_log.txt"
        try:
            with open(log_path, "w") as log_file:
                process = subprocess.Popen(["python", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                
                # Lendo a saída e erros em tempo real
                for line in process.stdout:
                    update_log(line.strip())  # Atualiza o log na interface
                    log_file.write(line + '\n')  # Salva no arquivo de log

                for error in process.stderr:
                    update_log(error.strip())  # Atualiza o log de erros
                    log_file.write(error + '\n')  # Salva erros no arquivo

            process.wait()
            update_log("Execução finalizada.")
        except Exception as e:
            update_log(f"Erro ao executar o script: {e}")

    # Botão de encerrar execução
    def encerrar_execucao():
        janela_script.destroy()

    encerrar_btn = tk.Button(janela_script, text="Encerrar Execução", command=encerrar_execucao)
    encerrar_btn.pack(pady=10)

    # Iniciar o script em uma thread separada
    threading.Thread(target=rodar_script).start()

# Função para executar o primeiro script
def executar_script_1():
    executar_script(r"D:\Scripts\bot ddt\bot_farm_CF.py", "Farm Dragão CF")

# Função para executar o segundo script
def executar_script_2():
    executar_script(r"D:\Scripts\bot ddt\bot_ddt.py", "Instância Única Erva Zamina")

# Criando a janela principal
janela = tk.Tk()
janela.title("DDFarm")
janela.geometry("600x400")

# Imagem de background
background_image = Image.open(r"D:\\Scripts\\bot ddt\\imagens\\background_img.JPG")  # Use o caminho completo da imagem
background_image = background_image.resize((600, 400), Image.LANCZOS)  # Ajusta o tamanho da imagem
bg_image = ImageTk.PhotoImage(background_image)

# Carregar o ícone da imagem
icone_image = ImageTk.PhotoImage(Image.open(r"D:\\Scripts\\bot ddt\\imagens\\LogoDDFarm.png"))

# Definir o ícone da janela
janela.iconphoto(False, icone_image)
# Canvas para o background
canvas = tk.Canvas(janela, width=600, height=400)
canvas.pack(fill="both", expand=True)

# Coloca a imagem no canvas
canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Título desenhado no Canvas
canvas.create_text(300, 20, text="Farm DDtank 337", font=("Helvetica", 24, "bold"), fill="black", anchor='center')

# Botão para executar o Script 1
botao1 = tk.Button(janela, text="Farm Dragão CF", width=25, command=executar_script_1)
botao1.place(relx=0.5, y=100, anchor='center')

# Botão para executar o Script 2
botao2 = tk.Button(janela, text="Farm Instância Única Erva Zamina", width=25, command=executar_script_2)
botao2.place(relx=0.5, y=140, anchor='center')

# Footer desenhado no Canvas
footer = canvas.create_text(550, 380, text="© 2024 - Dev Blooper", font=("Helvetica", 10), fill="gray", anchor='se')

# Inicia a janela
janela.mainloop()
