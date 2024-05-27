import serial
from datetime import datetime
import tkinter as tk

class SeuApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Configuração da porta serial
        self.porta_serial = serial.Serial('COM5', baudrate=115200, timeout=1)
        
        # Inicia o cronômetro
        self.contador = datetime.now()
        
        # Inicia a interface gráfica
        self.cronometro = tk.StringVar()
        self.label_cronometro = tk.Label(self, textvariable=self.cronometro, font=("Arial", 24))
        self.label_cronometro.pack(padx=10, pady=10)
        
        # Atualiza o cronômetro a cada segundo
        self.update_cronometro()
    
    def update_cronometro(self):
        if self.contador:
            tempo = datetime.now() - self.contador
            total_milliseconds = int(tempo.total_seconds() * 10)
            horas, resto = divmod(total_milliseconds, 36000)
            minutos, resto = divmod(resto, 600)
            segundos, milissegundos = divmod(resto, 10)
            valor_cronometro = f"{int(horas):02}:{int(minutos):02}:{int(segundos):02}.{int(milissegundos):01}"
            
            # Atualiza o valor do cronômetro na interface gráfica
            self.cronometro.set(valor_cronometro)
            
            # Envia o valor do cronômetro pela porta serial
            self.porta_serial.write(valor_cronometro.encode())
        
        # Chama a função update_cronometro novamente após 1 segundo
        self.after(1000, self.update_cronometro)

# Inicia o aplicativo
app = SeuApp()
app.mainloop()
