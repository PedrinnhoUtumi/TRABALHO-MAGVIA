from cx_Freeze import setup, Executable
import os

script = "main.py"

caminhoImagem = os.path.join(os.path.dirname(os.path.abspath(__file__)), './site/magvia.png')
executables = [Executable(script, base=None)]

setup(
    name="Gravador Serial",
    version="1.0",
    description="Software em Python para que consiga-se gravar em placas, suas informações mais úteis",
     options={"build_exe": {"include_files": [caminhoImagem]}},
    executables=executables
)
