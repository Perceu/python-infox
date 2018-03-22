import turtle
import tkinter as tk

class Example:

    def __init__(self, interface):
        self.interface = interface
        self.interface.title("Titulo")


        # Criando Labels
        self.title = tk.Label(self.interface, text="Usem esse exemplo para fazer os demais scripts terem interface:")
        self.label_1 = tk.Label(self.interface, text="Entrada 1:")
        self.label_2 = tk.Label(self.interface, text="Entrada 2:")
        # Criando Entrys 
        self.entry_1 = tk.Entry(interface)
        self.entry_2 = tk.Entry(interface)
        # Criando Botões e registrando funções
        self.button_1 = tk.Button(self.interface, text="Test 1", command=self.function1 )
        self.button_2 = tk.Button(self.interface, text="Test 2", command=self.function2 )
        self.button_3 = tk.Button(self.interface, text="Test 3", command=self.function3 )

        # Desenhando Entrada
        self.title.grid(row=0, column=0, columnspan=4, stick=tk.W+tk.E)
        
        # Desenhando Input 1
        self.label_1.grid(row=1, column=0)
        self.entry_1.grid(row=1, column=1, columnspan=3, stick=tk.W+tk.E)

        # Desenhando Input 2
        self.label_2.grid(row=2, column=0)
        self.entry_2.grid(row=2, column=1, columnspan=3, stick=tk.W+tk.E)

        # Desenhando Buttons
        self.button_1.grid(row=3, column=1, stick=tk.W+tk.E)
        self.button_2.grid(row=3, column=2, stick=tk.W+tk.E)
        self.button_3.grid(row=3, column=3, stick=tk.W+tk.E)

    def function1(self):
        print("passou na função 1")
        print(type(self.entry_1.get()))

    def function2(self):
        print("passou na função 2")
        print(self.entry_1.get())

    def function3(self):
        print("passou na função 3")
        print(self.entry_2.get())

root = tk.Tk()
my_gui = Example(root)
root.mainloop()
