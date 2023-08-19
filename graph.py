import tkinter as tk
import subprocess

def execute_main():
    try:
        subprocess.run(["python", "main.py"], check=True)
    except subprocess.CalledProcessError:
        result_label.config(text="Erro ao executar o arquivo.")

# Criação da janela principal
root = tk.Tk()
root.title("Executar Arquivo .py")

# Botão para executar arquivo main.py
execute_button = tk.Button(root, text="Executar", command=execute_main)
execute_button.pack(pady=20)

# Rótulo para exibir resultados ou erros
result_label = tk.Label(root, text="", fg="red")
result_label.pack()

# Inicialização da interface gráfica
root.mainloop()
