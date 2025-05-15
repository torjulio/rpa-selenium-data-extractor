import csv
import os

def salvar_csv(dados, caminho):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["Frase", "Autor"])
        writer.writeheader()
        writer.writerows(dados)
