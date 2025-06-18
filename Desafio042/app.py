import tkinter as tk
from tkinter import ttk, messagebox
import math
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class ModernTriangleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GeoMath - Classificador de Triângulos")
        self.root.geometry("900x700")
        self.root.configure(bg='#f8f9fa')
        
        # Configuração de estilo
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Cores modernas
        self.primary_color = '#4e73df'
        self.secondary_color = '#2e59d9'
        self.accent_color = '#1cc88a'
        self.danger_color = '#e74a3b'
        self.light_bg = '#f8f9fc'
        self.dark_text = '#5a5c69'
        
        self.setup_ui()
    
    def setup_ui(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg=self.light_bg)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Cabeçalho moderno
        header_frame = tk.Frame(main_frame, bg=self.primary_color)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(header_frame, text="GEOMATH", font=('Montserrat', 24, 'bold'), 
                bg=self.primary_color, fg='white', padx=20, pady=15).pack()
        
        # Frame de entrada moderno
        input_frame = tk.Frame(main_frame, bg='white', bd=0, 
                             highlightbackground='#dddfeb', highlightthickness=1)
        input_frame.pack(fill=tk.X, pady=(0, 20), padx=10)
        
        tk.Label(input_frame, text="Medidas dos lados", font=('Montserrat', 12, 'bold'), 
                bg='white', fg=self.dark_text).pack(pady=(15, 10))
        
        # Estilo dos campos de entrada
        entry_style = {'font': ('Montserrat', 11), 'bg': '#f8f9fc', 
                      'bd': 1, 'relief': 'flat', 'highlightbackground': '#dddfeb',
                      'highlightthickness': 1, 'highlightcolor': self.primary_color}
        
        # Campos de entrada
        sides = ['A', 'B', 'C']
        self.entries = []
        for i, side in enumerate(sides):
            row_frame = tk.Frame(input_frame, bg='white')
            row_frame.pack(fill=tk.X, padx=20, pady=5)
            
            tk.Label(row_frame, text=f"Lado {side}:", font=('Montserrat', 10), 
                    bg='white', fg=self.dark_text).pack(side=tk.LEFT, padx=(0, 10))
            
            entry = tk.Entry(row_frame, **entry_style)
            entry.pack(side=tk.RIGHT, fill=tk.X, expand=True, ipady=5)
            self.entries.append(entry)
        
        # Botão moderno
        btn_frame = tk.Frame(main_frame, bg=self.light_bg)
        btn_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.calc_btn = tk.Button(btn_frame, text="CLASSIFICAR O TRIÂNGULO", 
                                 font=('Montserrat', 11, 'bold'),
                                 bg=self.primary_color, fg='white', 
                                 activebackground=self.secondary_color,
                                 relief='flat', bd=0, padx=20, pady=10,
                                 command=self.classify_triangle)
        self.calc_btn.pack(fill=tk.X, ipady=8)
        
        # Frame de resultados moderno
        result_frame = tk.Frame(main_frame, bg='white', bd=0,
                              highlightbackground='#dddfeb', highlightthickness=1)
        result_frame.pack(fill=tk.BOTH, expand=True, padx=10)
        
        # Canvas para o desenho do triângulo
        self.figure = Figure(figsize=(5, 4), dpi=100, facecolor='white')
        self.canvas = FigureCanvasTkAgg(self.figure, master=result_frame)
        self.canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Frame de informações
        info_frame = tk.Frame(result_frame, bg='white')
        info_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Classificação com destaque
        self.classification_frame = tk.Frame(info_frame, bg='#f8f9fc', bd=0,
                                           highlightbackground='#dddfeb', highlightthickness=1)
        self.classification_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.class_label = tk.Label(self.classification_frame, text="", 
                                  font=('Montserrat', 14, 'bold'), 
                                  bg='#f8f9fc', fg=self.primary_color,
                                  justify=tk.CENTER)
        self.class_label.pack(pady=15)
        
        # Detalhes
        details_frame = tk.Frame(info_frame, bg='white')
        details_frame.pack(fill=tk.BOTH, expand=True)
        
        self.details_label = tk.Label(details_frame, text="", 
                                    font=('Montserrat', 10), 
                                    bg='white', fg=self.dark_text,
                                    justify=tk.LEFT)
        self.details_label.pack(fill=tk.BOTH, expand=True, padx=10)
    
    def classify_triangle(self):
        try:
            # Obter valores dos lados
            a, b, c = [float(entry.get()) for entry in self.entries]
            
            # Validar entradas
            if a <= 0 or b <= 0 or c <= 0:
                messagebox.showerror("Erro", "Todos os lados devem ser valores positivos!")
                return
            
            # Verificar se forma triângulo
            if not (a + b > c and a + c > b and b + c > a):
                messagebox.showwarning("Aviso", "Estas medidas não formam um triângulo!")
                self.clear_results()
                return
            
            # Calcular ângulos
            def calculate_angle(x, y, z):
                return math.degrees(math.acos((y**2 + z**2 - x**2) / (2 * y * z)))
            
            angle_A = calculate_angle(a, b, c)
            angle_B = calculate_angle(b, a, c)
            angle_C = 180 - angle_A - angle_B
            
            # Calcular área
            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            
            # Determinar tipo com cores diferentes
            if a == b == c:
                triangle_type = "EQUILÁTERO"
                type_explanation = "Todos os três lados são iguais"
                color = self.accent_color
            elif a == b or a == c or b == c:
                triangle_type = "ISÓSCELES"
                type_explanation = "Dois lados são iguais"
                color = '#36b9cc'
            else:
                triangle_type = "ESCALENO"
                type_explanation = "Todos os lados são diferentes"
                color = self.danger_color
            
            # Atualizar a classificação
            self.class_label.config(
                text=f"Triângulo {triangle_type}\n{type_explanation}",
                fg=color
            )
            
            # Desenhar triângulo
            self.draw_triangle(a, b, c, angle_A, angle_B, angle_C, color)
            
            # Exibir informações detalhadas
            details_text = (
                f"Ângulos:\n"
                f"• Op. a Lado A: {angle_A:.2f}°\n"
                f"• Op. a Lado B: {angle_B:.2f}°\n"
                f"• Op. a Lado C: {angle_C:.2f}°\n\n"
                f"Medidas:\n"
                f"• Área: {area:.2f} u²\n"
                f"• Perímetro: {a+b+c:.2f} u\n"
                f"• Semi-perímetro: {s:.2f} u"
            )
            self.details_label.config(text=details_text)
            
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos!")
            self.clear_results()
    
    def draw_triangle(self, a, b, c, angle_A, angle_B, angle_C, color):
        self.figure.clear()
        ax = self.figure.add_subplot(111, facecolor='white')
        
        # Calcular coordenadas para posicionamento preciso
        x = [0, c, b * math.cos(math.radians(angle_A))]
        y = [0, 0, b * math.sin(math.radians(angle_A))]
        
        # Desenhar o triângulo
        triangle = plt.Polygon(list(zip(x, y)), closed=True, 
                              fill=True, color=color, alpha=0.3, ec='#2c3e50', lw=1.5)
        ax.add_patch(triangle)
        
        # Adicionar rótulos dos lados
        ax.text((x[0]+x[1])/2, (y[0]+y[1])/2 - 0.05*max(y), f"{c:.1f}", 
                ha='center', va='top', fontsize=10, color=self.dark_text)
        ax.text((x[0]+x[2])/2 - 0.05*max(x), (y[0]+y[2])/2, f"{b:.1f}", 
                ha='right', va='center', fontsize=10, color=self.dark_text)
        ax.text((x[1]+x[2])/2 + 0.05*max(x), (y[1]+y[2])/2, f"{a:.1f}", 
                ha='left', va='center', fontsize=10, color=self.dark_text)
        
        # Adicionar ângulos
        ax.text(x[0] + 0.1*a, y[0] + 0.1*max(y), f"{angle_A:.1f}°", 
                ha='center', va='bottom', fontsize=9, color=self.primary_color)
        ax.text(x[1] - 0.1*a, y[1] + 0.1*max(y), f"{angle_B:.1f}°", 
                ha='center', va='bottom', fontsize=9, color=self.primary_color)
        ax.text(x[2], y[2] - 0.1*max(y), f"{angle_C:.1f}°", 
                ha='center', va='top', fontsize=9, color=self.primary_color)
        
        # Configurar visualização
        ax.set_aspect('equal')
        margin = max(a, b, c) * 0.2
        ax.set_xlim(min(x)-margin, max(x)+margin)
        ax.set_ylim(min(y)-margin, max(y)+margin)
        ax.axis('off')
        
        self.canvas.draw()
    
    def clear_results(self):
        self.figure.clear()
        self.canvas.draw()
        self.class_label.config(text="")
        self.details_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    
    # Tentar carregar a fonte Montserrat (opcional)
    try:
        from tkinter import font
        font.nametofont("TkDefaultFont").configure(family="Montserrat")
    except:
        pass
    
    app = ModernTriangleApp(root)
    root.mainloop()