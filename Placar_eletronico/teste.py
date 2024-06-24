import tkinter as tk
from datetime import datetime, timedelta

class CronometroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronômetro Regressivo")
        
        self.cronometro_label = tk.Label(self.root, text="00:00:00.0", font=("Arial", 24))
        self.cronometro_label.pack(pady=20)

        self.tempo_inicial = None
        self.update()

    def update(self):
        if self.tempo_inicial:
            tempo_atual = datetime.now()
            tempo_decorrido = tempo_atual - self.tempo_inicial
            tempo_restante = timedelta(seconds=60) - tempo_decorrido  # Contagem regressiva de 1 minuto (60 segundos)

            if tempo_restante.total_seconds() <= 0:
                self.cronometro_label.config(text="00:00:00.0")
                print("Contagem regressiva concluída")
                return
            
            total_milliseg = int(tempo_restante.total_seconds() * 10)
            hr, resto = divmod(total_milliseg, 36000)
            min, resto = divmod(resto, 600)
            seg, milisseg = divmod(resto, 10)
            tempo_formatado = f"{int(hr):01}:{int(min):02}:{int(seg):02}.{int(milisseg):01}"
            self.cronometro_label.config(text=tempo_formatado)

        self.root.after(100, self.update)

    def start_timer(self):
        self.tempo_inicial = datetime.now()
        self.update()

if __name__ == "__main__":
    root = tk.Tk()
    app = CronometroApp(root)
    
    start_button = tk.Button(root, text="Iniciar Contagem Regressiva", command=app.start_timer)
    start_button.pack(pady=10)
    
    root.mainloop()
