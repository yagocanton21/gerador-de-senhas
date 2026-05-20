import tkinter as tk
from tkinter import ttk
from main import gerar_senha_core

# Definição das cores (Paleta Dark Moderna)
COLOR_BG = "#0f172a"          # Fundo principal (Slate-900)
COLOR_CARD = "#1e293b"        # Fundo do card central (Slate-800)
COLOR_ENTRY = "#0d131f"       # Fundo da exibição da senha
COLOR_TEXT = "#f8fafc"        # Texto principal
COLOR_TEXT_MUTED = "#94a3b8"  # Texto secundário
COLOR_ACCENT = "#10b981"      # Verde esmeralda vibrante (alto contraste)
COLOR_ACCENT_HOVER = "#059669" # Verde esmeralda escuro no hover
COLOR_GREEN = "#10b981"       # Verde (Sucesso/Forte)
COLOR_ORANGE = "#f59e0b"      # Laranja (Médio)
COLOR_RED = "#ef4444"         # Vermelho (Fraca)
COLOR_CYAN = "#06b6d4"        # Ciano (Muito Forte)

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Senhas Seguro")
        self.root.geometry("450x580")
        self.root.configure(bg=COLOR_BG)
        self.root.resizable(False, False)

        # Variáveis de controle
        self.tamanho_var = tk.IntVar(value=12)
        self.chk_upper_var = tk.BooleanVar(value=True)
        self.chk_lower_var = tk.BooleanVar(value=True)
        self.chk_number_var = tk.BooleanVar(value=True)
        self.chk_symbol_var = tk.BooleanVar(value=True)
        self.senha_gerada = tk.StringVar(value="")

        self.setup_ui()
        self.gerar_senha()

    def setup_ui(self):
        # Container Central (Card)
        card = tk.Frame(self.root, bg=COLOR_CARD, bd=0, highlightthickness=1, highlightbackground="#334155")
        card.place(relx=0.5, rely=0.5, anchor="center", width=400, height=520)

        # Título do App
        lbl_title = tk.Label(
            card, text="Gerador de Senhas", 
            font=("Plus Jakarta Sans", 18, "bold"), 
            bg=COLOR_CARD, fg=COLOR_TEXT
        )
        lbl_title.pack(pady=(20, 5))

        lbl_subtitle = tk.Label(
            card, text="Gere senhas fortes e seguras localmente", 
            font=("Plus Jakarta Sans", 9), 
            bg=COLOR_CARD, fg=COLOR_TEXT_MUTED
        )
        lbl_subtitle.pack(pady=(0, 20))

        # Box de exibição da senha
        display_frame = tk.Frame(card, bg=COLOR_ENTRY, bd=0)
        display_frame.pack(fill="x", padx=30, pady=(0, 10))

        self.entry_senha = tk.Entry(
            display_frame, textvariable=self.senha_gerada,
            font=("Courier New", 14, "bold"), bg=COLOR_ENTRY, fg=COLOR_TEXT,
            bd=0, justify="center", state="readonly", readonlybackground=COLOR_ENTRY
        )
        self.entry_senha.pack(side="left", fill="both", expand=True, padx=(15, 5), pady=12)

        # Botão de Copiar
        self.btn_copy = tk.Button(
            display_frame, text="📋", font=("Segoe UI Symbol", 12),
            bg=COLOR_CARD, fg=COLOR_TEXT_MUTED, activebackground=COLOR_ACCENT, activeforeground="#ffffff",
            bd=0, cursor="hand2", width=3, command=self.copiar_senha
        )
        self.btn_copy.pack(side="right", fill="y", padx=5, pady=5)
        self.btn_copy.bind("<Enter>", lambda e: self.btn_copy.config(fg=COLOR_TEXT))
        self.btn_copy.bind("<Leave>", lambda e: self.btn_copy.config(fg=COLOR_TEXT_MUTED))

        # Medidor de Força
        strength_frame = tk.Frame(card, bg=COLOR_CARD)
        strength_frame.pack(fill="x", padx=30, pady=(0, 20))

        lbl_strength_title = tk.Label(
            strength_frame, text="Força da Senha:", 
            font=("Plus Jakarta Sans", 8, "bold"), bg=COLOR_CARD, fg=COLOR_TEXT_MUTED
        )
        lbl_strength_title.pack(side="left")

        self.lbl_strength = tk.Label(
            strength_frame, text="Forte", 
            font=("Plus Jakarta Sans", 8, "bold"), bg=COLOR_CARD, fg=COLOR_GREEN
        )
        self.lbl_strength.pack(side="right")

        # Barra de força (Custom Canvas)
        self.canvas_strength = tk.Canvas(card, height=6, bg=COLOR_ENTRY, highlightthickness=0)
        self.canvas_strength.pack(fill="x", padx=30, pady=(0, 20))

        # Frame de Configurações
        settings_frame = tk.LabelFrame(
            card, text=" Configurações ", font=("Plus Jakarta Sans", 9, "bold"),
            bg=COLOR_CARD, fg=COLOR_TEXT, bd=1, relief="flat",
            highlightthickness=1, highlightbackground="#1e293b"
        )
        settings_frame.pack(fill="x", padx=30, pady=(0, 25))

        # Slider de Tamanho
        slider_frame = tk.Frame(settings_frame, bg=COLOR_CARD)
        slider_frame.pack(fill="x", padx=15, pady=(15, 10))

        lbl_length_desc = tk.Label(
            slider_frame, text="Tamanho:", font=("Plus Jakarta Sans", 9),
            bg=COLOR_CARD, fg=COLOR_TEXT_MUTED
        )
        lbl_length_desc.pack(side="left")

        self.lbl_length_val = tk.Label(
            slider_frame, text="12", font=("Courier New", 11, "bold"),
            bg=COLOR_CARD, fg=COLOR_ACCENT
        )
        self.lbl_length_val.pack(side="right")

        # Configurando o estilo do slider no ttk
        style = ttk.Style()
        style.theme_use('default')
        style.configure("TScale", background=COLOR_CARD, troughcolor=COLOR_ENTRY, sliderthickness=15)

        self.slider = ttk.Scale(
            settings_frame, from_=4, to=32, variable=self.tamanho_var,
            orient="horizontal", style="TScale", command=self.on_slider_move
        )
        self.slider.pack(fill="x", padx=15, pady=(0, 15))

        # Checkboxes Grid
        chk_frame = tk.Frame(settings_frame, bg=COLOR_CARD)
        chk_frame.pack(fill="x", padx=15, pady=(0, 15))

        self.create_checkbox(chk_frame, "Maiúsculas (A-Z)", self.chk_upper_var, 0, 0)
        self.create_checkbox(chk_frame, "Minúsculas (a-z)", self.chk_lower_var, 0, 1)
        self.create_checkbox(chk_frame, "Números (0-9)", self.chk_number_var, 1, 0)
        self.create_checkbox(chk_frame, "Símbolos (!@#$)", self.chk_symbol_var, 1, 1)

        # Botão Principal "Gerar Senha" (Usando Label para renderizar a cor perfeitamente no macOS)
        self.btn_generate = tk.Label(
            card, text="Gerar Senha Forte", font=("Plus Jakarta Sans", 11, "bold"),
            bg=COLOR_ACCENT, fg="#ffffff", cursor="hand2", pady=10
        )
        self.btn_generate.pack(fill="x", padx=30, pady=(0, 10))
        self.btn_generate.bind("<Button-1>", lambda e: self.gerar_senha())
        self.btn_generate.bind("<Enter>", lambda e: self.btn_generate.config(bg=COLOR_ACCENT_HOVER))
        self.btn_generate.bind("<Leave>", lambda e: self.btn_generate.config(bg=COLOR_ACCENT))

        # Label de Status/Mensagem
        self.lbl_status = tk.Label(
            card, text="", font=("Plus Jakarta Sans", 8),
            bg=COLOR_CARD, fg=COLOR_TEXT_MUTED
        )
        self.lbl_status.pack(pady=(5, 0))

    def create_checkbox(self, parent, text, variable, row, col):
        chk = tk.Checkbutton(
            parent, text=text, variable=variable, font=("Plus Jakarta Sans", 8),
            bg=COLOR_CARD, fg=COLOR_TEXT_MUTED, activebackground=COLOR_CARD, activeforeground=COLOR_TEXT,
            selectcolor=COLOR_ENTRY, bd=0, command=self.verificar_checkboxes
        )
        chk.grid(row=row, column=col, sticky="w", pady=4, padx=5)

    def verificar_checkboxes(self):
        # Evita que o usuário desmarque todas as caixas
        options = [self.chk_upper_var, self.chk_lower_var, self.chk_number_var, self.chk_symbol_var]
        if not any(opt.get() for opt in options):
            self.chk_lower_var.set(True) # Garante que pelo menos um permaneça ativo
            self.lbl_status.config(text="⚠️ Selecione ao menos um requisito!", fg=COLOR_RED)
            self.root.after(2000, lambda: self.lbl_status.config(text=""))
        self.gerar_senha()

    def on_slider_move(self, value):
        val = int(float(value))
        self.tamanho_var.set(val)
        self.lbl_length_val.config(text=str(val))
        self.gerar_senha()

    def gerar_senha(self):
        tamanho = self.tamanho_var.get()
        usar_upper = self.chk_upper_var.get()
        usar_lower = self.chk_lower_var.get()
        usar_number = self.chk_number_var.get()
        usar_symbol = self.chk_symbol_var.get()

        # Chama a função core do arquivo main.py (o backend)
        senha_final = gerar_senha_core(
            tamanho,
            usar_maiusculas=usar_upper,
            usar_minusculas=usar_lower,
            usar_numeros=usar_number,
            usar_simbolos=usar_symbol
        )

        if not senha_final:
            return

        total_pools = sum([usar_upper, usar_lower, usar_number, usar_symbol])
        
        self.senha_gerada.set(senha_final)
        self.atualizar_forca(senha_final, total_pools)

    def atualizar_forca(self, senha, total_pools):
        length = len(senha)
        score = 0
        
        if length >= 8: score += 2
        if length >= 12: score += 2
        if length >= 16: score += 2
        score += total_pools

        # Atualiza a cor e o tamanho da barra no Canvas
        self.canvas_strength.delete("all")
        width = 340 # Largura da barra
        
        if score < 4 or length < 6:
            texto = "Fraca"
            cor = COLOR_RED
            fill_pct = 0.25
        elif score >= 4 and score <= 6:
            texto = "Média"
            cor = COLOR_ORANGE
            fill_pct = 0.50
        elif score >= 7 and score <= 8:
            texto = "Forte"
            cor = COLOR_GREEN
            fill_pct = 0.75
        else:
            texto = "Muito Forte"
            cor = COLOR_CYAN
            fill_pct = 1.00

        self.lbl_strength.config(text=texto, fg=cor)
        
        # Desenha o progresso da barra
        self.canvas_strength.create_rectangle(
            0, 0, width * fill_pct, 6, fill=cor, outline=""
        )

    def copiar_senha(self):
        senha = self.senha_gerada.get()
        if senha:
            self.root.clipboard_clear()
            self.root.clipboard_append(senha)
            self.lbl_status.config(text="✨ Senha copiada para a área de transferência!", fg=COLOR_GREEN)
            # Limpa o status depois de 3 segundos
            self.root.after(3000, lambda: self.lbl_status.config(text=""))

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
