import tkinter as tk
from tkinter import font

root = tk.Tk()

# Obter uma lista de todas as fontes disponíveis
font_list = font.families()
print(font_list)

root.destroy()
