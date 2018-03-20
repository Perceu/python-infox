import turtle
import tkinter as tk

class Example:

    def __init__(self, interface):
        self.interface = interface
        self.interface.title("Calculadora simples")


        # Criando Labels
        self.title = tk.Label(self.interface, text="Calculadora exemplo")
        self.label_1 = tk.Label(self.interface, text="valor 1:")
        self.label_2 = tk.Label(self.interface, text="valor 2:")
        self.saida = tk.Label(self.interface, text="")
        self.label_saida = tk.Label(self.interface, text="resultado")

        # Criando Entrys 
        self.entry_1 = tk.Entry(interface)
        self.entry_2 = tk.Entry(interface)

        # Criando Botões e registrando funções
        self.button_sum = tk.Button(self.interface, text="Somar", command=self.sum )
        self.button_sub = tk.Button(self.interface, text="Subtrair", command=self.sub )
        self.button_div = tk.Button(self.interface, text="Dividir", command=self.div )
        self.button_mult = tk.Button(self.interface, text="Multiplicar", command=self.mult )

        # Desenhando Entrada
        self.title.grid(row=0, column=0, columnspan=4, stick=tk.W+tk.E)
        
        # Desenhando Input 1
        self.label_1.grid(row=1, column=0)
        self.entry_1.grid(row=1, column=1, columnspan=3, stick=tk.W+tk.E)

        # Desenhando Input 2
        self.label_2.grid(row=2, column=0)
        self.entry_2.grid(row=2, column=1, columnspan=3, stick=tk.W+tk.E)

        self.label_saida.grid(row=3, column=0)
        self.saida.grid(row=3, column=1, columnspan=3, stick=tk.W+tk.E)

        # Desenhando Buttons
        self.button_sum.grid(row=5, column=0, stick=tk.W+tk.E)
        self.button_sub.grid(row=5, column=1, stick=tk.W+tk.E)
        self.button_div.grid(row=5, column=2, stick=tk.W+tk.E)
        self.button_mult.grid(row=5, column=3, stick=tk.W+tk.E)

    def sum(self):
        valor1 = float(self.entry_1.get())
        valor2 = float(self.entry_2.get())
        self.saida['text'] = valor1 + valor2

    def sub(self):
        valor1 = float(self.entry_1.get())
        valor2 = float(self.entry_2.get())
        self.saida['text'] = valor1 - valor2

    def div(self):
        valor1 = float(self.entry_1.get())
        valor2 = float(self.entry_2.get())
        self.saida['text'] = valor1 / valor2

    def mult(self):
        valor1 = float(self.entry_1.get())
        valor2 = float(self.entry_2.get())
        self.saida['text'] = valor1 * valor2

root = tk.Tk()
my_gui = Example(root)
root.mainloop()
