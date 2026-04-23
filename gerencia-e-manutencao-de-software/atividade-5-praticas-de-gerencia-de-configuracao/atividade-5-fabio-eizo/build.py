import os
import shutil
import subprocess
import sys


print("Iniciando a linha de montagem...")

comandos = [
    f"{sys.executable} -m pip install -r requirements.txt",
    f"{sys.executable} -m pytest teste_calculadora.py",
    f"{sys.executable} -m flake8 calculadora.py",
]

for comando in comandos:
    print(f"\nExecutando: {comando}")
    resultado = subprocess.run(comando, shell=True)
    if resultado.returncode != 0:
        print("\nA construção parou! Foi encontrado um erro.")
        sys.exit(resultado.returncode)

if os.path.exists("calculadora_build.zip"):
    os.remove("calculadora_build.zip")

shutil.make_archive("calculadora_build", "zip", root_dir=".", base_dir="calculadora.py")
print("\nArtefato gerado: calculadora_build.zip")
print("Construção finalizada com sucesso! Software pronto.")
