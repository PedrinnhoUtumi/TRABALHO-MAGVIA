import tkinter as tk

def on_map(event):
    print("Widget mapeado na tela")

root = tk.Tk()

label = tk.Label(root, text="Hello, World!")
label.pack()

label.bind("<Map>", on_map)

root.mainloop()
