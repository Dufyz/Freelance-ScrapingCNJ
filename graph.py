import tkinter as tk
from main import processo
import pandas as pd

def execute_main():
    selected_state = selected_state_var.get()
    
    if selected_state:
        selected_index = states.index(selected_state)
        result_label.config(text=f"Estado selecionado: {selected_index}")
        # Criando dataframe
        data = {
            'Denominacao': [""],
            'Situacao': [""],
            'Atribuicoes': [""],
            'Responsavel': [""],
            'Substituto': [""],
            'UF': [""],
            'Municipio': [""],
            'Telefone Principal': [""],
            'Telefone Secundario': [""],
            'Email': [""],
        }

        dataframe_final = pd.DataFrame(data)

        dataframe_final = processo(selected_index, dataframe_final)
        dataframe_final = dataframe_final.drop(index = 0)
        dataframe_final.to_excel(f"{selected_state}.xlsx")

    else:
        result_label.config(text="Nenhum estado selecionado.")

# Lista de estados do Brasil
states = [
    "RS", "SC", "PR", "SP", "RJ", "ES", "MG", "BA",
    "SE", "AL", "PE", "PB", "RN", "CE",
    "PI", "MA", "TO", "GO", "DF", "MS", "MT",
    "RO", "PA", "RR", "AM", "AC", "AP"
]

# Criação da janela principal
root = tk.Tk()
root.title("Seleção de Estado")

# Variável para armazenar o estado selecionado
selected_state_var = tk.StringVar()

# Criação dos radiobuttons
for state in states:
    radiobutton = tk.Radiobutton(root, text=state, variable=selected_state_var, value=state)
    radiobutton.pack(anchor="w")

# Botão para executar a ação
execute_button = tk.Button(root, text="Executar", command=execute_main)
execute_button.pack(pady=20)

# Rótulo para exibir resultados
result_label = tk.Label(root, text="", fg="green")
result_label.pack()

# Inicialização da interface gráfica
root.mainloop()
