import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from models.ranges import RangesRFI 
from models.card_grid import CardGrid 

class PokerHandAnalyzer:
    def __init__(self):
        self.num_players = 2
        self.root = tk.Tk()
        self.root.title("Analisador de Mãos - Poker Texas Hold'em")
        self.setup_ui()

    def setup_ui(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Número de jogadores
        ttk.Label(frame, text="Número de jogadores (2-10):").grid(row=0, column=0)
        self.entry_players = ttk.Entry(frame)
        self.entry_players.insert(0, "2")
        self.entry_players.grid(row=0, column=1)
        ttk.Button(frame, text="Atualizar", command=self.update_players).grid(row=0, column=2)

        # Posicao
        ttk.Label(frame, text="Posição na mesa:").grid(row=1, column=0)
        self.combo_position = ttk.Combobox(frame, values=list(RangesRFI.RANGES.keys()), state="readonly")
        self.combo_position.grid(row=1, column=1)
        self.combo_position.set("UTG")

        # Entrada de cartas
        ttk.Label(frame, text="Par de cartas:").grid(row=2, column=0)
        self.entry_hand = ttk.Entry(frame)
        self.entry_hand.grid(row=2, column=1)
        ttk.Button(frame, text="Calcular", command=self.calculate_hand).grid(row=2, column=2)

        # Resultado
        self.result_label = ttk.Label(frame, text="", foreground="blue")
        self.result_label.grid(row=3, column=0, columnspan=3)

        # Imagem
        self.load_image(frame)

    def load_image(self, frame):
        ttk.Label(frame, text="Selecione a carta na imagem:").grid(row=4, column=0, columnspan=3)
        img = Image.open("C:/Poker_Hand_Analyzer/img/ranges_pre_flop.png")
        img = img.resize((650, 650), Image.Resampling.LANCZOS)
        self.img_tk = ImageTk.PhotoImage(img)
        self.canvas = tk.Canvas(frame, width=650, height=650)
        self.canvas.grid(row=5, column=0, columnspan=3)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img_tk)
        self.canvas.bind("<Button-1>", self.on_image_click)

    def update_players(self):
        try:
            value = int(self.entry_players.get())
            if 2 <= value <= 10:
                self.num_players = value
            else:
                raise ValueError("O número de jogadores deve estar entre 2 e 10.")
        except ValueError as e:
            self.result_label["text"] = str(e)

    def calculate_hand(self):
        position = self.combo_position.get()
        hand = self.entry_hand.get().upper()
        if RangesRFI.is_in_range(position, hand):
            self.result_label["text"] = f"Mão {hand} está no range RFI para {position} | Jogadores: {self.num_players}"
        else:
            self.result_label["text"] = f"Mão {hand} NÃO está no range RFI para {position} | Jogadores: {self.num_players}"

    def on_image_click(self, event):
        card = CardGrid.get_card(event.x, event.y)
        if card:
            self.entry_hand.delete(0, tk.END)
            self.entry_hand.insert(0, card)

    def run(self):
        self.root.mainloop()