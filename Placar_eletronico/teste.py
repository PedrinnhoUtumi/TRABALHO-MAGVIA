import os
from PIL import Image

image_path = "C:\Users\magvi\OneDrive\Documentos\GitHub\TRABALHO-MAGVIA\TRABALHO-MAGVIA\Placar_eletronico\magvia.png"

if os.path.exists(image_path):
    imagem = Image.open(image_path)
    # Continue com o processamento da imagem
else:
    print(f"Erro: Arquivo '{image_path}' não encontrado.")
